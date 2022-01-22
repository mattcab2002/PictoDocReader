import os
import shutil

from pdf2image import convert_from_path


def convert_pdf_to_image(path):
    images = convert_from_path(path)
    for index, image in enumerate(images):
        image.save(f'convertedPages/converted_page{index + 1}.png')


if __name__ == '__main__':
    folder = r'convertedPages'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    convert_pdf_to_image('documents/textbook1.pdf')