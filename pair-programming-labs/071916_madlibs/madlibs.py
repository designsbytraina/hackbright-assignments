from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Ask for words!"""

    user_response = request.args.get("play-game")

    if user_response == "yes":
        return render_template("game.html",
                           play_game=user_response)
    else:
        return render_template("goodbye.html",
                           play_game=user_response)


@app.route('/madlib')
def show_madlib():
    """Prints out the madlib."""

    all_madlibs = ["madlib.html", "madlib2.html"]

    madlib_story = choice(all_madlibs)

    user_person = request.args.get("famous-person")
    user_color = request.args.get("color")
    user_noun = request.args.get("noun")
    user_adjective = request.args.get("adjective")
    user_place = request.args.get("place")
    user_heroine = request.args.get("heroine")
    user_food = request.args.get("food")

    return render_template(madlib_story,
                            famous=user_person,
                            color=user_color,
                            noun=user_noun,
                            adjective=user_adjective,
                            place=user_place,
                            food=user_food,
                            heroine=user_heroine)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
