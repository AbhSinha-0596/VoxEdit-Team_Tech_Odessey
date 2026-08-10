from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from rembg import remove

def adjust_brightness(image, factor):
    return ImageEnhance.Brightness(image).enhance(factor)

def adjust_saturation(image, factor):
    return ImageEnhance.Color(image).enhance(factor)

def adjust_sharpness(image, factor):
    return ImageEnhance.Sharpness(image).enhance(factor)

def apply_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))

def apply_warmth(image, intensity=20):
    image = image.convert("RGB")
    r, g, b = image.split()
    r = r.point(lambda i: min(255, i + intensity))
    b = b.point(lambda i: max(0, i - intensity))
    return Image.merge("RGB", (r, g, b))

def auto_enhance_background(image):
    image = image.convert("RGB")
    output_np = remove(np.array(image))
    foreground = Image.fromarray(output_np)
    bg = apply_blur(image, radius=10)
    if foreground.mode == "RGBA":
        bg.paste(foreground, (0, 0), foreground)
        return bg
    return image

def execute_command(image, command):
    action = command.get("action")

    if action == "brightness":
        return adjust_brightness(image, command.get("factor", 1.0))

    if action == "saturation":
        return adjust_saturation(image, command.get("factor", 1.0))

    if action == "sharpness":
        return adjust_sharpness(image, command.get("factor", 1.0))

    if action == "blur":
        return apply_blur(image, command.get("radius", 2))

    if action == "warmth":
        return apply_warmth(image, command.get("intensity", 20))

    if action == "background_blur":
        return auto_enhance_background(image)

    return image