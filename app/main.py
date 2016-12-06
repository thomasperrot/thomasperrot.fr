from flask import Flask, render_template, request
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    # TODO: send me a mail with ser data
    user_agent = request.headers.get('User-Agent')
    headers = request.headers.get('headers')
    ip = request.remote_addr
    print(ip)
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.error_handlers(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


# @app.error_handlers(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
