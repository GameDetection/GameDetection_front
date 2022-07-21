from imp import NullImporter
import json
import os

from flask import Flask, render_template, request
app = Flask(__name__)

UPLOAD_FOLDER = 'asset'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def callPredict(file_name):
    file_location = os.path.join(app.config['UPLOAD_FOLDER'], file_name)


    return {'precision': '100%','resul':'MMO'}


def checkValidationFile(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/dnd',methods=['POST','GET'])
def dnd():
    print(f"{request.method=}")
    if request.method =="GET":
        return render_template('dnd.html')

    imgf = request.files.get('def','')
    file_name = imgf.filename

    if file_name is not '' and checkValidationFile(file_name):
        print(f'{imgf=}')
        print(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        imgf.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

    res = callPredict(file_name)
    return render_template('dnd.html',res = res)


@app.route('/',methods=['POST','GET'])
def main():

    img = 'no img'
    print(f"{request.method=}")
    if request.method =="POST":
        imgf = request.files.get('def','')
        img = ' img found'
        print(f'{imgf=}')

        res = callPredict(imgf)
        return render_template('index.html',img = img,res = res)

    return render_template('index.html',img = img)

if __name__ == '__main__':
    app.run()
