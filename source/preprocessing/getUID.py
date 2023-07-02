# Extracted from Li, P., Wang, S., Li, T., Lu, J., HuangFu, Y., & Wang, D. (2020). A Large-Scale CT and PET/CT Dataset for Lung Cancer Diagnosis (Lung-PET-CT-Dx) [Data set]. The Cancer Imaging Archive. https://doi.org/10.7937/TCIA.2020.NNC2-0461

import os
from preprocessing.utils import *


def getUID_path(path):
    dict = {}
    list = os.listdir(path)

    for date in list:
        date_path = os.path.join(path, date)
        series_list = os.listdir(date_path)
        series_list.sort()

        for series in series_list:
            series_path = os.path.join(date_path, series)
            dicom_list = os.listdir(series_path)
            dicom_list.sort()

            for dicom in dicom_list:
                dicom_path = os.path.join(series_path, dicom)
                info = loadFileInformation(dicom_path)
                dict[info['dicom_num']] = (dicom_path, dicom)

    return dict


def getUID_file(path):
    info = loadFileInformation(path)
    UID = info['dicom_num']
    return UID
