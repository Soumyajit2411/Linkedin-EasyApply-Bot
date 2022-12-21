from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my-link/')
def my_link():
    import linkedin
    print('I got clicked!')
    file = open(r'linkedin.py', 'r').read()
    exec(file)
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
