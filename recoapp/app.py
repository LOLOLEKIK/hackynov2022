from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import src.reco as reco
import os


app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
app.config['UPLOAD_FOLDER'] = "upload"
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024

def allowed_file(filename):
    for extension in ALLOWED_EXTENSIONS:
        if filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS:
            return True
    return False

@app.route('/', methods=('GET', 'POST'))
def hello():
    if request.method == 'POST':
        img = request.files['img']
        if allowed_file(img.filename):
            filename = secure_filename(img.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img.save(path)
            if img != '':
                result = reco.reco.reco(path)
                os.remove(path)
                return render_template('result.html', text=result )
            else:
                return render_template('index.html')
        else:
            return render_template('error.html')      
    elif request.method == 'GET':
        return render_template('index.html')
