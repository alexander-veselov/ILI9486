from PIL import Image, ImageDraw, ImageFont

def create_gradient_image(size):
    gradient_image = Image.new('RGB', size)
    width, height = size
    for x in range(width):
        for y in range(height):
            normalized_x = x / width
            normalized_y = y / height
            r = int(normalized_x * 255)
            g = int(normalized_y * 255)
            b = int((1 - normalized_x) * 255)
            gradient_image.putpixel((x, y), (r, g, b))
    return gradient_image

def create_text_image(size, rotation=0, mirrored=False):
    width, height = size
    config_text = f"Size: {width}x{height}, Angle: {rotation}, Mirrored: {mirrored}"
    static_text = "---> right"
    image = Image.new('RGB', (width, height), color='white')
    main_text_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(main_text_image)
    font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), config_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), config_text, fill='black', font=font)
    if mirrored: main_text_image = main_text_image.transpose(Image.FLIP_LEFT_RIGHT)
    image.paste(main_text_image, (0, 0), main_text_image)
    arrow_font = ImageFont.load_default(20)
    static_text_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    static_draw = ImageDraw.Draw(static_text_image)
    static_bbox = static_draw.textbbox((0, 0), static_text, font=arrow_font)
    static_text_width = static_bbox[2] - static_bbox[0]
    static_text_x = (width - static_text_width) // 2
    static_text_y = text_y + text_height + 10
    static_draw.text((static_text_x, static_text_y), static_text, fill='black', font=arrow_font)
    image.paste(static_text_image, (0, 0), static_text_image)
    return image