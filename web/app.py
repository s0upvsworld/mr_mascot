from flask import Flask, render_template, request, flash, redirect, url_for
import json
import os
import re

app = Flask(__name__)
app.secret_key = os.urandom(24)  # for flash messages

# Get the absolute path to the parent directory where .users.json is located
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_FILE = os.path.join(PARENT_DIR, '.users.json')

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_user(name, email):
    try:
        # Read existing users
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
        
        # Check if email already exists
        if any(user['email'] == email for user in users):
            return False, "This email is already subscribed!"
        
        # Add new user
        new_user = {
            "id": len(users) + 1,
            "name": name,
            "email": email
        }
        users.append(new_user)
        
        # Write back to file
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=4)
        
        return True, "Successfully subscribed!"
    except Exception as e:
        return False, f"An error occurred: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        
        # Validation
        if not name:
            flash('Please enter your name!', 'error')
        elif not email:
            flash('Please enter your email!', 'error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address!', 'error')
        else:
            success, message = add_user(name, email)
            if success:
                flash(message, 'success')
                return redirect(url_for('index'))
            else:
                flash(message, 'error')
    
    return render_template('index.html')

@app.route('/prompt', methods=['GET', 'POST'])
def prompt():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        
        # Validation
        if not name:
            flash('Please enter your name!', 'error')
        elif not email:
            flash('Please enter your email!', 'error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address!', 'error')
        else:
            success, message = add_user(name, email)
            if success:
                flash(message, 'success')
                return redirect(url_for('index'))
            else:
                flash(message, 'error')
    
    return render_template('index.html')



if __name__ == '__main__':
    # Verify users file exists
    if not os.path.exists(USERS_FILE):
        print(f"Warning: {USERS_FILE} not found!")
    app.run(host='0.0.0.0', port=5000, debug=True) 