import os
import main
import json
import Questions

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'legalrefund@outlook.com'
app.config['MAIL_PASSWORD'] = 'campus09'
mail = Mail(app)



def ComplexHandler(Obj):
    if hasattr(Obj, 'jsonable'):
        return Obj.jsonable()
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(Obj), repr(Obj)))


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/fragebogen")
def view_fragebogen():
    return render_template("fragebogen.html", title="Fragebogen")


@app.route("/formular")
def view_formular():
    return render_template("formular.html", title="Formular")


@app.route("/formular_sendmail", methods=['POST'])
def formular_sendmail():
    msg = Message('Verbraucherproblem-Anfrage', sender='legalrefund@outlook.com', recipients=['legalrefund@outlook.com'])
    formdata = request.data
    msg.body = formdata
    mail.send(msg)
    return render_template("sent.html", title="Sent")


@app.route("/features")
def view_features():
    return render_template("features.html", title="Features")


@app.route("/pricing")
def view_pricing():
    return render_template("pricing.html", title="Pricing")

@app.route("/pricing_sendmail", methods=['POST'])
def pricing_sendmail():
    msg = Message('Pricing-Anfrage', sender='legalrefund@outlook.com', recipients=['legalrefund@outlook.com'])
    formdata = request.data
    msg.body = formdata
    mail.send(msg)
    return render_template("sent.html", title="Sent")

@app.route("/agb")
def view_agb():
    return render_template("agb.html", title="AGB")


@app.route("/impressum")
def view_impressum():
    return render_template("impressum.html", title="Impressum")


@app.route("/getAnswer")
def get_bot_response():
    # userInput = request.args.get('msg')
    # return str(main.get_response(userInput))
    answers = main.formatRequest(request.args.get('msg'))
    return json.dumps(main.get_response(answers))


@app.route("/getQuestions")
def get_questions():
    questions = Questions.Questions()
    questions.createQuestions()
    return json.dumps(questions.__dict__, default=ComplexHandler, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
