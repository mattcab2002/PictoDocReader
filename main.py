from matplotlib.image import imread
import numpy as np

imgArray = imread("images/img1.png")
imgSize = imgArray.shape
imgMaxRow = len(imgArray)
imgMaxCol = len(imgArray[0])

docArray = imread("documents/doc1.png")
docSize = docArray.shape
docMaxRow = len(docArray)
docMaxCol = len(docArray[0])


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


for row in range(len(docArray)):
    for col in range(len(docArray[row])):
        if ((docArray[row][col] == imgArray[0][0]).all()):
            i = 0
            j = 0
            i2 = row
            j2 = col

            while (True):

                currentDoc = docArray[i2][j2]
                currentImg = imgArray[i][j]

                if ((currentDoc != currentImg).all()):
                    print("break 1")
                    break
                if ((i == imgMaxRow - 1) and (j == imgMaxCol - 1)):
                    print("found image")

                    break
                if (j + 1 >= imgMaxCol):
                    if ((i + 1) < imgMaxRow):
                        i += 1
                        if ((i2+1) >= docMaxRow):
                            print("break 2")
                            break
                        i2 = i2 + 1
                        j = 0
                        j2 = col
                else:
                    j = j+1
                    if ((j2 + 1) >= docMaxCol):
                        print("break 3")
                        break
                    j2 += 1
            print(row, col)
