from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/products", methods=["GET"])
def products():
    return render_template("products.html")
# Add routes here

if __name__ == "__main__":
    app.run(debug=True, port=5000)