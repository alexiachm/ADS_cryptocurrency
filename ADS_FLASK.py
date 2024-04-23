
from flask import Flask, render_template, request
from tinydb import TinyDB, Query

app = Flask(_name_)
db = TinyDB('crypto_info_db.json')
crypto_table = db.table('crypto_info')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_input = request.form['search_input'].strip()  # Remove leading/trailing spaces
        if search_input:
            # Query the database to find the cryptocurrency information
            Crypto = Query()
            currency = crypto_table.search((Crypto.NIF == search_input) | (Crypto.name == search_input))
            if currency:
                return render_template('index.html', currency=currency)
            else:
                return render_template('index.html', message="No results found for '{}'.".format(search_input))
        else:
            return render_template('index.html', message="Please enter a symbol or NIF.")
    else:
        return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
