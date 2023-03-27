# Get Hardware
from Content.Python.DataHelper import saveData
from Content.Python.HardwareGrabber import grabHardware
from Content.Python.MetadataGrabber import grabPostRenderMeta, grabPreRenderMeta
from Content.Python.RenderHelper import render
from Content.Python.SettingsGrabber import grabSettings

hardware = grabHardware()

# Get Settings
settings = grabSettings()

# Get Initial Metadata
metaOne = grabPreRenderMeta()

# Render
render()

# Get Final Metadata
metaTwo = grabPostRenderMeta(metaOne["startTime"])

# Get Data/Send Data
saveData(hardware, settings, metaOne, metaTwo)
