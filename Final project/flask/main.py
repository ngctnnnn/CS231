from flask import Flask, jsonify, request, render_template, url_for
# from flask_ngrok import run_with_ngrok
import os, sys
import show
from werkzeug.utils import redirect

### FE construction
UPLOAD_FOLDER = 'upload'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'There is no file in form!'

        file = request.files['file']
        
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        return redirect('predict/' + path)
    return render_template('index.html')


@app.route("/predict/<path:path>")
def predict(path):
    return show.image_processing(path)
    return render_template('predict.html/', value='/' + path)

if __name__=='__main__':
    app.run(debug=True)

# os.system('open https://localhost:8000')

