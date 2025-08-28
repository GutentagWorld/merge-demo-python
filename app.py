from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Hello App</title>
<h1>Enter your name:</h1>
<form method="post">
  <input type="text" name="username" required>
  <input type="submit" value="Say Hello">
</form>
{% if name %}
  <h2>Hello {{ name }}!</h2>
{% endif %}
'''


@app.route('/', methods=['GET', 'POST'])
def hello():
  name = None
  if request.method == 'POST':
    name = request.form.get('username')
  return render_template_string(HTML, name=name)


if __name__ == '__main__':
  app.run(debug=True)
