from flask import Flask, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')


app.run(debug=True)