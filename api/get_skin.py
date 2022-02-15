import requests
import shutil


def get_skin_1(name, player_directory):
    """
    """
    url = "https://photopass.appspot.com/3d.php?user=" + name + "&vr=-25&hr=34&hrh=-16&vrll=-27&vrrl=18&vrla=20&vrra=-19&displayHair=true&headOnly=false&format=png&ratio=20&aa=false&layers=true&ratio=10"
    file_name = player_directory + "/" + name + "_1.png"

    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print("Image successfully downloaded: ", file_name)
        return file_name
    else:
        print("Image Couldn't be retrieved")


def get_skin_2(name, player_directory):
    """
    """
    url = "http://photopass.appspot.com/3d.php?user=" + name + "&vr=0&hr=0&hrh=0&vrll=0&vrrl=0&vrla=0&vrra=0&displayHair=true&headOnly=false&format=png&ratio=20&aa=false&layers=true"
    file_name = player_directory + "/" + name + "_2.png"

    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print("Image successfully downloaded: ", file_name)
    else:
        print("Image Couldn't be retrieved")
