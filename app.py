from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = f"Witaj, {name}!"
        return render_template('form.html', message=message)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
