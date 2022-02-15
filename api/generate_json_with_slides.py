import os
import json

def generate_json_with_slides(config):
    """
    Generate the JSON that will be used by
    react-insta-stories to showcase the
    stories.

    The JSON will contain the paths to the
    videos.
    """
    path = config["path"]
    url_uuid = config["url_uuid"]

    vid_dict_list = []

    # Search for all mp4 elements in provided folder and save as a list
    for elem in os.listdir(path):
        if elem.endswith('.mp4'):
            vid_dict_list.append(elem)

    # Order that list:
    vid_dict_list.sort()

    full_vid_dict_list = []
    # Attach the rest of the url to each elem
    for elem in vid_dict_list:
        vid_path = "http://mcwrapped.online/page/" + url_uuid + "/" + elem
        full_vid_dict_list.append(vid_path)

    # Append all elements as dictionaries to a list
    vid_list = []
    for elem in full_vid_dict_list:
        new_dict = {}
        new_dict["url"] = elem
        new_dict["type"] = "video"
        vid_list.append(new_dict)

    new_dict = {}
    new_dict["url"] = "http://mcwrapped.online/page/6.mp4"
    new_dict["type"] = "video"
    vid_list.append(new_dict)

    json_slides = path + "/" + url_uuid + '.json'

    with open(json_slides, 'w') as fp:
        json.dump(vid_list, fp)

    return json_slides