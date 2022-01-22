from matplotlib.image import imread
import numpy as np

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
        if (pixelsMatch(row, col+imgWidth-1, 0, -1)):  # bottom left
            if (pixelsMatch(row+imgHeight-1, col, -1, 0)):  # top right
                if (pixelsMatch(row+imgHeight-1, col+imgWidth-1, -1, -1)):  # bottom right
                    return True
    else:
        return False

def validateFullImage(row, col , docArray , docHeight , docWidth):
    for i in range(imgHeight):
        for j in range(imgWidth):
            try:
                # check all elements of doc to image
                if (pixelsMatch(row + i, col + j, i, j , docArray , docHeight , docWidth)):
                    continue
                else:
                    return False
            except IndexError:
                return False
    return True

def diagonalSearch1(row, col, docArray, docHeight, docWidth):
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


def diagonalSearch2(doc, row, col, img, imgWidth, imgHeight, docArray, docHeight, docWidth):
    j = imgWidth - 1
    for i in range(imgHeight - 1, 0, -1):
        try:
            if (doc[row + i][col + j] != img[i][j]).all():
                return False
            else:
                j -= 1
                continue
        except IndexError:
            return False
    return True


def main():
    pass
if __name__ == "__main__":
    main()