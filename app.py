from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form['email']
    password = request.form['password']
    print(f'Email: {email}, Password: {password}')
    return redirect('/login')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    print(f'Email: {email}, Password: {password}')
    return redirect('/home')


if __name__ == '__main__':
    app.run()