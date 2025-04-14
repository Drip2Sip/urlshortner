from flask import Flask, render_template, request
import pyshorteners
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    shorter_url = None
    if request.method == 'GET' and 'name' in request.args:
        url = request.args.get('name')
        if url:
            s = pyshorteners.Shortener()
            shorter_url = s.tinyurl.short(url)
    return render_template('home.html', shorter_url=shorter_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  # Heroku compatibility