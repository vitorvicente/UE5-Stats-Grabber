"""
    Copyright @Algorithm.ie.

    :author: vitor@bu.edu.
"""
import unreal

from Content.Python.Plugin.DataHelper import saveData
from RenderHelper import render
from MetadataGrabber import grabPreRenderMeta, grabPostRenderMeta
from SettingsGrabber import grabSettings
from Content.Python.Plugin.HardwareGrabber import grabHardware


@unreal.uclass()
class MyCustomRemoteRenderSubmitter(unreal.MoviePipelineExecutorBase):
    """
        Main implementation of the Remote Render Plugin.
        Allowing the output of a comprehensive set of render statistics to be printed out after a render.
    """

    @unreal.ufunction(override=True)
    def execute(self, pipeline_queue):
        """
        Main Render Execute Function, overrides Default Implementation.

        :param pipeline_queue: Render Pipeline Queue.
        :return: None.
        """

        hardware = grabHardware()

        for video in pipeline_queue.get_jobs():
            self.renderVideo(video, hardware)

    def renderVideo(self, video, hardware):
        """
        Helper Function to Render an individual Video on the Queue and save the statistics related to its Render..

        :param video: Video to be rendered.
        :param hardware: Hardware Metadata for the Machine.
        :return: None.
        """

        self.set_status_message("Pre-Render Setup")
        settings = grabSettings(video)

        metaOne = grabPreRenderMeta(video)

        self.set_status_message("Rendering")
        render(video)

        self.set_status_message("Post-Render Cleanup")
        metaTwo = grabPostRenderMeta(video, metaOne.startTime)

        saveData(hardware, settings, metaOne, metaTwo)
