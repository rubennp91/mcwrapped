from flask import Flask, request
from werkzeug.utils import secure_filename
import redis
from rq import Queue
from create_folder import create_folder
from generate_json_with_stats import generate_json_with_stats
from minecraft_wrapped import minecraft_wrapped
from write_log import write_log


app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)

default_values = "./default_values.json"


@app.route('/api/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['stats']
        playername = request.form['playername']
        servername = request.form['servername']
        email = request.form['email']
        mc_uuid = secure_filename(f.filename).strip('.json')
        url_uuid = create_folder(f)

        try:
            config_file = generate_json_with_stats(playername,
                                                   mc_uuid,
                                                   servername,
                                                   email,
                                                   url_uuid,
                                                   default_values)
        except Exception:
            return "Error 1"

        # This part to be queued
        try:
            result = q.enqueue(minecraft_wrapped, config_file)
            q_len = len(q)
            to_log = f"Queued {playername}, {servername} at position {q_len} with id {url_uuid}"
            write_log(to_log)
            return "Success"

        except Exception:
            return "Error 2"


@app.route('/api/getid', methods=['GET'])
def getid():
    folder_id = request.args["ID"]
    json_path = '../build/page/' + folder_id + "/" + folder_id + ".json"
    slides = {}
    try:
        with open(json_path) as fp:
            slides = fp.read()
        return slides
    except Exception:
        return "Error 2"
