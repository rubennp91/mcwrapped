from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import os


def generate_second_slide(config):
    """
    The second slide consists of a video background, and
    four separate text images showcasing stats.

    The first text is still, appearing when the video
    loads. The other three texts appear crossfading in.

    Duration of slide is 22 s.
    """

    # Read general configs
    path = config["path"]
    width = config["width"]
    height = config["height"]
    background = "./assets/" + config["background2"]
    fps = config["fps"]
    maxfontsize = config["maxfontsize"]
    font_path = config["font_path"]

    # Text
    text1 = config["2text1"]
    text2 = config["2text2"]
    text3 = config["2text3"]
    text4 = config["2text4"]
    text5 = config["2text5"]
    text6 = config["2text6"]

    # Text Positions
    text1_pos = config["2text1_pos"]
    text3_pos = config["2text3_pos"]
    text4_pos = config["2text4_pos"]
    text5_pos = config["2text5_pos"]
    text6_pos = config["2text6_pos"]

    # Font
    font_style_1 = ImageFont.truetype(font_path,
                                      int(config["2text1_size"]))
    font_style_3 = ImageFont.truetype(font_path,
                                      int(config["2text3_size"]))
    font_style_4 = ImageFont.truetype(font_path,
                                      int(config["2text4_size"]))
    font_style_5 = ImageFont.truetype(font_path,
                                      int(config["2text5_size"]))
    font_style_6 = ImageFont.truetype(font_path,
                                      int(config["2text6_size"]))

    # Create Image to put text into
    slide2_image = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    slide2_image_text = ImageDraw.Draw(slide2_image)

    # Calculate size of text 2 (text with server name)
    def calc_font_size(name, font_path, size=720):
        """
        Calculate what the font size for the name has to be depending
        on the lenght of the name and the size it would have.
        """
        scale = 0.9
        font_size = 1
        fnt = ImageFont.truetype(font_path, font_size)
        while fnt.getsize(name)[0] < scale*size:
            font_size += 1
            fnt = ImageFont.truetype(font_path, font_size)

        font_size -= 1

        if font_size > maxfontsize:
            font_size = maxfontsize
        return font_size

    font_size2 = calc_font_size(text2, font_path, width)
    font_style_2 = ImageFont.truetype(font_path, font_size2)
    vertical_offset = font_style_2.getsize(text2)[1]+70

    # Add text to image, save in between
    slide2_image_text.text(text1_pos,
                           text1,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')

    slide2_image_text.text([180, vertical_offset],
                           text2,
                           font=font_style_2,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_1 = path + "/21.png"
    slide2_image.save(image_1)

    slide2_image_text.text(text3_pos,
                           text3,
                           font=font_style_3,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_2 = path + "/22.png"
    slide2_image.save(image_2)

    slide2_image_text.text(text4_pos,
                           text4,
                           font=font_style_4,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_3 = path + "/23.png"
    slide2_image.save(image_3)

    slide2_image_text.text(text5_pos,
                           text5,
                           font=font_style_5,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_4 = path + "/24.png"
    slide2_image.save(image_4)

    slide2_image_text.text(text6_pos,
                           text6,
                           font=font_style_6,
                           fill=(255, 255, 255),
                           anchor='mm')
    image_5 = path + "/25.png"
    slide2_image.save(image_5)

    # Create clips for the five images
    image_1_vcp = mpy.ImageClip(img=image_1, duration=22, transparent=True)
    image_2_vcp = mpy.ImageClip(img=image_2, duration=16, transparent=True)
    image_3_vcp = mpy.ImageClip(img=image_3, duration=13, transparent=True)
    image_4_vcp = mpy.ImageClip(img=image_4, duration=10, transparent=True)
    image_5_vcp = mpy.ImageClip(img=image_5, duration=7, transparent=True)

    # Load background
    # TO BE REMOVED: final bg clip should already be pre edited to duration
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
    video_path = path + "/2.mp4"
    tmp_audiofile = path + "/1tmp.mp3"
    video.write_videofile(video_path, fps=fps, temp_audiofile=tmp_audiofile)

    # Remove unnecessary files
    os.remove(image_1)
    os.remove(image_2)
    os.remove(image_3)
    os.remove(image_4)
    os.remove(image_5)
