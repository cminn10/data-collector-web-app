from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://kurasame:soldout@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Float)

    def __init__(self, email, height):
        self.email_ = email
        self.height_ = height
#from app import db
#db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            collected = Data(email, height)
            db.session.add(collected)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1)
            num_in = db.session.query(Data.height_).count()
            send_email(email, height, average_height, num_in)
            return render_template("success.html")
    return render_template('index.html', 
    text = "Seems like you have already submitted.")

if __name__ == '__main__':
    app.debug = True
    app.run()