import os
from flask import Flask, request, flash, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
from pdfconduit import Watermark
from dirutility import DirPaths


def apply_watermark(file_path, params):
    # Execute Watermark class
    wm = Watermark(file_path, progress_bar_enabled=False, use_receipt=False, open_file=False)

    wm.draw(text1=params['address'],
            text2=str(params['town'] + ', ' + params['state']))
    return wm.add()


ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = 16 * (1024 * 1024)
UPLOAD_FOLDER = '/app/uploads'

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post action=http://18.204.43.53/watermark/process enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/uploads', methods=['GET'])
def all_uploads():
    response = '<ul>'
    uploads = DirPaths('/app/uploads', full_paths=False).walk()
    for upload in uploads:
        response += '''
        <li>
            <a href="/uploads/{0}">{0}</a>
        </li>
        '''.format(upload)
    response += '</ul>'
    return response


@app.route('/test', methods=['GET'])
def test():
    return 'pdfconduit-sandbox docker container is running!'


if __name__ == '__main__':
    # docker build -t basic .
    # docker run -i -t -p 5000:5000 basic:latest
    app.run(host='0.0.0.0', port=5000, debug=True)
