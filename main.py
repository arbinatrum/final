from flask import Flask
from flask import render_template, request
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'myflaskapptest@mail.ru'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'myflaskapptest@mail.ru'  # и здесь
app.config['MAIL_PASSWORD'] = 'sALEdXHTCxAMTkz6ALfF'
mail = Mail(app)



# myapp1234

@app.route('/mail', methods=['POST'])
def send_mail():
    email = request.form.get("email")
    full_name = request.form.get("full_name")
    phone_number = request.form.get("phone_number")

    try:
        with open("static/email_template.html") as file:
            template = file.read()
    except IOError:
        return "The template file doesn`t found!"

    text = f"""
        <h2>Пользователь {full_name}, Телефон - {phone_number} и с почтой - {email}</h2>\n<p>Записался на тренинг</p>
        """
    msg = Message("Ваш персональный тренер", recipients=[email], html=template)
    mail.send(msg)
    msg2 = Message("Новый заказчик!", recipients=[app.config['MAIL_DEFAULT_SENDER']], html=text)
    mail.send(msg2)
    return show_main(flag=True)


@app.route('/')
def index():
    return show_main()


@app.route('/main')
def show_main(flag=False):
    return render_template('/main.html', flag=flag)


if __name__ == '__main__':
    app.run()
