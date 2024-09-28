from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert('RGBA')
    width, height = input_image.size

    overlay = Image.new(mode='RGBA', size=input_image.size, color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    watermark_color_pattern = (255, 255, 255, 30)

    for i in range(0, width + height, 50):
        draw.line(xy=[(0, height - i), (i, height)], fill=watermark_color_pattern, width=5)

    font_size = 500  # Pastikan ini adalah integer
    font_path = "AnandaBlackPersonalUseRegular-rg9Rx.ttf"  # Pastikan path font ini benar
    font = ImageFont.truetype(font=font_path, size=font_size)

    # Menghitung ukuran teks
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255, 255, 255, 80)
    draw.text(xy=(x, y), text=watermark_text, fill=watermark_color_text, font=font)

    watermarked_image = Image.alpha_composite(input_image, overlay)
    watermarked_image.save(output_image_path)

# Ganti dengan path direktori yang sesuai
input_image_path = r"D:\project\image_watermarker\input_image.jpg"  # Ganti dengan path yang sesuai
output_image_path = r"D:\project\image_watermarker\output_image.png"  # Ganti dengan path yang sesuai
watermark_text = "asyah_majid"

add_watermark_overlay(input_image_path, output_image_path, watermark_text)

# Proses untuk semua file dalam direktori
input_directory = r"D:\project\image_watermarker\input"
output_directory = r"D:\project\image_watermarker\output"
os.makedirs(output_directory, exist_ok=True)

for file in os.listdir(input_directory):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_image_path = os.path.join(input_directory, file)
        output_image_path = os.path.join(output_directory, f'watermarked_{file.replace(".jpg", ".png").replace(".jpeg", ".png")}')
        add_watermark_overlay(input_image_path, output_image_path, watermark_text)
