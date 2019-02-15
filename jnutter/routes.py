from flask import render_template, url_for
from jnutter import app


@app.route("/index")
def index():
    return render_template('index.html', title='Home')
    
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/work")
def work():
    return render_template('work.html', title='Work')

@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog')