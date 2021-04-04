import os
from csv import DictReader
from requests import get

from flask import Flask, request, render_template, redirect, abort, session, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import abort, Api

from data import db_session
from data.__all_models import *
from forms.registerform import RegisterForm
from forms.loginform import LoginForm
from forms.topicform import TopicForm
from forms.questionform import QuestionForm

ROLES = ["user", "admin"]

TOPIC_IMG_DIR = 'static/img/topic_img'
QUESTION_IMG_DIR = 'static/img/quest_img'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I2D4423D2Q53D'

# login_manager = LoginManager()
# login_manager.init_app(app)

api = Api(app)


@app.route('/')
@app.route('/<string:page_name>')
def show_page(page_name=''):
    page_name = f'{page_name if page_name else "index"}.html'
    data = dict()
    with open('static/relationship_file.csv', mode='rt', encoding='utf8') as s_file:
        page_csv_name = list(DictReader(s_file, delimiter=';', quotechar='"'))[0]
        if page_name in page_csv_name:
            with open(f'static/{page_csv_name[page_name]}', mode='rt', encoding='utf8') as file:
                data = list(DictReader(file, delimiter=';', quotechar='"'))
    return render_template(page_name, data=data)


def main():
    db_session.global_init('db/forum.db')
    # app.run(port=8000, host='127.0.0.1')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()