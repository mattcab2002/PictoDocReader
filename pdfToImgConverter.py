import os
import shutil
from pdf2image import convert_from_path


def convert_pdf_to_image(path):
    images = convert_from_path(path)
    for index, image in enumerate(images):
        image.save(f'convertedPages/converted_page{index + 1}.png')


def main():
    shutil.rmtree(f'convertedPages/')
    os.makedirs(f'convertedPages/')  # create new instance of pages dir
    docPath = os.path.join('documents/', os.listdir('documents/')[0])
    if '.pdf' in docPath:
        convert_pdf_to_image(docPath)
    elif '.png' in docPath:
        shutil.copyfile(docPath, os.path.join(
            'convertedPages/', os.listdir('documents/')[0]))


if __name__ == "__main__":
    main()
