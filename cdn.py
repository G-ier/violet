from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import send_file
import os

app = Flask(__name__)

# This is necessary because QUploader uses an AJAX request
# to send the file
cors = CORS()
cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

@app.route('/upload', methods=['POST'])
def upload():
    for fname in request.files:
        f = request.files.get(fname)
        print(f)
        f.save('./uploads/%s' % secure_filename(fname))

    return 'Okay!'

@app.route('/get_image', methods=['GET'])

def get_image():
    filename = "./uploads/" + request.args.get('file')
    return send_file(filename, mimetype='image/gif')

if __name__ == '__main__':
    if not os.path.exists('./uploads'):
        os.mkdir('./uploads')
    app.run(debug=True)