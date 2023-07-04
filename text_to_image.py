from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFilter
import textwrap
import os


def text_to_image(episode, bg_image, text_1, text_2):
    # Define the size of the screen (in pixels)
    screen_size = (1284, 2778)

    # Create a new image with the size of screen
    image = Image.new("RGB", screen_size)

    # Load the background image
    background_image = Image.open(bg_image)

    # Resize the background image to fit screen
    background_image = background_image.resize(screen_size)

    # Apply blur effect to the background image
    blurred_background = background_image.filter(ImageFilter.GaussianBlur(radius=10))

    # Paste the blurred background onto the new image
    image.paste(blurred_background, (0, 0))

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text content and font
    #text_content_1 = text_1
    text_content_2 = text_2
    font = ImageFont.truetype("BRLNSDB.TTF", 100)

    # Calculate the maximum width and height for the text
    max_text_width = int(image.width * 0.8)
    max_text_height = int(image.height * 0.8)

    # Wrap the text to fit within the maximum width
    #wrapped_text_1 = textwrap.wrap(text_content_1, width=25)
    wrapped_text_2 = textwrap.wrap(text_content_2, width=25)

    # Calculate the position to center the text
    text_position = ((image.width - max_text_width) // 2, (image.height - max_text_height) // 2)

    # Draw Title Text
    text_position_1 = (150, 270)
    draw.text(text_position_1,text_1, font=font, fill=(255, 255, 255))

    # Draw the wrapped text on the image
    text_position_2 = (106,560)
    for line in wrapped_text_2:
        text_position_2 = (text_position_2[0], text_position_2[1]+100)
        draw.text(text_position_2, line, font=font, fill=(255, 255, 255))

    # Save the final image
    #os.mkdir(f"./Episodes/Spells/{episode}/{text_1}")
    image.save(f"./Episodes/Spells/{episode}/{text_1}/{text_1}.png")

def intro_image(ep_number, bg_image, text_1, text_2):
    # Define the size of the screen (in pixels)
    screen_size = (1284, 2778)

    # Create a new image with the size of screen
    image = Image.new("RGB", screen_size)

    # Load the background image
    background_image = Image.open(bg_image)

    # Resize the background image to fit screen
    background_image = background_image.resize(screen_size)

    # Apply blur effect to the background image
    blurred_background = background_image.filter(ImageFilter.GaussianBlur(radius=10))

    # Paste the blurred background onto the new image
    image.paste(blurred_background, (0, 0))

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text content and font
    text_content_1 = text_1
    text_content_2 = text_2
    font = ImageFont.truetype("BRLNSDB.TTF", 100)

    # Calculate the maximum width and height for the text
    max_text_width = int(image.width * 0.8)
    max_text_height = int(image.height * 0.8)

    # Wrap the text to fit within the maximum width
    wrapped_text_1 = textwrap.wrap(text_content_1, width=25)
    wrapped_text_2 = textwrap.wrap(text_content_2, width=25)

    # Calculate the position to center the text
    text_position = ((image.width - max_text_width) // 2, (image.height - max_text_height) // 2)

    # Draw Title Text
    text_position_1 = (150, 270)
    for line in wrapped_text_1:
        text_position_1 = (text_position_1[0], text_position_1[1]+100)
        draw.text(text_position_1, line, font=font, fill=(255, 255, 255))

    # Draw the wrapped text on the image
    text_position_2 = (106,760)
    for line in wrapped_text_2:
        text_position_2 = (text_position_2[0], text_position_2[1]+100)
        draw.text(text_position_2, line, font=font, fill=(255, 255, 255))

    # Save the final image
    #os.mkdir(f"./images/intros/{ep_number}")
    image.save(f"./Episodes/Spells/{ep_number}/intro/{ep_number}.png")
