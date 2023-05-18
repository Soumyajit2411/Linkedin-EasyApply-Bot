import os

from flask import Flask, redirect, render_template, request
from typing import List
import assets.utils as utils

app = Flask(__name__)


@app.route('/input')
def student():
    return render_template('input.html')


@app.route('/result', methods=['POST', 'GET'])
def result() -> List[str]:
    if request.method == 'POST':
        config = utils.configs(request.form)
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        try:
            with open("downloads/config.py", 'w', encoding="utf-8") as f:
                f.write(config)
        except:
            print("No Data Provided!")
    return redirect('/my-link/')


@app.route('/my-link/')
def my_link():
    try:
        import linkedin
        open(r'linkedin.py', 'r').read()
    except Exception as e:
        print(e)
        return render_template('failure.html')
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
