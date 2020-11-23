import os

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

from model.model import initialize_model, calcforuser


def createApp():
    return Flask(__name__)


app = createApp()

UPLOAD_FOLDER = os.path.abspath(os.getcwd()) + "/files"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        mode = request.form.get('mode')
        if mode == 'accuracy':
            print("Starting accuracy")
            initialize_model('accuracy')
        else:
            print("Starting f score")
            initialize_model('f_score')
        initialized = 1
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
        print(uploaded_files)
        valid_files = []
        for file in uploaded_files:
            if allowed_file(file.filename):
                filename = os.path.join(
                    app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filename)
                valid_files.append(secure_filename(file.filename))
        if len(valid_files) <= 2:
            return "Upload atleast 2 valid files"
        ret = []
        for file1 in valid_files:
            for file2 in valid_files:
                if file1 == file2:
                    continue
                file1path = "files/" + file1
                file2path = "files/" + file2
                res = calcforuser(file1path, file2path)
                if res:
                    ret.append(
                        {'file1': file1, 'file2': file2, 'res': 'Plagiarized'})
                else:
                    ret.append(
                        {'file1': file1, 'file2': file2, 'res': 'Not plagiarized'})
        for file in valid_files:
            os.remove("files/" + file)
        return render_template('results.html', valid_files=valid_files, res=ret)
    else:
        return "No files sent!"


@app.route("/")
def select_type():
    return render_template('select.html')


if __name__ == '__main__':
    initialize_model(modeltype="accuracy")
    app.run(debug=True)
