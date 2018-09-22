from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

# index page - display form
@app.route("/")
def index():
    title = "User Signup Page"
    return render_template("index.html", title=title)


def is_a_valid_email(email):
    if len(email) >= 3 and len(email) <= 20 and email.count(@) == 1 and email.count(.) == 1:
        return True
    else:
        return False    

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

        
    # validate user inputs

    if len(username) < 3 or len(username) > 20 or not username or re.search(" ",username):
        username_error = "Username entered is not valid. **Must have minimum length of 3 characters and maximum length of 20 characters"

    if len(password) < 3 or len(password) > 20 or not password or re.search(" ",password):
        password_error = "Password entered is not valid. **Must have minimum length of 3 characters and maximum length of 20 characters"
        password = ""
        verify_password = ""

    # if passwords do not match, show different error

    if password != verify_password:
        verify_password_error = "Entered passwords do not match. Passwords must match. Please re-enter."
        password = ""
        verify_password = ""

    # validate email if field is not empty

    if not email:
        email_error = email_error
    else:
        if not is_a_valid_email(email):
            email_error = "Email entered is not a valid format. Please re-enter"     
        

    

    # if all fields pass validation, redirect to welcome page, if not return error messages

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template("welcome.html", title="Signup Successful!", username=username)  
    else:
        return render_template("index.html", title="User Signup Form", username=username, username_error=username_error, password=password, password_error=password_error, verify_password=verify_password, verify_password_error=verify_password_error, email=email, email_error=email_error)



app.run()    