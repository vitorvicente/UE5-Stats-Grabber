import csv
import os
import time

import numpy

HEADER = ["shotName", "levelName", "action", "renderLocation", "projectLocation",
          "startTime", "endTime", "totalTime", "totalFrames", "avgFrameTime",
          "frameTimeMap", "resolution", "spatial_samples", "temporal_samples", "console_variables",
          "settings_notes", "CPU", "GPU", "RAM"]


def mergeFiles(folder="./data/"):
    fileName = "Master_File-" + time.ctime(time.time()).replace(" ", "_").replace(":", "-")
    data = extractAllFiles(folder)
    if data == 1:
        return 1
    writeFile(folder, fileName, data)


def writeFile(folder, fileName, data):
    header = HEADER
    upperPath = os.path.join("c:\\", os.getcwd() + folder + "master/")

    if not os.path.exists(upperPath):
        os.mkdir(upperPath)

    with open((folder + "master/" + fileName), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)
        for entry in data:
            writer.writerow(entry)


def extractAllFiles(folder):
    directory = os.path.join("c:\\", os.getcwd() + folder)
    finalData = []

    if not os.path.exists(directory):
        return 1

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv") and ("Master" not in file):
                f = open(folder + file, 'r')
                if checkFile(f) == 0:
                    finalData.extend(extractData(f))
                f.close()

    return finalData


def checkFile(file):
    lead = file.readline()
    if numpy.array_equiv(lead, HEADER):
        return 1

    return 0


def extractData(file):
    fileData = []
    reader = csv.reader(file)
    for line in reader:
        fileData.append(line)

    return fileData

mergeFiles()
