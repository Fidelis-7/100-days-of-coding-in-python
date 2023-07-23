from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return ""


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/6c452b8687ca1d9400b8"
    response = requests.get(blog_url)
    all_posts = response.json()
    render_template("blog.html", all_posts=all_posts)


@app.route("/guess/<username>")
def guess(username):
    made_req_for_age = requests.get(f"https://api.agify.io?name={username}")
    response_for_made_req_for_age = made_req_for_age.json()

    made_req_for_age = requests.get(f"https://api.genderize.io?name={username}")
    response_for_made_req_for_gender = made_req_for_age.json()
    return render_template("Bio.html", username=username.capitalize(), gender=response_for_made_req_for_gender["gender"]
                           , age=response_for_made_req_for_age["age"])


if __name__ == "__main__":
    app.run(debug=True, port=8080)
