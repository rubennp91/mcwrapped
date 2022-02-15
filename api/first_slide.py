import moviepy.editor as mpy
from PIL import Image, ImageDraw, ImageFont
import os

from get_skin import get_skin_1


def generate_first_slide(config):
    """
    The first slide consists of a video background, a
    still image and four slices of text.

    The first two slices of text contain the playername.
    Playername size has to be calculated dynamically so
    it does not outsize the window.

    The third and fourth slices of text will appear
    in a crossfade effect.

    Duration of this slide is 9s.
    """

    # Read general configs
    path = config["path"]
    background = "./assets/" + config["background1"]
    playername = config["playername"]
    width = config["width"]
    height = config["height"]
    fps = config["fps"]

    # Image
    skin_pos = config["skin_pos"]

    # Text
    text1 = config["1text1"]
    text2 = config["1text2"]
    text3 = config["1text3"]

    # Text Positions
    text1_pos = config["1text1_pos"]
    text2_pos = config["1text2_pos"]
    text3_pos = config["1text3_pos"]

    # Font
    font_style_1 = ImageFont.truetype(config["font_path"],
                                      int(config["1text1_size"]))
    font_style_2 = ImageFont.truetype(config["font_path"],
                                      int(config["1text2_size"]))
    font_style_3 = ImageFont.truetype(config["font_path"],
                                      int(config["1text3_size"]))

    maxfontsize = config["maxfontsize"]

    # Get the skin into an image and create an imagevideoclip with it
    skin_path = get_skin_1(playername, path)

    skin = Image.open(skin_path)
    skin_bg = Image.new('RGBA', (360, 640), color=(255, 255, 255, 0))
    skin_bg.paste(skin, skin_pos, mask=skin)

    skin_bg_draw = ImageDraw.Draw(skin_bg)

    # Add first text
    skin_bg_draw.text(text1_pos,
                      text1,
                      font=font_style_1,
                      fill=(255, 255, 255),
                      anchor='mm')

    # Add playername, size is dynamic
    def calc_font_size(name, font_path, size=720):
        """
        Calculate what the font size for the name has to be depending
        on the lenght of the name and the size it would have.
        """
        scale = 0.7
        font_size = 1
        fnt = ImageFont.truetype(font_path, font_size)
        while fnt.getsize(name)[0] < scale*size:
            font_size += 1
            fnt = ImageFont.truetype(font_path, font_size)

        font_size -= 1

        if font_size > maxfontsize:
            font_size = maxfontsize
        return font_size

    font_size3 = calc_font_size(playername, config["font_path"], width)
    font_style_4 = ImageFont.truetype(config["font_path"],
                                      font_size3)
    vertical_offset = font_style_4.getsize(playername)[1]+55

    skin_bg_draw.text((180, vertical_offset),
                      playername,
                      font=font_style_4,
                      fill=(255, 255, 255),
                      anchor='mm')

    # Save the image for the first time
    image_1 = path + "/11.png"
    skin_bg.save(image_1)

    # Add text2
    skin_bg_draw.text(text2_pos,
                      text2,
                      font=font_style_2,
                      fill=(255, 255, 255),
                      anchor='mm')

    # Add text3
    skin_bg_draw.text(text3_pos,
                      text3,
                      font=font_style_3,
                      fill=(255, 255, 255),
                      anchor='mm')

    # Save the second image
    image_2 = path + "/12.png"
    skin_bg.save(image_2)

    # Create two clips with the two newly created images
    image1_vcp = mpy.ImageClip(img=image_1, duration=9, transparent=True)
    image2_vcp = mpy.ImageClip(img=image_2, duration=6, transparent=True)

    # Create videofileclip from bg video
    bg_vcp = mpy.VideoFileClip(background)

    # Composite the videos together
    video = mpy.CompositeVideoClip(
        [
            bg_vcp.audio_fadein(2).audio_fadeout(2),
            image1_vcp,
            image2_vcp.set_start(3).crossfadein(3),
        ],
        size=(width, height)
    )

    # Save the video
    video_path = path + "/1.mp4"
    tmp_audiofile = path + "/tmp.mp3"
    video.write_videofile(video_path, fps=fps, temp_audiofile=tmp_audiofile)

    # Delete unnecessary files
    os.remove(image_1)
    os.remove(image_2)
    os.remove(skin_path)
