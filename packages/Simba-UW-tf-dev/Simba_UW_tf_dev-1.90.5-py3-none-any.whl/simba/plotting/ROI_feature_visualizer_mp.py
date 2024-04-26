__author__ = "Simon Nilsson"

import functools
import itertools
import multiprocessing
import os
import platform
from typing import Any, Dict, List, Optional, Union

import cv2
import numpy as np
import pandas as pd

from simba.mixins.config_reader import ConfigReader
from simba.mixins.plotting_mixin import PlottingMixin
from simba.roi_tools.ROI_feature_analyzer import ROIFeatureCreator
from simba.utils.checks import (check_file_exist_and_readable,
                                check_if_keys_exist_in_dict, check_int,
                                check_valid_lst,
                                check_video_and_data_frm_count_align)
from simba.utils.data import slice_roi_dict_for_video
from simba.utils.enums import Formats, TextOptions
from simba.utils.errors import (BodypartColumnNotFoundError, NoFilesFoundError,
                                ROICoordinatesNotFoundError)
from simba.utils.printing import stdout_success
from simba.utils.read_write import (concatenate_videos_in_folder,
                                    find_core_cnt, get_fn_ext,
                                    get_video_meta_data, read_df,
                                    remove_a_folder)
from simba.utils.warnings import DuplicateNamesWarning

ROI_CENTERS = "roi_centers"
ROI_EAR_TAGS = "roi_ear_tags"
DIRECTIONALITY = "directionality"
DIRECTIONALITY_STYLE = "directionality_style"
BORDER_COLOR = "border_color"
POSE = "pose_estimation"
ANIMAL_NAMES = "animal_names"
STYLE_KEYS = [
    ROI_CENTERS,
    ROI_EAR_TAGS,
    DIRECTIONALITY,
    BORDER_COLOR,
    POSE,
    DIRECTIONALITY_STYLE,
    ANIMAL_NAMES,
]


def _roi_feature_visualizer_mp(
    data: pd.DataFrame,
    text_locations: dict,
    font_size: float,
    circle_size: float,
    save_temp_dir: str,
    video_meta_data: dict,
    shape_info: dict,
    shape_names: list,
    style_attr: dict,
    video_path: str,
    animal_names: list,
    roi_dict: dict,
    bp_lk: dict,
    animal_bps: dict,
    animal_bp_names: List[str],
    animal_bp_dict: dict,
    roi_features_df: pd.DataFrame,
    directing_data: Union[pd.DataFrame, None],
):
    def __insert_texts(shape_info: dict, img: np.ndarray):
        for shape_name, shape_info in shape_info.items():
            shape_color = shape_info["Color BGR"]
            for cnt, animal_data in bp_lk.items():
                animal, animal_bp, _ = animal_data
                animal_name = f"{animal} {animal_bp}"
                cv2.putText(
                    img,
                    text_locations[animal_name][shape_name]["in_zone_text"],
                    text_locations[animal_name][shape_name]["in_zone_text_loc"],
                    font,
                    font_size,
                    shape_color,
                    1,
                )
                cv2.putText(
                    img,
                    text_locations[animal_name][shape_name]["distance_text"],
                    text_locations[animal_name][shape_name]["distance_text_loc"],
                    font,
                    font_size,
                    shape_color,
                    1,
                )
                if directing_data is not None and style_attr[DIRECTIONALITY]:
                    cv2.putText(
                        img,
                        text_locations[animal][shape_name]["directing_text"],
                        text_locations[animal][shape_name]["directing_text_loc"],
                        font,
                        font_size,
                        shape_color,
                        1,
                    )
        return img

    fourcc = cv2.VideoWriter_fourcc(*Formats.MP4_CODEC.value)
    font = cv2.FONT_HERSHEY_COMPLEX
    group_cnt = int(data["group"].values[0])
    start_frm, current_frm, end_frm = data.index[0], data.index[0], data.index[-1]
    save_path = os.path.join(save_temp_dir, f"{group_cnt}.mp4")
    writer = cv2.VideoWriter(
        save_path,
        fourcc,
        video_meta_data["fps"],
        (video_meta_data["width"] * 2, video_meta_data["height"]),
    )
    cap = cv2.VideoCapture(video_path)
    cap.set(1, start_frm)
    while current_frm <= end_frm:
        ret, img = cap.read()
        if ret:
            img = cv2.copyMakeBorder(
                img,
                0,
                0,
                0,
                int(video_meta_data["width"]),
                borderType=cv2.BORDER_CONSTANT,
                value=style_attr[BORDER_COLOR],
            )
            img = __insert_texts(shape_info=shape_info, img=img)
            if style_attr[POSE]:
                for animal_name, bp_data in animal_bp_dict.items():
                    for bp_cnt, bp in enumerate(
                        zip(bp_data["X_bps"], bp_data["Y_bps"])
                    ):
                        bp_cords = data.loc[current_frm, list(bp)].values.astype(
                            np.int64
                        )
                        cv2.circle(
                            img,
                            (bp_cords[0], bp_cords[1]),
                            0,
                            animal_bp_dict[animal_name]["colors"][bp_cnt],
                            circle_size,
                        )
            if style_attr[ANIMAL_NAMES]:
                for animal_name, bp_data in animal_bp_dict.items():
                    headers = [bp_data["X_bps"][-1], bp_data["Y_bps"][-1]]
                    bp_cords = data.loc[current_frm, headers].values.astype(np.int64)
                    cv2.putText(
                        img,
                        animal_name,
                        (bp_cords[0], bp_cords[1]),
                        font,
                        font_size,
                        animal_bp_dict[animal_name]["colors"][0],
                        1,
                    )

            img = PlottingMixin.roi_dict_onto_img(
                img=img,
                roi_dict=roi_dict,
                circle_size=circle_size,
                show_tags=style_attr[ROI_EAR_TAGS],
                show_center=style_attr[ROI_CENTERS],
            )

            for animal_name, shape_name in itertools.product(
                animal_bp_names, shape_names
            ):
                in_zone_col_name = f"{shape_name} {animal_name} in zone"
                distance_col_name = f"{shape_name} {animal_name} distance"
                in_zone_value = str(
                    bool(roi_features_df.loc[current_frm, in_zone_col_name])
                )
                distance_value = round(
                    roi_features_df.loc[current_frm, distance_col_name], 2
                )
                cv2.putText(
                    img,
                    in_zone_value,
                    text_locations[animal_name][shape_name]["in_zone_data_loc"],
                    font,
                    font_size,
                    shape_info[shape_name]["Color BGR"],
                    1,
                )
                cv2.putText(
                    img,
                    str(distance_value),
                    text_locations[animal_name][shape_name]["distance_data_loc"],
                    font,
                    font_size,
                    shape_info[shape_name]["Color BGR"],
                    1,
                )
            if (directing_data is not None) and (style_attr[DIRECTIONALITY]):
                for animal_name, shape_name in itertools.product(
                    animal_names, shape_names
                ):
                    facing_col_name = f"{shape_name} {animal_name} facing"
                    facing_value = roi_features_df.loc[current_frm, facing_col_name]
                    cv2.putText(
                        img,
                        str(bool(facing_value)),
                        text_locations[animal_name][shape_name]["directing_data_loc"],
                        font,
                        font_size,
                        shape_info[shape_name]["Color BGR"],
                        1,
                    )
                    if facing_value:
                        img = PlottingMixin.insert_directing_line(
                            directing_df=directing_data,
                            img=img,
                            shape_name=shape_name,
                            animal_name=animal_name,
                            frame_id=current_frm,
                            color=shape_info[shape_name]["Color BGR"],
                            thickness=shape_info[shape_name]["Thickness"],
                            style=style_attr[DIRECTIONALITY_STYLE],
                        )
            current_frm += 1
            writer.write(np.uint8(img))
            print(
                f"Multiprocessing frame: {current_frm} / {video_meta_data['frame_count']}  on core {group_cnt}..."
            )
        else:
            break
    writer.release()
    return group_cnt


class ROIfeatureVisualizerMultiprocess(ConfigReader):
    """
    Visualize features that depend on the relationships between the location of the animals and user-defined
    ROIs. E.g., distances to centroids of ROIs, cumulative time spent in ROIs, if animals are directing towards ROIs
    etc.

    :param Union[str, os.PathLike] config_path: Path to SimBA project config file in Configparser format
    :param Union[str, os.PathLike] video_path: Path to video file to overlay ROI features on.
    :param List[str] body_parts: List of body-parts to use as proxy for animal location(s).
    :param Dict[str, Any] style_attr: User-defined styles (sizes, colors etc.)
    :param Optional[int] core_cnt: Number of cores to use. Defaults to -1 which is all available cores.

    .. note:
       `Tutorials <https://github.com/sgoldenlab/simba/blob/master/docs/ROI_tutorial.md#part-5-visualizing-roi-features>`__.

        See :meth:`simba.ROI_feature_visualizer.ROIfeatureVisualizer` for single process class. Would be slower but potentially more reliable.

    .. image:: _static/img/ROIfeatureVisualizer_1.png
       :width: 700
       :align: center

    .. image:: _static/img/ROIfeatureVisualizer_2.png
       :width: 700
       :align: center


    :example:
    >>> style_attr = {'ROI_centers': True, 'ROI_ear_tags': True, 'Directionality': True, 'Directionality_style': 'Funnel', 'Border_color': (0, 128, 0), 'Pose_estimation': True}
    >>> _ = ROIfeatureVisualizerMultiprocess(config_path='test_/project_folder/project_config.ini', video_name='Together_1.avi', style_attr=style_attr, core_cnt=3).run()
    """

    def __init__(
        self,
        config_path: Union[str, os.PathLike],
        video_path: Union[str, os.PathLike],
        body_parts: List[str],
        style_attr: Dict[str, Any],
        core_cnt: Optional[int] = -1,
    ):

        if platform.system() == "Darwin":
            multiprocessing.set_start_method("spawn", force=True)
        check_int(
            name=f"{self.__class__.__name__} core_cnt",
            value=core_cnt,
            min_value=-1,
            max_value=find_core_cnt()[0],
        )
        if core_cnt == -1:
            core_cnt = find_core_cnt()[0]
        check_file_exist_and_readable(file_path=video_path)
        ConfigReader.__init__(self, config_path=config_path)
        PlottingMixin.__init__(self)
        check_if_keys_exist_in_dict(
            data=style_attr,
            key=STYLE_KEYS,
            name=f"{self.__class__.__name__} style_attr",
        )
        if not os.path.isfile(self.roi_coordinates_path):
            raise ROICoordinatesNotFoundError(
                expected_file_path=self.roi_coordinates_path
            )
        self.read_roi_data()
        _, self.video_name, _ = get_fn_ext(video_path)
        self.roi_dict, self.shape_names = slice_roi_dict_for_video(
            data=self.roi_dict, video_name=self.video_name
        )
        self.core_cnt, self.style_attr = core_cnt, style_attr
        self.save_path = os.path.join(
            self.roi_features_save_dir, f"{self.video_name}.mp4"
        )
        if not os.path.exists(self.roi_features_save_dir):
            os.makedirs(self.roi_features_save_dir)
        self.save_temp_dir = os.path.join(self.roi_features_save_dir, "temp")
        if os.path.exists(self.save_temp_dir):
            remove_a_folder(folder_dir=self.save_temp_dir)
        os.makedirs(self.save_temp_dir)
        self.data_path = os.path.join(
            self.outlier_corrected_dir, f"{self.video_name}.{self.file_type}"
        )
        if not os.path.isfile(self.data_path):
            raise NoFilesFoundError(
                msg=f"SIMBA ERROR: Could not find the file at path {self.data_path}. Make sure the data file exist to create ROI visualizations",
                source=self.__class__.__name__,
            )
        check_valid_lst(
            data=body_parts,
            source=f"{self.__class__.__name__} body-parts",
            valid_dtypes=(str,),
            min_len=1,
        )
        for bp in body_parts:
            if bp not in self.body_parts_lst:
                raise BodypartColumnNotFoundError(
                    msg=f"The body-part {bp} is not a valid body-part in the SimBA project. Options: {self.body_parts_lst}",
                    source=self.__class__.__name__,
                )
        self.roi_feature_creator = ROIFeatureCreator(
            config_path=config_path,
            body_parts=body_parts,
            append_data=False,
            data_path=self.data_path,
        )
        self.roi_feature_creator.run()
        self.bp_lk = self.roi_feature_creator.bp_lk
        self.animal_names = [v[0] for v in self.bp_lk.values()]
        self.animal_bp_names = [f"{v[0]} {v[1]}" for v in self.bp_lk.values()]
        self.video_meta_data = get_video_meta_data(video_path)
        self.fourcc = cv2.VideoWriter_fourcc(*Formats.MP4_CODEC.value)
        self.cap = cv2.VideoCapture(video_path)
        self.max_dim = max(
            self.video_meta_data["width"], self.video_meta_data["height"]
        )
        self.circle_size = int(
            TextOptions.RADIUS_SCALER.value
            / (TextOptions.RESOLUTION_SCALER.value / self.max_dim)
        )
        self.font_size = float(
            TextOptions.FONT_SCALER.value
            / (TextOptions.RESOLUTION_SCALER.value / self.max_dim)
        )
        self.spacing_scale = int(
            TextOptions.SPACE_SCALER.value
            / (TextOptions.RESOLUTION_SCALER.value / self.max_dim)
        )
        check_video_and_data_frm_count_align(
            video=video_path, data=self.data_path, name=video_path, raise_error=False
        )
        self.style_attr = style_attr
        self.direct_viable = self.roi_feature_creator.roi_directing_viable
        self.data_df = read_df(file_path=self.data_path, file_type=self.file_type)
        self.shape_dicts = self.__create_shape_dicts()
        self.directing_df = self.roi_feature_creator.dr
        self.video_path = video_path
        self.roi_features_df = self.roi_feature_creator.out_df

    def __create_shape_dicts(self):
        shape_dicts = {}
        for shape, df in self.roi_dict.items():
            if not df["Name"].is_unique:
                df = df.drop_duplicates(subset=["Name"], keep="first")
                DuplicateNamesWarning(
                    msg=f'Some of your ROIs with the same shape ({shape}) has the same names for video {self.video_name}. E.g., you have two rectangles named "My rectangle". SimBA prefers ROI shapes with unique names. SimBA will keep one of the unique shape names and drop the rest.',
                    source=self.__class__.__name__,
                )
            d = df.set_index("Name").to_dict(orient="index")
            shape_dicts = {**shape_dicts, **d}
        return shape_dicts

    def __calc_text_locs(self):
        add_spacer = TextOptions.FIRST_LINE_SPACING.value
        self.loc_dict = {}
        for animal_cnt, animal_data in self.bp_lk.items():
            animal, animal_bp, _ = animal_data
            animal_name = f"{animal} {animal_bp}"
            self.loc_dict[animal_name] = {}
            self.loc_dict[animal] = {}
            for shape in self.shape_names:
                self.loc_dict[animal_name][shape] = {}
                self.loc_dict[animal_name][shape][
                    "in_zone_text"
                ] = f"{shape} {animal_name} in zone"
                self.loc_dict[animal_name][shape][
                    "distance_text"
                ] = f"{shape} {animal_name} distance"
                self.loc_dict[animal_name][shape]["in_zone_text_loc"] = (
                    (self.video_meta_data["width"] + 5),
                    (
                        self.video_meta_data["height"]
                        - (self.video_meta_data["height"] + 10)
                        + self.spacing_scale * add_spacer
                    ),
                )
                self.loc_dict[animal_name][shape]["in_zone_data_loc"] = (
                    int(self.img_w_border_w - (self.img_w_border_w / 8)),
                    (
                        self.video_meta_data["height"]
                        - (self.video_meta_data["height"] + 10)
                        + self.spacing_scale * add_spacer
                    ),
                )
                add_spacer += 1
                self.loc_dict[animal_name][shape]["distance_text_loc"] = (
                    (self.video_meta_data["width"] + 5),
                    (
                        self.video_meta_data["height"]
                        - (self.video_meta_data["height"] + 10)
                        + self.spacing_scale * add_spacer
                    ),
                )
                self.loc_dict[animal_name][shape]["distance_data_loc"] = (
                    int(self.img_w_border_w - (self.img_w_border_w / 8)),
                    (
                        self.video_meta_data["height"]
                        - (self.video_meta_data["height"] + 10)
                        + self.spacing_scale * add_spacer
                    ),
                )
                add_spacer += 1
                if self.direct_viable and self.style_attr[DIRECTIONALITY]:
                    self.loc_dict[animal][shape] = {}
                    self.loc_dict[animal][shape][
                        "directing_text"
                    ] = f"{shape} {animal} facing"
                    self.loc_dict[animal][shape]["directing_text_loc"] = (
                        (self.video_meta_data["width"] + 5),
                        (
                            self.video_meta_data["height"]
                            - (self.video_meta_data["height"] + 10)
                            + self.spacing_scale * add_spacer
                        ),
                    )
                    self.loc_dict[animal][shape]["directing_data_loc"] = (
                        int(self.img_w_border_w - (self.img_w_border_w / 8)),
                        (
                            self.video_meta_data["height"]
                            - (self.video_meta_data["height"] + 10)
                            + self.spacing_scale * add_spacer
                        ),
                    )
                    add_spacer += 1

    def __get_border_img_size(self, video_path: Union[str, os.PathLike]):
        cap = cv2.VideoCapture(video_path)
        cap.set(1, 1)
        _, img = self.cap.read()
        bordered_img = cv2.copyMakeBorder(
            img,
            0,
            0,
            0,
            int(self.video_meta_data["width"]),
            borderType=cv2.BORDER_CONSTANT,
            value=[0, 0, 0],
        )
        cap.release()
        return bordered_img.shape[0], bordered_img.shape[1]

    def run(self):
        self.img_w_border_h, self.img_w_border_w = self.__get_border_img_size(
            video_path=self.video_path
        )
        self.__calc_text_locs()
        data_arr, frm_per_core = PlottingMixin.split_and_group_df(
            self,
            df=self.roi_feature_creator.out_df,
            splits=self.core_cnt,
            include_split_order=True,
        )
        print(
            f"Creating ROI feature images, multiprocessing (chunksize: {self.multiprocess_chunksize}, cores: {self.core_cnt})..."
        )
        with multiprocessing.Pool(
            self.core_cnt, maxtasksperchild=self.maxtasksperchild
        ) as pool:
            constants = functools.partial(
                _roi_feature_visualizer_mp,
                text_locations=self.loc_dict,
                font_size=self.font_size,
                circle_size=self.circle_size,
                video_meta_data=self.video_meta_data,
                shape_info=self.shape_dicts,
                roi_dict=self.roi_dict,
                style_attr=self.style_attr,
                save_temp_dir=self.save_temp_dir,
                directing_data=self.directing_df,
                shape_names=self.shape_names,
                animal_bp_names=self.animal_bp_names,
                video_path=self.video_path,
                animal_names=self.animal_names,
                animal_bp_dict=self.animal_bp_dict,
                bp_lk=self.bp_lk,
                roi_features_df=self.roi_features_df,
                animal_bps=self.animal_bp_dict,
            )
            for cnt, result in enumerate(
                pool.imap(constants, data_arr, chunksize=self.multiprocess_chunksize)
            ):
                print(f"Batch core {result+1}/{self.core_cnt} complete...")
            print(f"Joining {self.video_name} multi-processed video...")
            concatenate_videos_in_folder(
                in_folder=self.save_temp_dir,
                save_path=self.save_path,
                video_format="mp4",
                remove_splits=True,
            )
            self.timer.stop_timer()
            pool.terminate()
            pool.join()
            stdout_success(
                msg=f"Video {self.video_name} complete. Video saved in project_folder/frames/output/ROI_features.",
                elapsed_time=self.timer.elapsed_time_str,
            )


#
# style_attr = {'roi_centers': True, 'roi_ear_tags': True, 'directionality': True, 'directionality_style': 'funnel', 'border_color': (0, 0, 0), 'pose_estimation': True, 'animal_names': True}
# test = ROIfeatureVisualizerMultiprocess(config_path='/Users/simon/Desktop/envs/simba/troubleshooting/RAT_NOR/project_folder/project_config.ini',
#                             video_path='/Users/simon/Desktop/envs/simba/troubleshooting/RAT_NOR/project_folder/videos/2022-06-20_NOB_DOT_4.mp4',
#                             style_attr=style_attr,
#                             body_parts=['Nose'], core_cnt=-1)
# test.run()


# style_attr = {'ROI_centers': True,
#               'ROI_ear_tags': True,
#               'Directionality': True,
#               'Directionality_style': 'Funnel',
#               'Border_color': (0, 128, 0),
#               'Pose_estimation': True,
#               'Directionality_roi_subset': ['My_polygon']}

# roi_feature_visualizer = ROIfeatureVisualizerMultiprocess(config_path='/Users/simon/Desktop/envs/simba/troubleshooting/two_black_animals_14bp/project_folder/project_config.ini',
#                                                           video_name='Together_1.avi',
#                                                           style_attr=style_attr,
#                                                           core_cnt=3)
# roi_feature_visualizer.run()


# style_attr = {'ROI_centers': True,
#               'ROI_ear_tags': True,
#               'Directionality': True,
#               'Directionality_style': 'Funnel',
#               'Border_color': (0, 128, 0),
#               'Pose_estimation': True}
# roi_feature_visualizer = ROIfeatureVisualizerMultiprocess(config_path='/Users/simon/Desktop/envs/simba_dev/tests/test_data/mouse_open_field/project_folder/project_config.ini',
#                                                           video_name='Video1.mp4',
#                                                           style_attr=style_attr,
#                                                           core_cnt=3)
# roi_feature_visualizer.create_visualization()
#
# style_attr = {'ROI_centers': True, 'ROI_ear_tags': True, 'Directionality': True, 'Directionality_style': 'Funnel', 'Border_color': (0, 128, 0), 'Pose_estimation': True}
# test = ROIfeatureVisualizerMultiprocess(config_path='/Users/simon/Desktop/envs/simba_dev/tests/test_data/mouse_open_field/project_folder/project_config.ini', video_name='Video1.mp4', style_attr=style_attr, core_cnt=5)
# test.create_visualization()
