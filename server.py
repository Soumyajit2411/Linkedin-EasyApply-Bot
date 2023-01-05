from flask import Flask, redirect, render_template, request
from typing import List
import assets.utils as utils

app = Flask(__name__)


@app.route('/')
def index():
    try:
        import file
        open(r'file.py', 'r').read()
    except:
        return render_template('failure.html')
    return render_template('index.html')


@app.route('/input')
def student():
    return render_template('input.html')


@app.route('/result', methods=['POST', 'GET'])
def result() -> List[str]:
    if request.method == 'POST':
        config = utils.configs(request.form)
        with open("downloads/config.py", 'w', encoding="utf-8") as f:
            f.write(config)
    return redirect('/my-link/')


@app.route('/my-link/')
def my_link():
    try:
        import linkedin
        open(r'linkedin.py', 'r').read()
    except:
        return render_template('failure.html')
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=False)
