import time


def grabPreRenderMeta():
    shotName = "Test Shot"
    levelName = "Test Level"
    action = "Test Action"
    renderLocation = "c:/Test/Render"
    projectLocation = "c:/Test/Project"
    startTime = time.time()

    return {
        "shotName": shotName,
        "levelName": levelName,
        "action": action,
        "renderLocation": renderLocation,
        "projectLocation": projectLocation,
        "startTime": startTime
    }


def grabPostRenderMeta(startTime):
    endTime = time.time()
    totalTime = (startTime - endTime) / 60
    totalFrames = 1000
    avgFrameTime = 100
    frameTimeMap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return {
        "endTime": endTime,
        "totalTime": totalTime,
        "totalFrames": totalFrames,
        "avgFrameTime": avgFrameTime,
        "frameTimeMap": frameTimeMap
    }
