from write_log import write_log
import configparser
import smtplib, ssl

smtp_config = configparser.ConfigParser()
smtp_config.read('smtp.ini')


def send_email(config, json_slides):
    playername = config["playername"]
    servername = config["servername"]
    receiver_email = config["email"]
    url = "http://mcwrapped.online/page/" + config["url_uuid"]

    smtp_server = smtp_config["CREDENTIALS"]["server"]
    sender_email = smtp_config["CREDENTIALS"]["sender_email"]
    password = smtp_config["CREDENTIALS"]["password"]
    port = smtp_config["CREDENTIALS"]["port"]

    write_log(f"Mail sent to {receiver_email} for {playername}, {servername} at {json_slides}")

    message = f"""\
Subject: Your MCWrapped is ready!
To: {receiver_email}
From: {sender_email}

Hi, {playername}! Your {servername} MCWrapped is ready. Check it out here:

{url}

www.mcwrapped.online"""

    print(smtp_server, sender_email, password, port, receiver_email)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
