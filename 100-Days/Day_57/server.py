from flask import Flask, render_template
import random, datetime

app = Flask(__name__)


@app.route("/")
def home():
    automated_year = datetime.date.today()
    random_number = random.randint(0, 9)
    return render_template("index.html", num=random_number, automated_year=automated_year.year)


if __name__ == "__main__":
    app.run(debug=True)

