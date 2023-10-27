import os
from random import randint


def get_filename_ext(filepath):
    """ return file name & ext """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_product_image_path(instance, filepath) -> str:
    """ return product image path """
    name, ext = get_filename_ext(filepath)
    # generate random number
    random_number = randint(100, 999999)
    final_name = f"{random_number}{ext}"
    return f"products/thumbnails/{final_name}"


def generate_order_id() -> int:
    """
    generate random ID for Order model.
    """
    number = randint(1000000, 9999999)
    return number
