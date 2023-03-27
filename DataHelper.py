import csv
import os
import time
import numpy

HARDWARE_CHECKER = {"CPU": "String", "GPU": "String", "RAM": "String"}
SETTINGS_CHECKER = {"resolution": "String",
                    "spatial_samples": "Numerical",
                    "temporal_samples": "Numerical",
                    "console_variables": "StrArray",
                    "settings_notes": "String"}
META_ONE_CHECKER = {"shotName": "String",
                    "levelName": "String",
                    "action": "String",
                    "renderLocation": "String",
                    "projectLocation": "String",
                    "startTime": "Numerical"}
META_TWO_CHECKER = {"endTime": "Numerical",
                    "totalTime": "Numerical",
                    "totalFrames": "Numerical",
                    "avgFrameTime": "Numerical",
                    "frameTimeMap": "NumArray"}


def saveData(hardware, settings, metaOne, metaTwo):
    if checkMap(hardware, HARDWARE_CHECKER) + checkMap(settings, SETTINGS_CHECKER) \
            + checkMap(metaOne, META_ONE_CHECKER) + checkMap(metaTwo, META_TWO_CHECKER) != 0:
        print(checkMap(metaTwo, META_TWO_CHECKER))
        return 1

    fileName = "./data/" + metaOne["shotName"].replace(" ", "_") + "-" + str(time.ctime(metaTwo["endTime"])) \
        .replace(" ", "_").replace(":", "-") + ".csv"
    header = []
    row = []
    for valueMap in [metaOne, metaTwo, settings, hardware]:
        for key, value in valueMap.items():
            header.append(key)
            if key == "startTime" or key == "endTime":
                row.append(time.ctime(value))
            else:
                row.append(value)

    directory = os.path.join("c:\\", os.getcwd() + "./data/")

    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(fileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(row)

    return 0


def checkMap(valueMap, checker):
    if type(valueMap) != dict:
        return 1
    elif len(valueMap) == 0:
        return 1
    elif not numpy.array_equiv(checker.keys(), valueMap.keys()):
        return 1

    for key in checker.keys():
        if checker[key] == "String":
            if not type(valueMap[key]) == str:
                print(valueMap[key])
                return 1
        elif checker[key] == "Numerical":
            if not (type(valueMap[key]) == int or type(valueMap[key]) == float):
                return 1
        elif checker[key] == "StrArray":
            if (not type(valueMap[key]) == list) or (len(valueMap[key]) == 0) or (not type(valueMap[key][0]) == str):
                return 1
        elif checker[key] == "NumArray":
            if (not type(valueMap[key]) == list) or (len(valueMap[key]) == 0) or \
                    (not (type(valueMap[key][0]) == int or type(valueMap[key][0]) == float)):
                return 1

    return 0
