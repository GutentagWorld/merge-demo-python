from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Hello App</title>
<style>
    body, html {
        height: 100%;
        margin: 0;
        padding: 0;
    }
    .center-container {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>
<div class="center-container">
    <h1>Enter your name:</h1>
    <form method="post">
        <input type="text" name="username" required>
        <input type="submit" value="Say Hello">
    </form>
    {% if name %}
        <h2>Hello {{ name }}!</h2>
        <p>Your favorite number is: {{ favorite_number }}</p>
    {% endif %}
</div>
"""


def generate_favorite_number():
    return random.randint(1, 10)


@app.route("/", methods=["GET", "POST"])
def hello():
    name = None
    favorite_number = None
    error = None
    if request.method == "POST":
        name = request.form.get("username")
        if name and len(name) > 20:
            error = "Name must be less than 20 characters."
            name = None
        else:
            favorite_number = generate_favorite_number()
    return render_template_string(
        HTML + ("<p style='color:red;'>{{ error }}</p>" if error else ""),
        name=name,
        favorite_number=favorite_number,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
