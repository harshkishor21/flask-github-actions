from flask import Flask,render_template

# Create a Flask web app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    # return '<h1>Hello, system! This is My CICD Pipeline test #8</h1>'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
