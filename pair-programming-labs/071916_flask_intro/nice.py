from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
      <!doctype html>
      <html>
        <body>
          <h1>Hi! This is the home page.</h1>
          <a href="/hello">Click here now!</a>

        </body>

      </html>

      """



@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          <select name="compliment">
            <option value="great">You're great!</option>
            <option value="smart">You're smart!</option>
            <option value="talented">You're talented!</option>
            <option value="special">You're special!</option>
          </select><br>
          How are you feeling today? 
          <label><input type="checkbox" name="feelings" value="happy">Happy</label>
          <label><input type="checkbox" name="feelings" value="sad">Sad</label>
          <label><input type="checkbox" name="feelings" value="meh">Meh</label><br>
      
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    feelings = request.args.get("feelings")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s, I think you're %s! I'm %s, you're %s.
      </body>
    </html>
    """ % (player, compliment, feelings, feelings)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
