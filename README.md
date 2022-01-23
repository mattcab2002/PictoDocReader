# PictoDocReader

A project created for the 9th edition of McGill's hackathon McHacks (2022). Created by MAAG innovations.

## Table of Contents

-   [Overview](#overview)
-   [How To Use This Project](#how-to-use-this-project)
-   [Validation Methods & Occurences](#validation-methods-and-occurences)
    -   [Validation Methods](#validation-methods)
    -   [Occurences](#occurences)
-   [Cropping](#cropping)
-   [Threading](#threading)
-   [Dash Application](#dash-application)
-   [PictoDocReader In The Future](#pictodocreacer-in-the-future)
-   [Disclaimer](#disclaimer)
-   [Credits](#credits)

## Overview

Due to COVID, many students like us have become accustomed to work on their schoolwork, projects and even hackathons remotely. This led students to use online resources at their disposal in order to facilitate their workload at home. One of the tools most used is “ctrl+f” which enables the user to quickly locate any text within a document. Thus, we came to a realisation that no such accurate method exists for images. This led to the birth of our project for this hackathon titled “PictoDocReader”.

## How To Use This Project

1. Clone the repository (i.e `git clone https://github.com/mattcab2002/PictoDocReader`)
2. Install the requirements by running `pip install -r requirements.txt` or by using your preferred package manager
3. Run any of the following commands:

| Commands                        |                                                                                                                                                                                                                 Description                                                                                                                                                                                                                 |
| ------------------------------- | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| python3 display.py              |                                                                        Creates a development server for the Dash application. Serves as an interface for users to test the search algorithims in place to detect search images. Upon upload buttons will appear which upon clicking will implicitly call python scripts to execute the proper search algroritihims.                                                                         |
| python3 pdfToImageConverter.py  |                                                                                                                                                          Converts the file found in the documents folder into a set of PNG images where each images is a page found within the PDF                                                                                                                                                          |
| python3 main.py `<int>` `<int>` | Explicitly calls the search algorithims and specifies the number of occurences to search for. For more about the search methods and occurences checkout out [Validation Methods & Occurences](#validation-methods-and-occurences). The first integer takes in either 0 or 1 and corresponds to the first occurrence or all occurrences, and second integer takes in 0,1, or 2 and corresponds to which search method the script should use. |

## Validation Methods and Occurences

### Validation Methods

| Validation Method('s) | Time Complexity (big-O-notation) \* |                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                          |
| --------------------- | :---------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| fourCorners           |                O(1)                 |                                                                                                                                            fourCorners method searches for the first occurence of the top left pixel of the image within the document. It then extends the search area of the document by the image's width and height and compares the 4 corners of both search area's to see if they're a match.                                                                                                                                            |
| linearSearch          |               O(n\*m)               |                                                                                                                                                                                                      linearSearch method checks fir the first occurence of the image within the document and then validates all the pixels of the image to find a match.                                                                                                                                                                                                      |
| DiagonalSearch        |            O(log(n\*m))             |                                                                                                                                                                                                                diagonalSearch method selectively iterates through the diagnoal of the image. Works independent of the dimensions of the image.                                                                                                                                                                                                                |
| randomSearch          |            O(log(n\*m))             |                                                                                                                                                                                                       randomSearch method selectively picks p\*\* pixels within the image and tries to match them with a set of pixels that match within the document.                                                                                                                                                                                                        |
| KMPSearch             |               O(n^2)                | The [Knuth–Morris–Pratt](https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm) search method is know for 2D string matching. It is best used when there are several occurences of a character or substring. We have modified this search method in order to find a subset of pixels within each row of the search document. This search method rules out mismatched substrings as it traverses the string. Although the worst case has a search time this of O(n^2) the algorithim proves to be consist and is why we have incorporated in the project. |

`*` where n refers to the height of the image and m refers to it's width
`**`p is a specified number of pixels to search for
`***` all of these time complexities were calculated using Master's theorem

### Occurences

| Occurences         |                                                                         Description                                                                         |
| ------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------: |
| singleOccurence    | Method searched for a single occurence of an image match within the document and then exits the script. Will return the image outlined within the document. |
| multipleOccurences |                 Method to search for all occurences of the image within the document. Will return each image outlined within the document.                  |

## Cropping

Images like the following:

<img src="https://i.imgur.com/9IOe3gr.png" alt="Stadium" />

tend to have uncessary white space that can heavily slow down validation methods. This will usually come in the form of a background color of the page itself. In order to avoid this obstacle we implemented a method that will crop the image down to it's "unique proportion". This will allow the validation methods to validate the content that really "matters". Once a match is found the image is then sized back to it's original dimensions.

## Threading

We incorporated [threading](https://www.ibm.com/docs/en/aix/7.1?topic=concepts-multithreaded-programming) into our project to speed up processes relating to validating the images. Instead of running the program page by page threading allows us to validate images within each page concurrently. By assigning a thread for every page within the document we reduce the time it takes to validate the whole document.

## Dash Application

The dash application presents a user interface to allow users to upload a pdf and the appropriate image to search for within that document. The dash application implicitly calls the validation methods to run based of the following buttons presented to the user:

<div align="center">
	<img src="https://i.imgur.com/w9snOV2.png"  alt="Dash App Validation Buttons" />
</div>

and then subsequent buttons are presented to the user for the number of occurences they want to search for.

<div align="center">
	<img src="https://i.imgur.com/RLPVhVO.png"  alt="Dash App Number of Occurences Buttons" />
</div>

Once wither buttons have registered a click the dash application runs the appropriate scripts and will return the image plotted onto the document.

## PictoDocReader In The Future

For the future of PictoDocReader we plan to implement an AI model that will be able to differentiate images based off their content rather than there exact RGB values. Rather than trying to find images within documents that match exactly the image we are looking for (that is each pixel are the exact same RGB values). The model would verify if a pixel in the document is found within a range of pixels for the pixel in the image. Take the following cube as an example:

<img src="https://upload.wikimedia.org/wikipedia/commons/a/af/RGB_color_solid_cube.png" alt="RGB Cube" width="400" height="300" />

A pixel in the image can be a subset of the face of red-green pixels found on the cube. A different but same (content-wise) pixel on the document can be found on the same face but is a slightly different shade. Although the content of the 2 pixels is the same their RGB values do not match and thus the current program would not consider them to be a match. Implementing this AI model would allow the program to still detect images taken via screenshot, with different color profiles, with worse or better resolutions, or images that have different oppacities.

Here's an example of a situation where this solution would seem fit:

<div align="center">
	<img src="https://i.imgur.com/hmlOVFW.png" alt="Harddisk Example 1" />
	<img src="https://i.imgur.com/rZH1e7Q.png" alt="Harddisk Example 1" />
</div>

## Disclaimer

The runtime of the program is greatly affected based off the number of CPU cores contained by the machine running it because of the use of threading within the project. In an ideal world instead of threading we would use [parallel processing](#https://searchdatacenter.techtarget.com/definition/parallel-processing).

## Credits

MAAG innovations, a group comprised [Abhijeet Praveen](https://github.com/abhijeetpraveen), [Athavan Thambimuthu](https://github.com/Arty2001), [Gianluca Piccirillo](https://github.com/GianlucaP106), and [Matthew Cabral](https://github.com/mattcab2002).

The following [Dash Uploader Component](#https://github.com/np-8/dash-uploader) helped in the development of the Dash application immensely and we would like to thank the contributors.
