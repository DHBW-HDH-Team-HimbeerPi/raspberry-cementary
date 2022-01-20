from pathlib import Path
import csv

def readSprite(fileName):
    basePath = Path(__file__).parent
    filePath = (basePath / ("../sprites/"+fileName)).resolve()

    with open(filePath) as file:
        sprite = [line for line in csv.reader(file)]
        return sprite