from flask import Flask, render_template
from model_usuario import read_csv

app = Flask(__name__)

@app.route("/")
def home():
    data = read_csv()

    dict_home = {
        "usuario": "Admin",
        "csv": data,
    }
    
    print(dict_home["csv"])
    return render_template("index.html", res_home=dict_home)


if __name__ == "__main__":
    app.run(debug=True)
