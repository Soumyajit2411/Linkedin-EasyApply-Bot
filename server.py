from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    try:
        import file
        open(r'file.py', 'r').read()
    except:
        return render_template('failure.html')
    return render_template('index.html')


@app.route('/my-link/')
def my_link():
    try:
        import linkedin
        open(r'linkedin.py', 'r').read()
    except:
        return render_template('failure.html')
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
