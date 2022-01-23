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


def longestPrefixSuffix(s):
    n = len(s)
    lps = [0] * n
    l = 0
    i = 1
    while (i < n):
        if (s[i] == s[l]):
            l = l + 1
            lps[i] = l
            i = i + 1
        else:
            if (l != 0):
                l = lps[l - 1]
            else:
                lps[i] = 0
                i = i + 1
    return lps


def KMP(row, x, y, docArray, imgArray):
    if len(docArray[0][0]) == 4:
        docArray = docArray[:, :, 0:-1]
    if len(imgArray[0][0]) == 4:
        imgArray = imgArray[:, :, 0:-1]

    docRow = docArray[row].flatten()
    imgRow = imgArray[x].flatten()
    n = len(docRow)
    m = len(imgRow)
    i = 0
    j = 0
    lps = longestPrefixSuffix(imgRow)
    colLst = []
    while (i < n):
        if imgRow[j] == docRow[i]:
            i += 1
            j += 1

        if j == m:
            col = int(((i - m) / 3) - y)
            colLst.append(col)

            j = lps[j - 1]

        elif i < n and imgRow[j] != docRow[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return colLst


def main():
    crop = cropImage()
    count = 0
    x = crop[0]
    y = crop[1]
    func_dict = {"0": validateCorners,
                 "1": diagonalSearch, "2": validateFullImage}
    for row in range(docHeight-imgHeight+1):
        KMPLst = KMP(row, x, y, docArray, imgArray)
        if (len(KMPLst) != 0):
            for col in KMPLst:
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
    for entry in os.scandir(r'convertedPages'):
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
