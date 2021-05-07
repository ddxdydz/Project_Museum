import os
from csv import DictReader

from flask import Flask, render_template

from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I2D4423D2Q53D'


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
    # Для локального тестирования
    # db_session.global_init('db/forum.db')
    # app.run(port=8080, host='127.0.0.1')

    # Для удалённой загрузки
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    # main()
