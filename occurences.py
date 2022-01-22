import time
from plotOutline import *
from main import imgWidth, imgHeight, docArray


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


def findAllOccurences(func, row, col, x, y, count):
    start_time = time.time()
    if (findOccurence(func, row-x, col-y)):
        print("--- %s seconds ---" %
              (time.time() - start_time))  # print execution time
        print("{}th Occurence located @ Top Left Corner: ({},{}), Top Right Corner: ({},{}), Bottom Left Corner: ({},{}), Bottom Right Corner: ({},{})".format(count,
                                                                                                                                                               row, col, row+imgWidth, col, row, col+imgHeight, row+imgWidth, col+imgHeight))
        showImage(docArray, row-x, col-y, imgWidth, imgHeight, 4)