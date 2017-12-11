import io
import sys
import argparse


def ladi_ocr():
    """reads the image file from the provided path in terminal
        extract and prints spanish language text in the image using Google Vision api"""
    # we need to have vision api activated
    from google.cloud import vision # importing google cloud vision api  
    vision_client = vision.Client() # calling  client to make vision api request
    for image_path in sys.argv[1:]: # iteration over all the image path provided in the terminali
        try:
            with io.open(image_path, 'rb') as image_file_path:
                image = image_file_path.read()
                image_content = vision_client.image(content = image) # using the vision client to read the image
                encoding = sys.stdout.encoding or 'utf-8'
                print(image_content.detect_full_text(language_hints = ['es']).text).encode(encoding)
                print('\n')
        except KeyboardInterrupt:
            print('You cancelled the operation; bbye.')
        except ImportError:
            print("No module found, make sure you have required modules installed")
        except IOError:
            print("An error occurred trying to read the file.")
        except:
            print("something seems Strange; there is some error")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You need to provide more arguments' + '\n' + " add [*imagePath] as your argument" +
        "\n" " or --help for more help")
    elif sys.argv[1] == '--help':
        print('Input: Path for one or more images'+ '\n' + "output: extract and prints the text in the images using google vision api")
    elif sys.argv[1] =="--h":
        print('Input: Path for one or more images'+ '\n' + "output: extract and prints the text in the images using google-vision api")
    elif sys.argv[1] == '--version':
        print(" ladi_vision.py 0.1")

    else:
        ladi_ocr()



