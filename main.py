from matplotlib.image import imread
import numpy as np
import sys

imgArray = imread("images/img1.png")
imgSize = imgArray.shape
imgHeight = len(imgArray)
imgWidth = len(imgArray[0])

docArray = imread("documents/doc1.png")
docSize = docArray.shape
docHeight = len(docArray)
docWidth = len(docArray[0])


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
<<<<<<< HEAD
        if (pixelsMatch(row, col+imgWidth-1, 0, -1)):  # bottom left
            if (pixelsMatch(row+imgHeight-1, col, -1, 0)):  # top right
                if (pixelsMatch(row+imgHeight-1, col+imgWidth-1, -1, -1)):  # bottom right
                    print("Found Image")
=======
        if (pixelsMatch(row, col + imgWidth - 1, 0, -1)):  # bottom left
            if (pixelsMatch(row + imgHeight - 1, col, -1, 0)):  # top right
                if (pixelsMatch(row + imgHeight - 1, col + imgWidth - 1, -1, -1)):  # bottom right
>>>>>>> de9dc7df8d2217cbe0c636ae73006fab20cf31ef
                    return True
    else:
        return False


def validateFullImage(row, col, docArray, docHeight, docWidth):
    for i in range(imgHeight):
        for j in range(imgWidth):
            try:
                # check all elements of doc to image
<<<<<<< HEAD
                if (pixelsMatch(row + i, col + j, i, j)):
=======
                if (pixelsMatch(row + i, col + j, i, j, docArray, docHeight, docWidth)):
>>>>>>> de9dc7df8d2217cbe0c636ae73006fab20cf31ef
                    continue
                else:
                    return False
            except IndexError:
                return False
    print("Found Image")
    return True


<<<<<<< HEAD
def diagonalSearch(row, col, docArray, docHeight, docWidth):
=======
def diagonalSearch1(row, col, docArray, docHeight, docWidth):
>>>>>>> de9dc7df8d2217cbe0c636ae73006fab20cf31ef
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
<<<<<<< HEAD
    for row in range(docHeight-imgHeight+1):
        for col in range(docWidth-imgWidth+1):
            if (pixelsMatch(row, col, 0, 0)):  # find first instance of correct pixel
                if(sys.argv[1] == "0"):
                    validateCorners(row, col)
                elif (sys.argv[1] == "1"):
                    validateFullImage(row, col, docArray, docHeight, docWidth)
                elif(sys.argv[1] == "2"):
                    diagonalSearch(row, col, docArray, docHeightdocWidth)
                else:
                    print("Invalid command")
                    exit(0)
=======
    pass
>>>>>>> de9dc7df8d2217cbe0c636ae73006fab20cf31ef


if __name__ == "__main__":
    main()
