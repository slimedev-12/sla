from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/gay")
def gay():
    return render_template("gay.html")

if __name__ == "__main__":
    app.run(debug=True)