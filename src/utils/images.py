import os


def getImage(imagePath):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, imagePath)
