import json
from get_stats import get_custom
from get_stats import get_top
from get_readable_name import get_readable_name
from get_icons import get_icon


def generate_json_with_stats(playername, uuid, server_name, email, url_uuid, default_values):
    """
    """

    # Load default values into player_dict
    with open(default_values, 'r') as fp:
        player_dict = json.load(fp)

    player_dict["playername"] = playername
    player_dict["url_uuid"] = url_uuid
    player_dict["path"] = '../build/page/' + player_dict["url_uuid"]
    player_dict["uuid"] = uuid
    player_dict["stats"] = player_dict["path"] + "/" + player_dict["uuid"] + ".json"
    player_dict["servername"] = server_name
    player_dict["email"] = email

    # Second slide: basics
    player_dict["2text1"] = "Let's start with some basics."
    player_dict["2text2"] = "On " + server_name + " you have..."

    # Get stats
    # Get play time or times quit
    if get_custom(player_dict["stats"], 'minecraft:play_time') is not None:
        play_time = get_custom(player_dict["stats"], 'minecraft:play_time')
        play_time = str((play_time/60)/1200).split('.')[0]
        player_dict["2text3"] = "Played for " + play_time + " hours"
    else:
        times_quit = get_custom(player_dict["stats"], 'minecraft:leave_game')
        times_quit = str(times_quit)
        player_dict["2text3"] = "Quit the game " + times_quit + " times"

    # Get walked distance
    walked_distance = get_custom(player_dict["stats"], 'minecraft:walk_one_cm')
    walked_distance = str(walked_distance/100).split('.')[0]
    player_dict["2text4"] = "Walked for " + walked_distance + " m"

    # Get sprinted distance
    sprinted_distance = get_custom(player_dict["stats"], 'minecraft:sprint_one_cm')
    sprinted_distance = str(sprinted_distance/100).split('.')[0]
    player_dict["2text5"] = "Sprinted for " + sprinted_distance + " m"

    # Get flown distance or swam distance
    if get_custom(player_dict["stats"], 'minecraft:fly_one_cm') is not None:
        flown_distance = get_custom(player_dict["stats"], 'minecraft:fly_one_cm')
        flown_distance = str(flown_distance/100).split('.')[0]
        player_dict["2text6"] = "Flown for " + flown_distance + " m"
    else:
        swam_distance = get_custom(player_dict["stats"], 'minecraft:swim_one_cm')
        swam_distance = str(swam_distance/100).split('.')[0]
        player_dict["2text6"] = "Flown for " + swam_distance + " m"

    # Third slide: blocks
    top_3 = get_top(player_dict["stats"], 'minecraft:mined', 3)
    readable_top_3 = [get_readable_name(i[0], "block") for i in top_3]

    player_dict["3text2"] = readable_top_3[0] + " " + str(top_3[0][1])
    player_dict["3text3"] = readable_top_3[1] + " " + str(top_3[1][1])
    player_dict["3text4"] = readable_top_3[2] + " " + str(top_3[2][1])

    # Icons for third slide
    player_dict["1most_block_icon"] = get_icon(top_3[0][0], "block")
    player_dict["2most_block_icon"] = get_icon(top_3[1][0], "block")
    player_dict["3most_block_icon"] = get_icon(top_3[2][0], "block")

    # Fourth slide: kill

    # Number of deaths
    n_deaths = get_custom(player_dict["stats"], "minecraft:deaths")
    player_dict["4text2"] = "You died " + str(n_deaths) + " times"

    # The mob that killed you the most
    n_deaths_by_mob = get_top(player_dict["stats"], "minecraft:killed_by")
    readable_d_by_mob = get_readable_name(n_deaths_by_mob[0][0], "ent")
    player_dict["4text3"] = "You died the most to:"
    player_dict["4text4"] = str(readable_d_by_mob)

    # Your most killed mob
    n_mob_killed = get_top(player_dict["stats"], "minecraft:killed")
    readable_mob_killed = get_readable_name(n_mob_killed[0][0], "ent")
    player_dict["4text5"] = "Your most killed mob was"
    player_dict["4text6"] = str(readable_mob_killed)

    # Fifth slide: misc

    misc = ["minecraft:pot_flower",
            "minecraft:eat_cake_slice",
            "minecraft:animals_bred",
            "minecraft:sleep_in_bed",
            "minecraft:traded_with_villager",
            "minecraft:play_noteblock",
            "minecraft:play_record",
            "minecraft:open_barrel",
            "minecraft:open_chest",
            "minecraft:fish_caught",
            "minecraft:interact_with_crafting_table",
            ]

    misc_chosen = []

    for elem in misc:
        if get_custom(player_dict["stats"], elem) is not None:
            misc_chosen.append([elem, get_custom(player_dict["stats"], elem)])

    player_dict["5text2"] = get_readable_name(misc_chosen[0][0], 'stat') + ": " +\
        str(get_custom(player_dict['stats'], misc_chosen[0][0]))
    player_dict["5text3"] = get_readable_name(misc_chosen[1][0], 'stat') + ": " +\
        str(get_custom(player_dict['stats'], misc_chosen[1][0]))
    player_dict["5text4"] = get_readable_name(misc_chosen[2][0], 'stat') + ": " +\
        str(get_custom(player_dict['stats'], misc_chosen[2][0]))
    player_dict["5text5"] = get_readable_name(misc_chosen[3][0], 'stat') + ": " +\
        str(get_custom(player_dict['stats'], misc_chosen[3][0]))

    # Save player json file
    player_json = player_dict["path"] + "/" + playername + ".json"
    with open(player_json, 'w') as fp:
        json.dump(player_dict, fp)

    return player_json
