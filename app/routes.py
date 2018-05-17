from app import app, db
from app.models import Stadium

from flask import render_template
from flask import request
from flask import redirect

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/stadiums", methods=["GET", "POST"])
def stadiums():
    stadiums = Stadium.query.all()
    return render_template("matches.html", stadiums=stadiums)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.form:
        stadium = Stadium(name=request.form.get("name"), city=request.form.get("city"), country=request.form.get("country"))
        db.session.add(stadium)
        db.session.commit()
    return render_template("add.html")

@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    stadium = Stadium.query.filter_by(id=id).first()
    if request.form:
        print(request.form)
        stadium.name = request.form.get("newname")
        stadium.city  = request.form.get("newcity")
        stadium.country  = request.form.get("newcountry")
        db.session.commit()
        return redirect("/stadiums")
    return render_template("update.html", stadium=stadium)

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    stadium = Stadium.query.filter_by(id=id).first()
    db.session.delete(stadium)
    db.session.commit()
    return redirect("/stadiums")
