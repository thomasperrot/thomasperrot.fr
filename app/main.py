import os
from threading import Thread

from flask import Flask, render_template, request
from flask.ext.mail import Mail, Message
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')


@app.route('/')
def index():
    # TODO: send me a mail with ser data
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    print(user_agent, ip)
    if app.config['FLASKY_ADMIN']:
        send_email(app.config['FLASKY_ADMIN'], 'New visitor', 'mail/new_visitor', user_agent=user_agent, ip=ip)
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

if __name__ == '__main__':
    manager.run()
