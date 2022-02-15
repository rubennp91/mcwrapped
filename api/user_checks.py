import os
import json


def user_check(uuid, playername, servername):
    """
    Checks if user already created a wrapped.

    If uuid, mcname and servername are the same
    get back to user and ask if they want to
    generate it again. --> return 2

    If uuid and mcname are the same but servername
    is different, it will be generated again but with
    a different path name (uuid_2) --> return 1

    If uuid cannot be found, it will be generated
    for the first time --> return 0
    """

    working_directory = "./user_data"

    # If there is anything inside the working directory
    if os.listdir(working_directory):
        for elem in os.listdir(working_directory):
            iterable_path = os.path.join(working_directory, elem)

            # If what we found is a folder
            if os.path.isdir(iterable_path):

                # If the name of the folder is equal to the uuid
                # Open the player json to check the server name
                if elem == uuid:
                    user_json = playername + ".json"
                    user_info = {}
                    user_path = os.path.join(working_directory, elem)
                    with open(os.path.join(user_path, user_json), 'r') as fp:
                        user_info = json.load(fp)
                    check_server = user_info["servername"]

                    # If the name of the server is the same as
                    # the one saved
                    if servername == check_server:
                        return 2, 0

                    # If not, count the number of uuid folders and return it
                    else:
                        num_of_uuid_folders = len([i for i in os.listdir(working_directory) if uuid in i])
                        return 1, num_of_uuid_folders

                # The folder we found is not the one with the uuid
                else:
                    pass

            # What we found was not a folder
            else:
                pass

        # If after iterating all the folders we're still here
        # it means that a folder with the uuid was not found
        return 0, 0

    # If there is nothing in the working directory
    else:
        return 0, 0
