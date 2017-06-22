from flask import Flask, request, url_for, send_from_directory, render_template
from gevent.wsgi import WSGIServer
from werkzeug.utils import secure_filename
import shutil
import os
import time

__name__ = "clip-server"
__version__ = 1.0

CLIP_PATH = "/tmp/clip"
TIMEOUT = 1800.0

app = Flask(__name__)
app.config['DEBUG'] = True
shutil.rmtree(CLIP_PATH, ignore_errors=True)
os.makedirs(CLIP_PATH)

clips = {}

def _path(name):
    return "%s/%s"%(CLIP_PATH, name)

def _is_exist(name):
    if name in clips and time.time() - clips[name] < TIMEOUT and os.path.exists(_path(name)):
        return True
    
    if os.path.exists(_path(name)):
        os.remove(_path(name))
    
    return False

def _save_clip(name, data):
    with open(_path(name), "wb") as f:
        f.write(data)
        return True

    return False

def _get_clip(name):
    with open(_path(name), "rb") as f:
        return f.read()
    
    return ""

@app.after_request
def apply_caching(response):
    response.headers["Server"] = "%s/v%.1f"%(__name__, __version__)
    return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/<name>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def clip(name):
    name = secure_filename(name)
    if request.method == 'POST':
        data = request.get_data()
        if _is_exist(name):
            return "", 409

        if _save_clip(name, data):
            clips[name] = time.time()
            return "", 201
        
        return "", 406

    elif request.method == 'PUT':
        data = request.get_data()
        if _is_exist(name):
            if _save_clip(name, data):
                return "", 200

            return "", 406
        
        return "", 404
    
    elif request.method == 'DELETE':
        if _is_exist(name):
            del clips[name]
            os.remove(_path(name))
            return "", 200

        return "", 404
    
    else:
        if _is_exist(name):
            return _get_clip(name), 200, {'Content-Type': 'application/octet-stream'}
        
        return "", 404

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
