def grabSettings():
    resolution = "1980x1080"
    spatial_samples = 4
    temporal_samples = 4
    console_variables = [
        "r.VolumetricFog.GridPixelSize 1",
        "r.VolumetricFog.GridSizeZ 256",
        "r.VolumetricFog.HistoryWeight 0.5"
    ]
    settings_notes = "Test Notes!"

    return {
        "resolution": resolution,
        "spatial_samples": spatial_samples,
        "temporal_samples": temporal_samples,
        "console_variables": console_variables,
        "settings_notes": settings_notes
    }
