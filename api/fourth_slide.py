from operator import le, length_hint
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import os

def generate_fourth_slide(config):
    """
    The fourth slide shows the kill game to the player.
    It consists of a video background and 6 separate images
    showcasing the stats.

    Duration of slide is 20s
    """

    # Read general configs
    path = config["path"]
    width = config["width"]
    height = config["height"]
    background = "./assets/" + config["background4"]
    fps = config["fps"]
    font_path = config["font_path"]

    # Text
    text1 = config["4text1"]
    text2 = config["4text2"]
    text3 = config["4text3"]
    text4 = config["4text4"]
    text5 = config["4text5"]
    text6 = config["4text6"]

    # Text Positions
    text1_pos = config["4text1_pos"]
    text2_pos = config["4text2_pos"]
    text3_pos = config["4text3_pos"]
    text4_pos = config["4text4_pos"]
    text5_pos = config["4text5_pos"]
    text6_pos = config["4text6_pos"]

    # Font
    font_style_1 = ImageFont.truetype(font_path,
                                      int(config["4text1_size"]))
    font_style_2 = ImageFont.truetype(font_path,
                                      int(config["4text2_size"]))
    font_style_3 = ImageFont.truetype(font_path,
                                      int(config["4text3_size"]))
    font_style_4 = ImageFont.truetype(font_path,
                                      int(config["4text4_size"]))
    font_style_5 = ImageFont.truetype(font_path,
                                      int(config["4text5_size"]))
    font_style_6 = ImageFont.truetype(font_path,
                                      int(config["4text6_size"]))

    # Create Image to put text into
    slide4_image = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    slide4_image_text = ImageDraw.Draw(slide4_image)

    # Add text to image, save in between
    slide4_image_text.text(text1_pos,
                           text1,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_1 = path + "/41.png"
    slide4_image.save(image_1)

    slide4_image_text.text(text2_pos,
                           text2,
                           font=font_style_2,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_2 = path + "/42.png"
    slide4_image.save(image_2)

    slide4_image_text.text(text3_pos,
                           text3,
                           font=font_style_3,
                           fill=(255, 255, 255),
                           anchor='mm')

    slide4_image_text.text(text4_pos,
                           text4,
                           font=font_style_4,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_3 = path + "/43.png"
    slide4_image.save(image_3)

    slide4_image_text.text(text5_pos,
                           text5,
                           font=font_style_5,
                           fill=(255, 255, 255),
                           anchor='mm')

    slide4_image_text.text(text6_pos,
                           text6,
                           font=font_style_6,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_4 = path + "/44.png"
    slide4_image.save(image_4)

    # Convert images to video
    image_1_vcp = mpy.ImageClip(img=image_1, duration=20, transparent=True)
    image_2_vcp = mpy.ImageClip(img=image_2, duration=15, transparent=True)
    image_3_vcp = mpy.ImageClip(img=image_3, duration=12, transparent=True)
    image_4_vcp = mpy.ImageClip(img=image_4, duration=9, transparent=True)

    # Load background
    bg_vcp = mpy.VideoFileClip(background)

    # Create videofileclip
    video = mpy.CompositeVideoClip(
        [
            bg_vcp.audio_fadein(2).audio_fadeout(2),
            image_1_vcp,
            image_2_vcp.set_start(5).crossfadein(3),
            image_3_vcp.set_start(8).crossfadein(3),
            image_4_vcp.set_start(11).crossfadein(3),
        ],
        size=(width, height)
    )

    # Save the video
    video_path = path + "/4.mp4"
    tmp_audiofile = path + "/1tmp.mp3"
    video.write_videofile(video_path, fps=fps, temp_audiofile=tmp_audiofile)

    # Remove unnecessary files
    os.remove(image_1)
    os.remove(image_2)
    os.remove(image_3)
    os.remove(image_4)
