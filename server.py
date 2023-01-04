from flask import Flask, redirect, render_template, request, session, url_for
from typing import List

app = Flask(__name__)
username = ''
password = ''


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
        result = request.form
        username = result["Email"]
        password = result["Password"]
        with open("config.py", encoding="utf-8") as file:
            lines = []
            for line in file:
                lines.append(line)
        url = "email = '" + username + "'\n" + "password = '" + password + "'"
        with open("config.py", 'w', encoding="utf-8") as f:
            for line in lines:
                f.write(line)
            f.write("\n" + url + "\n")
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
