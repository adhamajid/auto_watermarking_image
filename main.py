from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert('RGBA')
    width, height = input_image.size

    overlay = Image.new(mode='RGBA', size= input_image.size, color=(255, 255, 255, 0))

    draw = ImageDraw.Draw(overlay)

    watermar_color_pattern = (255, 255, 255, 30)

    for i in range(0, width + height, 50):
        draw.line(xy= [(0, height - i), (i, height)], fill=watermar_color_pattern, width=5)

    font_size = "Enter your font size in int"
    font = ImageFont.truetype(font="enter your font.ttf", size=font_size)

    text_width, text_height = draw.textsize(watermark_text, font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255, 255, 255, 80)

    draw.text(xy=(x, y), text= watermark_text, fill= watermark_color_text, font= font)

    watermarked_image = Image.alpha_composite(input_image, overlay)

    watermarked_image.save(output_image_path)

input_image_path = 'input_image.jpg'
output_image_path = 'output_image.png'
watermark_text = "Your text here"

add_watermark_overlay(input_image_path, output_image_path, watermark_text)


#for multiple file in a directory

for file in os.listdir("file name"):
    add_watermark_overlay(input_image_path= f'file path', output_image_path= f'file/watermarked{file.replace("jpg", "png")}', watermark_text= watermark_text)

