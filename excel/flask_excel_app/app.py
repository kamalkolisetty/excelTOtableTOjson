from flask import Flask, request, render_template_string, redirect, url_for
import pandas as pd
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            data = df.to_dict(orient='records')
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return redirect(url_for('success'))
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upload Excel File</title>
    </head>
    <body>
        <h1>Upload an Excel File</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    ''')

@app.route('/success')
def success():
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Success</title>
    </head>
    <body>
        <h1>File successfully uploaded and saved as JSON!</h1>
        <a href="/">Upload another file</a>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)


"""
from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            data = df.to_html()
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upload Excel File</title>
    </head>
    <body>
        <h1>Upload an Excel File</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
        <h2>Data:</h2>
        <div>{{ data|safe }}</div>
    </body>
    </html>
    ''', data=data)

if __name__ == "__main__":
    app.run(debug=True)

"""