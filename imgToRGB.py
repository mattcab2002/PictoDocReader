from matplotlib.image import imread
import numpy as np

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]


fp = open ("outputText/out.txt", "w")

fp2 = open("outputText/out2.txt", "w")


fp.write(to_str(imread("images/img1.png")))
fp2.write(to_str(imread("documents/doc1.png")))

fp.close()
fp2.close()