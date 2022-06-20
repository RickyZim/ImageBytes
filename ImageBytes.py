from io import BytesIO
from PIL import Image
from easy_pil import Editor
from requests import get


class ImageBytes():
    def image_to_bytes(path:str):
        try:
            img = Editor(path)
            return img.image_bytes
        except ValueError as erro:
            return erro
    def bytes_to_image(bytes, save = True, show = True):
        try:
            img = Image.open(BytesIO(bytes.read()))
            if save == True:
                img.save("Final.png")
            if show == True:
                img.show()
            else:
                return img.getdata
        except ValueError as erro:
            return erro
    def url_to_bytes(url:str):
        try:
            getimg = get(url)
            byte = BytesIO(getimg.content)
            return byte
        except ValueError as erro:
            return erro