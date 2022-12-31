from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my-link/')
def my_link():
    try:
        import linkedin
        open(r'linkedinn.py', 'r').read()
    except:
        return render_template('failure.html')
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
