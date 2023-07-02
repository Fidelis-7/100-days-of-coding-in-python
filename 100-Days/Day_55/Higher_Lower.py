from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlez0REHP1aesipUNaiaLIZYPeLJevGBqw4i9HWDVihQ&s'>"


@app.route("/<int:guess>")
def guess(guess):
    if guess < random_number:
        return f"<h1 style='color:Red'>number is too low<h1>" \
               "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlez0REHP1aesipUNaiaLIZYPeLJevGBqw4i9HWDVihQ&s'>"
    elif guess > random_number:
        return f"<h1 style='color:Red'>number is too low<h1>" \
               "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlez0REHP1aesipUNaiaLIZYPeLJevGBqw4i9HWDVihQ&s'>"
    else:
        return f"<h1 style='color:Green'>You got the number<h1>" \
               "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlez0REHP1aesipUNaiaLIZYPeLJevGBqw4i9HWDVihQ&s'>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)