import os
from app import app
from flask import request, send_from_directory, render_template
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip',
                          '.tar.gz', '.7z', 'gz', 'bz2'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    error = False
    filename = ""
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename = filename
        else:
            error = True

    return render_template("upload.html", allowed_extension=ALLOWED_EXTENSIONS,
                           upload_error=error, filename=filename)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/list')
def list_files():
    onlyfiles = [f for f in os.listdir(app.config['UPLOAD_FOLDER'])
                 if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'],
                                                f))]
    onlyfiles.remove(".gitignore")
    return render_template("list.html", files=onlyfiles)
