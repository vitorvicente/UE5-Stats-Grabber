"""
    Copyright @Algorithm.ie.

    :author: vitor@bu.edu.
"""
import csv
import os
import time

import numpy

"""
    Header for the Master Data File.
"""
HEADER = ["shotName", "levelName", "action", "renderLocation", "projectLocation",
          "startTime", "endTime", "totalTime", "totalFrames", "avgFrameTime",
          "frameTimeMap", "resolution", "spatial_samples", "temporal_samples", "console_variables",
          "settings_notes", "CPU", "GPU", "RAM"]


def mergeFiles(folder="./data/"):
    """
    Helper Function to Merge all existing Data Files into a Master File.

    :param folder: Data Folder to read from/write to.
    :return: None.
    """
    fileName = "Master_File-" + time.ctime(time.time()).replace(" ", "_").replace(":", "-")
    data = extractAllFiles(folder)
    if data == 1:
        return 1
    writeFile(folder, fileName, data)


def writeFile(folder, fileName, data):
    """
    Helper Function to Write the data to a Master File.

    :param folder: Data Folder to write to.
    :param fileName: Name for the Master Data File.
    :param data: Data to write to the File.
    :return: None.
    """
    upperPath = os.path.join("c:\\", os.getcwd() + folder + "master/")

    if not os.path.exists(upperPath):
        os.mkdir(upperPath)

    with open((folder + "master/" + fileName), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)
        for entry in data:
            writer.writerow(entry)


def extractAllFiles(folder):
    """
    Helper Function to Extract all Data from the csv Files in a Folder.

    :param folder: Data Folder to read from.
    :return: Read Data Array.
    """
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
    """
    Helper Function to verify that a File is a Render Statistics Data File.

    :param file: File to Check.
    :return: 1 if Valid, 0 if Invalid.
    """
    lead = file.readline()
    if numpy.array_equiv(lead, HEADER):
        return 1

    return 0


def extractData(file):
    """
    Helper Function to Extract Data from a specific Data File.

    :param file: File to Read From.
    :return: Data from the File.
    """
    fileData = []
    reader = csv.reader(file)
    for line in reader:
        fileData.append(line)

    return fileData
