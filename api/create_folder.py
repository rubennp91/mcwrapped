import os
import json
import uuid
from user_checks import user_check


def create_folder(statsfile):
    """
    Generate a unique ID for the session, create
    a folder where the files will be saved and
    return the ID value.
    """

    # Load the existing ID JSON
    uuid_json = '/home/mcwrapped/build/page/ids.json'
    with open(uuid_json, 'r') as fp:
        id_list = json.load(fp)

    is_equal = True
    new_uuid = str(uuid.uuid4())[:8]

    while is_equal:
        if new_uuid in id_list:
            new_uuid = str(uuid.uuid4())[8:]
        else:
            is_equal = False

    # Update the existing ID JSON
    id_list[new_uuid] = new_uuid
    with open(uuid_json, 'w') as fp:
        json.dump(id_list, fp)

    # Create the folder
    new_uuid_path = os.path.join('/home/mcwrapped/build/page/', new_uuid)
    os.mkdir(new_uuid_path)

    # Save the JSON inside the folder
    json_path = os.path.join(new_uuid_path, statsfile.filename)
    statsfile.save(json_path)

    # Return the ID value
    return new_uuid
