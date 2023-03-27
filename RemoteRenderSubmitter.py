import unreal

from DataHelper import saveData
from RenderHelper import render
from MetadataGrabber import grabPreRenderMeta, grabPostRenderMeta
from SettingsGrabber import grabSettings
from HardwareGrabber import grabHardware


@unreal.uclass()
class MyCustomRemoteRenderSubmitter(unreal.MoviePipelineExecutorBase):

    @unreal.ufunction(override=True)
    def execute(self, pipeline_queue):
        unreal.log("Execute!")
        # Get Hardware
        hardware = grabHardware()

        # Get Settings
        settings = grabSettings()

        # Get Initial Metadata
        metaOne = grabPreRenderMeta()

        # Render
        render()

        # Get Final Metadata
        metaTwo = grabPostRenderMeta()

        # Get Data/Send Data
        saveData(hardware, settings, metaOne, metaTwo)
