from matplotlib.image import imread
import numpy as np
import sys
from plotOutline import *
import time
import shutil
import os

imgArray = imread("images/img5.png")
imgSize = imgArray.shape
imgHeight = len(imgArray)
imgWidth = len(imgArray[0])

docArray = imread("documents/doc5.png")
docSize = docArray.shape
docHeight = len(docArray)
docWidth = len(docArray[0])

def findOccurence(func, x, y):
    return func(x, y)


def findFirstOccurence(func, row, col, x, y):
    start_time = time.time()
    if (findOccurence(func, row-x, col-y)):
        print("--- %s seconds ---" %
              (time.time() - start_time))  # print execution time
        print("Top Left Corner: ({},{}), Top Right Corner: ({},{}), Bottom Left Corner: ({},{}), Bottom Right Corner: ({},{})".format(
            row, col, row+imgWidth, col, row, col+imgHeight, row+imgWidth, col+imgHeight))
        showImage(docArray, row-x, col-y, imgWidth, imgHeight, 4)
        exit(0)


def findAllOccurences(func, row, col, x, y, count):
    start_time = time.time()
    if (findOccurence(func, row-x, col-y)):
        print("--- %s seconds ---" %
              (time.time() - start_time))  # print execution time
        print("{}th Occurence located @ Top Left Corner: ({},{}), Top Right Corner: ({},{}), Bottom Left Corner: ({},{}), Bottom Right Corner: ({},{})".format(count,
                                                                                                                                                               row, col, row+imgWidth, col, row, col+imgHeight, row+imgWidth, col+imgHeight))
        showImage(docArray, row-x, col-y, imgWidth, imgHeight, 4)

def pixelsMatch(docRow, docCol, imgRow, imgCol):
    if (docRow >= docHeight) or (docCol >= docWidth):
        return False
    minlen = min(len(docArray[docRow][docCol]), len(imgArray[imgRow][imgCol]))
    for i in range(minlen):
        if (docArray[docRow][docCol][i] != imgArray[imgRow][imgCol][i]):
            return False
    return True


def validateCorners(row, col):
    if (pixelsMatch(row, col, 0, 0)):  # top left
        if (pixelsMatch(row, col+imgWidth-1, 0, -1)):  # bottom left
            if (pixelsMatch(row+imgHeight-1, col, -1, 0)):  # top right
                if (pixelsMatch(row+imgHeight-1, col+imgWidth-1, -1, -1)):  # bottom right
                    print("Found Image")
                    return True
    else:
        return False


def validateFullImage(row, col):
    for i in range(imgHeight):
        for j in range(imgWidth):
            try:
                # check all elements of doc to image
                if (pixelsMatch(row + i, col + j, i, j)):
                    continue
                else:
                    return False
            except IndexError:
                return False
    return True

def cropImage():
    pixel = imgArray[0][0]
    for row in range(imgHeight):
        for col in range(imgWidth):
            if not(pixelsMatch(row, col, 0, 0)):
                return [row, col]
            else:
                continue
    return [0, 0]


def diagonalSearch(row, col, docArray, docHeight, docWidth):
    j = 0
    for i in range(imgHeight):
        try:
            if not (pixelsMatch(row + i, col + j, i, j)):
                return False
            else:
                j += 1
                continue
        except IndexError:
            return False
    print("Found Image")
    return True


def main():
    crop = cropImage()
    count = 0
    x = crop[0]
    y = crop[1]
    func_dict = {"0": validateCorners,
                 "1": diagonalSearch, "2": validateFullImage}
    print(imgArray[0][0])
    for row in range(docHeight-imgHeight+1):
        for col in range(docWidth-imgWidth+1):
            if (pixelsMatch(row, col, x, y)):  # find first instance of correct pixel
                if(sys.argv[1] == "0"):
                    findFirstOccurence(
                        func_dict[sys.argv[2]], row, col, x, y)
                elif(sys.argv[1] == "1"):
                    findAllOccurences(
                        func_dict[sys.argv[2]], row, col, x, y, count)
                    count += 1
                    break
                else:
                    print("Invalid command")
                    exit(0)


if __name__ == "__main__":
    for entry in os.scandir(r'pages'):
        if (entry.path.endswith('.png')):
            docArray = imread(entry.path)
            docSize = docArray.shape
            docHeight = len(docArray)
            docWidth = len(docArray[0])
            main()
    # copy documents and image to assets for future reference
    shutil.copyfile(os.path.join('images/', os.listdir('images/')
                    [0]), os.path.join('assets/', os.listdir('images/')[0]))
    shutil.rmtree(f'images/')
    shutil.copyfile(os.path.join('documents/', os.listdir('documents/')
                    [0]), os.path.join('assets/', os.listdir('documents/')[0]))
    shutil.rmtree(f'documents/')