from flask import Flask, request, redirect, render_template
import re
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

# index page - display form
@app.route("/")
def index():
    title = "User Signup Page"
    return render_template("index.html", title=title, heading=title)


def is_a_valid_email(email):
    pattern=re.compile(r"^[\S]{3,20}$")
    if pattern.match(email) and email.count("@") == 1 and email.count(".") == 1:
        return True
    else:
        return False    

# validate inputs upon submission
@app.route("/", methods=['POST'])
def validate():
    # get user inputs
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    # create variables for error messages, set to ""

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

        
    # validate user inputs
    pattern=re.compile(r"^[\S]{3,20}$")
    

    if not pattern.match(username) or not username:
        username_error = "Username entered is not valid. **Must have minimum length of 3 characters and maximum length of 20 characters with no spaces."

    if not pattern.match(password) or not password:
        password_error = "Password entered is not valid. **Must have minimum length of 3 characters and maximum length of 20 characters with no spaces."

    # if passwords do not match, show different error

    if password != verify_password:
        verify_password_error = "Entered passwords do not match. Passwords must match. Please re-enter."

    # validate email if field is not empty

    if not email:
        email_error = email_error
    else:
        if not is_a_valid_email(email):
            email_error = "Email entered is not a valid format. Please re-enter"
            
    # if username or email are errors, erase password and verify_password fields
    
    if username_error or email_error or password_error or verify_password_error:
        password = ""
        verify_password = ""              
     
    
    # if all fields pass validation, redirect to welcome page, if not return error messages

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template("welcome.html", title="Signup Successful!", heading="Success!", username=username) 
    else:
        return render_template("index.html", title="User Signup Form", heading="User Signup Form - Please fix errors", username=username, username_error=username_error, password=password, password_error=password_error, verify_password=verify_password, verify_password_error=verify_password_error, email=email, email_error=email_error)



app.run()    