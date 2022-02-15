from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mpy
import os


def generate_sixth_slide():
    text1 = "All in all "
    text2 = "it was a good play!"
    text3 = "Share your results"
    text4 = "with your friends"

    font_style_1 = ImageFont.truetype('./assets/fonts/Minecraft.ttf', 36)

    slide2_image = Image.new('RGBA', (360, 640), color=(255, 255, 255, 0))
    slide2_image_text = ImageDraw.Draw(slide2_image)

    slide2_image_text.text([180, 240],
                           text1,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')

    slide2_image_text.text([180, 280],
                           text2,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')
    
    slide2_image_text.text([180, 400],
                           text3,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')

    slide2_image_text.text([180, 440],
                           text4,
                           font=font_style_1,
                           fill=(255, 255, 255),
                           anchor='mm')
    
    image_1 = "./6.png"
    slide2_image.save(image_1)

    image_1_vcp = mpy.ImageClip(img=image_1, duration=10, transparent=True)
    bg_vcp = mpy.VideoFileClip("C:/Users/ruben/Desktop/Minecraft_Wrapped/home/api/assets/background6.mp4")

    video = mpy.CompositeVideoClip(
        [
            bg_vcp.audio_fadein(2).audio_fadeout(2),
            image_1_vcp
        ],
        size=(360, 640)
    )

    video_path = "./6.mp4"
    video.write_videofile(video_path, fps=24)

generate_sixth_slide()