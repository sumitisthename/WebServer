from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def welcome(methods=['GET']):
    return "<html><h1>Welcome to the Flask application!</h1></html>"

@app.route('/about',methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/forms',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"<html><h1>Form submitted! Hello, {name}!</h1></html>"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)