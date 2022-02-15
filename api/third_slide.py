from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import os

from get_readable_name import get_readable_name
from get_icons import get_icon


def generate_third_slide(config):
    """
    The third slide shows the most mined blocks to the player.
    It consists of a video background, and four separate images
    showcasing the stats, as well as three images of the
    most mined blocks shown below.

    Duration of slide is 20 s.
    """

    # Read general configs
    path = config["path"]
    width = config["width"]
    height = config["height"]
    background = "./assets/" + config["background3"]
    fps = config["fps"]
    font_path = config["font_path"]

    # Text
    text1 = config["3text1"]
    text2 = config["3text2"]
    text3 = config["3text3"]
    text4 = config["3text4"]

    # Text Positions
    text1_pos = config["3text1_pos"]
    text2_pos = config["3text2_pos"]
    text3_pos = config["3text3_pos"]
    text4_pos = config["3text4_pos"]

    # Font
    font_style_1 = ImageFont.truetype(font_path,
                                      int(config["3text1_size"]))
    font_style_2 = ImageFont.truetype(font_path,
                                      int(config["3text2_size"]))
    font_style_3 = ImageFont.truetype(font_path,
                                      int(config["3text3_size"]))
    font_style_4 = ImageFont.truetype(font_path,
                                      int(config["3text4_size"]))
    
    # Block icons
    block1 = config["1most_block_icon"]
    block2 = config["2most_block_icon"]
    block3 = config["3most_block_icon"]
    block1_pos = config["1most_block_pos"]
    block2_pos = config["2most_block_pos"]
    block3_pos = config["3most_block_pos"]

    # Create Image to put text into
    slide3_image = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    slide3_image_text = ImageDraw.Draw(slide3_image)

    # Add text to image, save in between
    slide3_image_text.text(text1_pos,
                           text1,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_1 = path + "/31.png"
    slide3_image.save(image_1)

    slide3_image_text.text(text2_pos,
                           text2,
                           font=font_style_2,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_2 = path + "/32.png"
    slide3_image.save(image_2)

    slide3_image_text.text(text3_pos,
                           text3,
                           font=font_style_3,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_3 = path + "/33.png"
    slide3_image.save(image_3)

    slide3_image_text.text(text4_pos,
                           text4,
                           font=font_style_4,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_4 = path + "/34.png"
    slide3_image.save(image_4)

    # Add icons
    block1_image = Image.open(block1)
    block2_image = Image.open(block2)
    block3_image = Image.open(block3)

    block1_image = block1_image.resize((32, 32))
    block2_image = block2_image.resize((32, 32))
    block3_image = block3_image.resize((32, 32))

    slide3_image.paste(block1_image, block1_pos, mask=block1_image)
    slide3_image.paste(block2_image, block2_pos, mask=block2_image)
    slide3_image.paste(block3_image, block3_pos, mask=block3_image)

    image_5 = path + "/35.png"
    slide3_image.save(image_5)

    # Convert images to video
    image_1_vcp = mpy.ImageClip(img=image_1, duration=22, transparent=True)
    image_2_vcp = mpy.ImageClip(img=image_2, duration=16, transparent=True)
    image_3_vcp = mpy.ImageClip(img=image_3, duration=13, transparent=True)
    image_4_vcp = mpy.ImageClip(img=image_4, duration=10, transparent=True)
    image_5_vcp = mpy.ImageClip(img=image_5, duration=7, transparent=True)

    # Load background
    bg_vcp = mpy.VideoFileClip(background)

    # Create videofileclip
    video = mpy.CompositeVideoClip(
        [
            bg_vcp.audio_fadein(2).audio_fadeout(2),
            image_1_vcp,
            image_2_vcp.set_start(6).crossfadein(3),
            image_3_vcp.set_start(9).crossfadein(3),
            image_4_vcp.set_start(12).crossfadein(3),
            image_5_vcp.set_start(15).crossfadein(3),
        ],
        size=(width, height)
    )

    # Save the video
    video_path = path + "/3.mp4"
    tmp_audiofile = path + "/1tmp.mp3"
    video.write_videofile(video_path, fps=fps, temp_audiofile=tmp_audiofile)

    # Remove unnecessary files
    os.remove(image_1)
    os.remove(image_2)
    os.remove(image_3)
    os.remove(image_4)
    os.remove(image_5)
