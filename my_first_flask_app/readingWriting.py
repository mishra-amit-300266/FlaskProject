from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with open('submissions.txt', 'a') as file:
        file.write(f"{name},{email},{message}\n")

    return render_template('success.html', name=name)

@app.route('/submissions')
def show_submissions():
    entries = []
    try:
        with open('submissions.txt', 'r') as file:
            for line in file:
                name, email, message = line.strip().split(',', 2)
                entries.append({'name': name, 'email': email, 'message': message})
    except FileNotFoundError:
        entries = []

    return render_template('submissions.html', entries=entries)

@app.route('/clear', methods=['POST'])
def clear_submissions():
    open('submissions.txt', 'w').close()  # Clear the file by overwriting it with nothing
    return render_template('submissions.html', entries=[])

if __name__ == '__main__':
    app.run(debug=True)
