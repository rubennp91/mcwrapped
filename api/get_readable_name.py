import json


def get_readable_name(id, type):
    """
    """
    block_json = "./assets/blocknames.json"
    item_json = "./assets/itemnames.json"
    entities_json = "./assets/entities.json"
    stats_json = "./assets/stats.json"

    if 'minecraft:' in id:
        id = id.split('minecraft:')[1]

    if type == 'block':
        json_file = block_json
    elif type == 'item':
        json_file = item_json
    elif type == 'ent':
        json_file = entities_json
    elif type == "stat":
        json_file = stats_json

    dict = {}
    with open(json_file, 'r') as f:
        dict = json.load(f)
    return dict[id]
