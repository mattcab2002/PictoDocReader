from matplotlib.image import imread
import numpy as np
<<<<<<< HEAD
import sys
=======
>>>>>>> image-conversion

imgArray = imread("images/img1.png")
imgSize = imgArray.shape
imgHeight = len(imgArray)
imgWidth = len(imgArray[0])

docArray = imread("documents/doc1.png")
docSize = docArray.shape
docHeight = len(docArray)
docWidth = len(docArray[0])
<<<<<<< HEAD
=======


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


>>>>>>> pdf-conversion


def pixelsMatch(docRow, docCol, imgRow, imgCol):
    if (docRow >= docHeight) or (docCol >= docWidth):
        return False
    minlen = min(len(docArray[docRow][docCol]), len(imgArray[imgRow][imgCol]))
    for i in range(minlen):
        if (docArray[docRow][docCol][i] != imgArray[imgRow][imgCol][i]):
            return False
    return True


<<<<<<< HEAD
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
>>>>>>> image-conversion
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
>>>>>>> image-conversion
                    continue
                else:
                    return False
            except IndexError:
                return False
<<<<<<< HEAD
    print("Found Image")
    return True


def diagonalSearch(row, col, docArray, docHeight, docWidth):
    j = 0
    for i in range(imgHeight):
        try:
            if not (pixelsMatch(row + i, col + j, i, j)):
=======
    return True


def diagonalSearch1(row, col, docArray, docHeight, docWidth):
    j = 0
    for i in range(imgHeight):
        try:
            if ((not pixelsMatch(row + i, col + j, i, j, docArray, docHeight, docWidth))):
>>>>>>> image-conversion
                return False
            else:
                j += 1
                continue
        except IndexError:
            return False
<<<<<<< HEAD
    print("Found Image")
=======
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
>>>>>>> image-conversion
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
>>>>>>> image-conversion


if __name__ == "__main__":
    main()
=======
                if ((currentDoc != currentImg).all()):
                    print("break 1")
                    break
                if ((i == imgHeight - 1) and (j == imgWidth - 1)):
                    print("found image")

                    break
                if (j + 1 >= imgWidth):
                    if ((i + 1) < imgHeight):
                        i += 1
                        if ((i2+1) >= docHeight):
                            print("break 2")
                            break
                        i2 = i2 + 1
                        j = 0
                        j2 = col
                else:
                    j = j+1
                    if ((j2 + 1) >= docWidth):
                        print("break 3")
                        break
                    j2 += 1
            print(row, col)
>>>>>>> pdf-conversion
