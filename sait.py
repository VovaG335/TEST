from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')
    return 'Donate me please(no)'


@app.route("/666")
def about():
    return render_template('about.html')

@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return 'User page profile:' + name + '_' + str(id)


if __name__ == '__main__':
    app.run(debug=True)







