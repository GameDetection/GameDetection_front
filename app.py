from imp import NullImporter
import json

from flask import Flask, render_template, request
app = Flask(__name__)


def callPredict(file):



    return {'precision': '100%','resul':'MMO'}


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
