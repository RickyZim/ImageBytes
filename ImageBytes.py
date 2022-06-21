from requests import get
from easy_pil import Editor
from PIL import Image
from io import BytesIO

class ImageBytes():
    def url_to_bytes(url:str):
        base = get(url)
        bytes = BytesIO(base.content)
        return bytes
    def bytes_to_image(bytes):
        b = BytesIO(bytes.read())
        img = Editor(b)
        return img.image_bytes
    def image_to_bytes(path:str):
        img = Editor(path)
        return img.image_bytes
