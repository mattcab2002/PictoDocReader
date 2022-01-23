import matplotlib.pyplot as plt
import sys


def showImage(doc, row, col, imgWidth, imgHeight, thicc):
    doclist = doc.tolist()
    for i in range(row, row + imgHeight):
        for j in range(col, col + imgWidth):
            if (i < row + thicc or row + imgHeight - thicc < i < row + imgHeight):
                doclist[i][j][0] = 255
                doclist[i][j][1] = 0
                doclist[i][j][2] = 0
            elif (j < col + thicc or col + imgWidth - thicc < j < col + imgWidth):
                doclist[i][j][0] = 255
                doclist[i][j][1] = 0
                doclist[i][j][2] = 0
            else:
                doclist[i][j][1] = doclist[i][j][1] * 0.97  # Highlight Yellow
                doclist[i][j][2] = doclist[i][j][2] * 0.84  # Highlight Yellow
    imgplot = plt.imshow(doclist)
    plt.savefig('output/output.png')


def plotPixel(image, x, y):
    doclist = image.tolist()
    if (len(image[0][0]) == 4):
        doclist[x][y] = [255.0, 0.0, 0.0, 1.0]
        doclist[x][y+1] = [255.0, 0.0, 0.0, 1.0]
        doclist[x+1][y+1] = [255.0, 0.0, 0.0, 1.0]
        doclist[x+1][y] = [255.0, 0.0, 0.0, 1.0]
    if (len(image[0][0]) == 3):
        doclist[x][y] = [0.0, 255.0, 0.0]
        doclist[x][y+1] = [0.0, 255.0, 0.0]
        doclist[x+1][y+1] = [0.0, 255.0, 0.0]
        doclist[x+1][y] = [0.0, 255.0, 0.0]

    docNumpy = np.array(doclist)
    imgplot = plt.imshow(docNumpy)
    plt.show()
