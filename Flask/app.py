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

#Variable Routing
@app.route('/forms/<score>')
def score(score):
    try:
        score = int(score)
        if score < 0 or score > 100:
            return "<html><h1>Score must be between 0 and 100!</h1></html>"
        return f"<html><h1>Your score is {score}.</h1></html>"
    except ValueError:
        return "<html><h1>Invalid score format!</h1></html>"

if __name__ == '__main__':
    app.run(debug=True)