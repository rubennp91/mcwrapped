import os


def get_icon(id, type):
    """
    """

    block_icons_folder = "./assets/block"
    item_icons_folder = "./assets/item"

    if 'minecraft:' in id:
        id = id.split('minecraft:')[1]

    if type == 'block':
        folder = block_icons_folder
    elif type == 'item':
        folder = item_icons_folder

    for i in os.listdir(folder):
        name = i.split('.png')[0]
        if '_side' in name:
            name = name.split('_side')[0]
        if '_large' in name:
            name = name.split('_large')[0]
        if '_stage' in name:
            name = name.split('_stage')[0]
        if name == id:
            filename = i

    return "./assets/" + type + "/" + filename
