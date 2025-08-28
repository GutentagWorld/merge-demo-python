from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Hello App</title>
<h1>Enter your name:</h1>
<form method="post">
  <input type="text" name="username" required>
  <input type="submit" value="Say Hello">
</form>
{% if name %}
  <h2>Hello {{ name }}!</h2>
  <p>Your favorite number is: {{ favorite_number }}</p>
{% endif %}
"""


def generate_favorite_number():
    return random.randint(1, 10)


@app.route("/", methods=["GET", "POST"])
def hello():
    name = None
    favorite_number = None
    if request.method == "POST":
        name = request.form.get("username")
        favorite_number = generate_favorite_number()
    return render_template_string(HTML, name=name, favorite_number=favorite_number)


if __name__ == "__main__":
    app.run(debug=True)
