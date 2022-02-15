import json


def get_stats_from_json(json_file):
    """
    Read the JSON stats file and return
    the stats included in the file.
    """
    dict = {}
    with open(json_file, 'r') as f:
        dict = json.load(f)
    dict = dict['stats']
    return dict


def get_top(json_path, interest, num=1):
    """
    Return a list of the top anything
    by interest. Returns a list of len num.
    """
    stats = get_stats_from_json(json_path)
    try:
        list_of_interest = \
            [[key, stats[interest][key]] for key in stats[interest]]
    except Exception:
        return None

    # Now search for the top 3 values
    list_of_interest.sort(key=lambda x: x[1], reverse=True)

    return list_of_interest[:num]


def get_custom(json_path, argument):
    """
    Get the custom value of the custom stats.
    """
    stats = get_stats_from_json(json_path)
    try:
        return stats['minecraft:custom'][argument]
    except Exception:
        return None
