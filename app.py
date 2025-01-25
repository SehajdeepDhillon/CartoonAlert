from flask import Flask, request, redirect, url_for, render_template, flash
from config import client, r
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

def validate_phone_number(phone_number):
    try:
        lookup = client.lookups.phone_numbers(phone_number).fetch()
        phone_number = lookup.phone_number

        if lookup.country_code != 'CA':
            return False, 'Please enter a valid Canadian number'
        return True, phone_number
    except Exception:
        return False, 'Please enter a valid phone number'

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone']

        is_valid, result = validate_phone_number(phone_number)
        if not is_valid:
            flash(result, 'error')
            return redirect(url_for('index'))
        
        r.sadd('phone_numbers', result)
        flash('Phone number added successfully', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)