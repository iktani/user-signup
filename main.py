from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

# index page - display form
@app.route("/")
def index():
    title = "User Signup Page"
    return render_template("index.html", title=title)

# validate inputs upon submission
@app.route("/validate-inputs", methods=['POST'])
def validate():
    # get user inputs
    username = form.request["username"]
    password = form.request["password"]
    verify_password = form.request["verify_password"]
    email = form.request["email"]

    # create variables for error messages, set to ""

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

        
    # check length requirement for username and password >3 <20

    if len(username) < 3 or len(username) > 20 or username == username_error:
        username_error = "Username entered is not valid. **Must have minimum length of 3 characters and maximum length of 20 characters"

    if len(password) < 3 or len(password) > 20 or password == password_error:
        password_error = "Password enterd is not valid. **Must have minimum length of 3 characters and maximum length of 20 characters"
        password = ""
        verify_password = ""

    # make sure there are no spaces in username or password

    if         



app.run()    