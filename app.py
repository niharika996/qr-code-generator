from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_generated = False
    if request.method == "POST":
        data = request.form["data"]
        img = qrcode.make(data)        
        os.makedirs("static", exist_ok=True)
        img.save("static/qr.png")
        qr_generated = True
    return render_template("index.html", qr_generated=qr_generated)

if __name__ == "__main__":
    app.run(debug=True)
