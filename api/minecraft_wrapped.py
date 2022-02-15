import json
from first_slide import generate_first_slide
from second_slide import generate_second_slide
from third_slide import generate_third_slide
from fourth_slide import generate_fourth_slide
from fifth_slide import generate_fifth_slide
from generate_json_with_slides import generate_json_with_slides
from send_email import send_email

def minecraft_wrapped(config_file):

    with open(config_file, 'r') as fp:
        config = json.load(fp)

    generate_first_slide(config)
    generate_second_slide(config)
    generate_third_slide(config)
    generate_fourth_slide(config)
    generate_fifth_slide(config)
    json_slides = generate_json_with_slides(config)
    send_email(config, json_slides)
