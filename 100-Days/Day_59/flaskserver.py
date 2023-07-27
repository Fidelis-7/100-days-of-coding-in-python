from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/6c452b8687ca1d9400b8" 
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:index>')
def post(index):
    asked_post = None
    for blog_post in post:
        if blog_post['id'] == index:
            asked_post = blog_post
    return render_template("post.html", post=asked_post)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
