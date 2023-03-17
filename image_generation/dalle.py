from pypdf import PdfReader
import os
import openai
import json
from PIL import Image
from io import BytesIO
import urllib

openai.api_key = ""

'''

Get byte stream of image

Input:
- img_path (str): path to image to generate
- image_size (tuple_int): image size

Output:

- byte_array(byte stream): output byte stream of image file

'''

def image_to_byte_stream(img_path, image_size):

    image = Image.open(img_path)
    image = image.resize(image_size)

    # Convert the image to a BytesIO object
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()
    return byte_array

'''

Get variation generation of image

Input:

- img_stream(byte stream): output byte stream of image file

- img_out_path (str): output path of image


'''

def generate_variation(img_stream, img_out_path):
    # Generate augmentation
    response = openai.Image.create_variation(
      image= img_stream,
      n=1,
      size="512x512"
    )

    image_url = response['data'][0]['url']

    urllib.request.urlretrieve(image_url, img_out_path)


# Quick using
if __name__ == "__main__":

    img_path = "test.png"
    path_out = "out.png"

    img_byte = image_to_byte_stream(img_path, 256)
    generate_variation(img_byte, path_out)