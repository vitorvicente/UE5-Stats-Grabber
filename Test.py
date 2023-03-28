"""
    Copyright @Algorithm.ie.

    :author: vitor@bu.edu.
"""
import time

from Content.Python.DataHelper import saveData
from Content.Python.FileMerger import mergeFiles
from Content.Python.HardwareGrabber import grabHardware
from Content.Python.MetadataGrabber import grabPostRenderMeta, grabPreRenderMeta
from Content.Python.RenderHelper import render
from Content.Python.SettingsGrabber import grabSettings


def full_test():
    """
    Helper Function to perform a Full Systems Check.

    :return: None.
    """
    gen_test()
    mergeFiles()


def gen_test(amount=10, wait=10):
    """
    Helper Function to Test the Data Gathering System.

    :param amount: Number of Data Samples to take.
    :param wait: Resting Period between Data Samples.
    :return: None.
    """
    for i in range(amount):
        hardware = grabHardware()

        # Get Settings
        settings = grabSettings(None)

        # Get Initial Metadata
        metaOne = grabPreRenderMeta(None)

        # Render
        render(None)

        # Get Final Metadata
        metaTwo = grabPostRenderMeta(None, metaOne["startTime"])

        # Get Data/Send Data
        saveData(hardware, settings, metaOne, metaTwo)
        time.sleep(wait)


def compile_test():
    """
    Helper Function to Test the Data Compilation System.

    :return: None.
    """
    mergeFiles()


# Run Full Test.
full_test()
