from operator import le, length_hint
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import os

def generate_fifth_slide(config):
    """
    The fifth slide shows misc information about the player.
    It consists of four images.

    Duration of slide is 20 s.
    """

    # Read general configs
    path = config["path"]
    width = config["width"]
    height = config["height"]
    background = "./assets/" + config["background5"]
    fps = config["fps"]
    font_path = config["font_path"]

    # Text
    text1 = config["5text1"]
    text2 = config["5text2"]
    text3 = config["5text3"]
    text4 = config["5text4"]
    text5 = config["5text5"]

    # Text Positions
    text1_pos = config["5text1_pos"]
    text2_pos = config["5text2_pos"]
    text3_pos = config["5text3_pos"]
    text4_pos = config["5text4_pos"]
    text5_pos = config["5text5_pos"]

    # Font
    font_style_1 = ImageFont.truetype(font_path,
                                      int(config["5text1_size"]))
    font_style_2 = ImageFont.truetype(font_path,
                                      int(config["5text2_size"]))
    font_style_3 = ImageFont.truetype(font_path,
                                      int(config["5text3_size"]))
    font_style_4 = ImageFont.truetype(font_path,
                                      int(config["5text4_size"]))
    font_style_5 = ImageFont.truetype(font_path,
                                      int(config["5text5_size"]))

    # Create Image to put text into
    slide5_image = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    slide5_image_text = ImageDraw.Draw(slide5_image)

    # Add text to image, save in between
    slide5_image_text.text(text1_pos,
                           text1,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_1 = path + "/51.png"
    slide5_image.save(image_1)

    slide5_image_text.text(text2_pos,
                           text2,
                           font=font_style_2,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_2 = path + "/52.png"
    slide5_image.save(image_2)

    slide5_image_text.text(text3_pos,
                           text3,
                           font=font_style_3,
                           fill=(255, 255, 255),
                           anchor='mm')

    image_3 = path + "/53.png"
    slide5_image.save(image_3)

    slide5_image_text.text(text4_pos,
                           text4,
                           font=font_style_4,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_4 = path + "/54.png"
    slide5_image.save(image_4)

    slide5_image_text.text(text5_pos,
                           text5,
                           font=font_style_5,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_5 = path + "/55.png"
    slide5_image.save(image_5)


    # Convert images to video
    image_1_vcp = mpy.ImageClip(img=image_1, duration=20, transparent=True)
    image_2_vcp = mpy.ImageClip(img=image_2, duration=15, transparent=True)
    image_3_vcp = mpy.ImageClip(img=image_3, duration=12, transparent=True)
    image_4_vcp = mpy.ImageClip(img=image_4, duration=9, transparent=True)
    image_5_vcp = mpy.ImageClip(img=image_5, duration=6, transparent=True)

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
            image_5_vcp.set_start(14).crossfadein(3),
        ],
        size=(width, height)
    )

    # Save the video
    video_path = path + "/5.mp4"
    tmp_audiofile = path + "/1tmp.mp3"
    video.write_videofile(video_path, fps=fps, temp_audiofile=tmp_audiofile)

    # Remove unnecessary files
    os.remove(image_1)
    os.remove(image_2)
    os.remove(image_3)
    os.remove(image_4)
    os.remove(image_5)
