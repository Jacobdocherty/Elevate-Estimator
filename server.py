
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Ensure the app binds to the correct port
    app.run(host='0.0.0.0', port=port)
