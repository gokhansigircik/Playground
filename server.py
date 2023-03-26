from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play/")
def play():
    return render_template("index.html")

@app.route("/play/<int:num>")
def box(num):
  return render_template("level2.html", num=num)

@app.route("/play/<int:num>/<color>")
def changeboxes(num, color):
  return render_template("level3.html", num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)