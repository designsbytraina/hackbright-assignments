from flask import Flask, render_template, request


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "KEYSTUFFGOESHERE"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show the application form to user."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def submit_application():
    """Return a confirmation to user that application was submitted."""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary = request.form.get("salary")
    position = request.form.get("apply-role")

    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salary=salary,
                            position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    app.run(host="0.0.0.0")

