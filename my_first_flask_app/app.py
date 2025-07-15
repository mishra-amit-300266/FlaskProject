from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/greet', methods=['POST'])
def greet():
    user = request.form['user_name']
    return render_template('greet.html', name=user)

if __name__ == '__main__':
    app.run(debug=True)
