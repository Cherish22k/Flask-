from flask import Flask , redirect, url_for
app = Flask(__name__)   
@app.route('/')
def home():
    return "Welcome to the Home Page!"
@app.route("/<name>")
def user(name):
    return f"Hello, {name}!"   
@app.route('/admin')
def admin():
    return redirect(url_for('home'))  # Redirect to the home page
    if __name__ == '__main__':
    app.run()   
