from glob import glob
from matplotlib.image import imread
import threading
import numpy as np
# from occurences import *
import random
import os
import shutil
from os import walk
from pdfToImgConverter import convert_pdf_to_image
import time
from plotOutline import *
from queue import Queue
from storage import store_file

# picture to search in
imgArray = imread(os.path.join('images/', os.listdir('images/')[0]))
imgSize = imgArray.shape
imgHeight = len(imgArray)
imgWidth = len(imgArray[0])

test = []
active = True


def findOccurence(func, x, y, docArray, docHeight, docWidth):
    return func(x, y, docArray, docHeight, docWidth)


def findFirstOccurence(func, row, col, x, y, docArray, docHeight, docWidth):
    global active
    global test
    if (findOccurence(func, row-x, col-y, docArray, docHeight, docWidth)):
        print("--- %s seconds ---" %
              (time.time() - start_time))  # print execution time
        print("Top Left Corner: ({},{}), Top Right Corner: ({},{}), Bottom Left Corner: ({},{}), Bottom Right Corner: ({},{})".format(
            row, col, row+imgWidth, col, row, col+imgHeight, row+imgWidth, col+imgHeight))
        active = False
        test = [docArray, row-x, col-y, imgWidth, imgHeight, 4]


def findAllOccurences(func, row, col, x, y, count, docArray, docHeight, docWidth):
    start_time = time.time()
    if (findOccurence(func, row-x, col-y, docArray, docHeight, docWidth)):
        print("--- %s seconds ---" %
              (time.time() - start_time))  # print execution time
        print("{}th Occurence located @ Top Left Corner: ({},{}), Top Right Corner: ({},{}), Bottom Left Corner: ({},{}), Bottom Right Corner: ({},{})".format(
            count, row, col, row+imgWidth, col, row, col+imgHeight, row+imgWidth, col+imgHeight))

        text.append([docArray, row-x, col-y, imgWidth, imgHeight, 4])


def pixelsMatch(docRow, docCol, imgRow, imgCol, docArray, docHeight, docWidth):
    if (docRow >= docHeight) or (docCol >= docWidth):
        return False
    minlen = min(len(docArray[docRow][docCol]), len(imgArray[imgRow][imgCol]))
    for i in range(minlen):
        if (docArray[docRow][docCol][i] != imgArray[imgRow][imgCol][i]):
            return False
    return True


def pixelsMatchImg(imgRow, imgCol):
    for i in range(len(imgArray[0][0])):
        if (imgArray[imgRow][imgCol][i] != imgArray[0][0][i]):
            return False
    return True


def cropImage(imgWidth, imgHeight):
    for row in range(imgHeight):
        for col in range(imgWidth):
            if not(pixelsMatchImg(row, col)):
                return [row, col]
    return [0, 0]


def validateCorners(row, col, docArray, docHeight, docWidth):
    if (pixelsMatch(row, col, 0, 0, docArray, docHeight, docWidth)):  # top left
        if (pixelsMatch(row + imgHeight - 1, col, -1, 0, docArray, docHeight, docWidth)):  # top right
            if (pixelsMatch(row, col + imgWidth - 1, 0, -1, docArray, docHeight, docWidth)):  # bottom left
                if (pixelsMatch(row+imgHeight-1, col+imgWidth-1, -1, -1, docArray, docHeight, docWidth)):  # bottom right
                    return True
    else:
        return False


def randomSearch(row, col, docArray, docHeight, docWidth):
    factor = 0.05 * imgHeight * imgWidth
    # n can quantify the accuracy
    n = int(factor)
    for i in range(n):
        x = random.randint(0, imgHeight - 1)
        y = random.randint(0, imgWidth - 1)
        try:
            if (not pixelsMatch(row + x, col + y, x, y, docArray, docHeight, docWidth)):
                return False
            else:
                continue
        except IndexError:
            return False
    return True


def diagonalSearch(row, col, docArray, docHeight, docWidth):
    j = 0
    for i in range(imgHeight):
        try:
            if ((not pixelsMatch(row + i, col + j, i, j, docArray, docHeight, docWidth))):
                return False
            else:
                j += 1
                continue
        except IndexError:
            return False
    return True


def validateFullImage(row, col, docArray, docHeight, docWidth):
    for i in range(imgHeight):
        for j in range(imgWidth):
            try:
                # check all elements of doc to image
                if (pixelsMatch(row + i, col + j, i, j, docArray, docHeight, docWidth)):
                    continue
                else:
                    return False
            except IndexError:
                return False
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


def KMP(row, x, docArray, imgArray):
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
            return True
        elif i < n and imgRow[j] != docRow[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def main(docArray, docHeight, docWidth):
    crop = cropImage(imgWidth, imgHeight)
    count = 0
    x = crop[0]
    y = crop[1]
    func_dict = {"0": validateCorners,
                 "1": randomSearch, "2": validateFullImage}

    for row in range(docHeight-imgHeight):
        if(KMP(row, x, docArray, imgArray)):
            for col in range(docWidth-imgWidth):
                if(sys.argv[1] == "0"):
                    findFirstOccurence(
                        func_dict[sys.argv[2]], row, col, x, y, docArray, docHeight, docWidth)
                elif(sys.argv[1] == "1"):
                    findAllOccurences(
                        func_dict[sys.argv[2]], row, col, x, y, count, docArray, docHeight, docWidth)
                    count += 1
                    break
                else:
                    print("Invalid command")
                    exit(0)


def unPack(lst):
    for i in lst:
        main(i[0], i[1], i[2])


if __name__ == "__main__":

    start_time = time.time()
    pages = dict()
    i = 1
    for entry in os.scandir(r'convertedPages'):
        if (entry.path.endswith('.png')):
            docA = imread(entry.path)  # convertedPages/converted_page3.png
            docSize = docA.shape
            docH = len(docA)
            docW = len(docA[0])
            pages[i] = (docA, docH, docW)
            i += 1

    # copy documents and image to assets for future reference
    # 15-20 seconds
    # store_file(os.path.join('images/', os.listdir('images/')
    #                         [0]), 'png')
    # shutil.rmtree(f'images/')
    # store_file(os.path.join('documents/', os.listdir('documents/')
    #                         [0]), 'png')
    # shutil.rmtree(f'documents/')

    numberOfPages = len(pages)
    start = 1
    while (active):
        if (start >= numberOfPages):
            break
        if ((numberOfPages - start) <= 11):
            end = numberOfPages - start + 1
        else:
            end = 11
        threads = []
        for i in range(start, start + end):
            t = threading.Thread(target=main, args=(
                pages[i][0], pages[i][1], pages[i][2]))
            t.daemon = True
            threads.append(t)
        for i in threads:
            i.start()
        for i in threads:
            i.join()
        start += 11

    showImage(test[0], test[1], test[2], test[3], test[4], test[5])
