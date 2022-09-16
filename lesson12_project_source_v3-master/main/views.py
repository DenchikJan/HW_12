from flask import render_template, Blueprint, request
import json
from json import JSONDecodeError
import logging

logging.basicConfig(filename="log.log", level=logging.INFO)


def read_json():
    with open('posts.json', 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
        return content


def search_posts(text):
    posts = []
    contents = read_json()
    for content in contents:
        if text.lower() in content['content'].lower():
            posts.append(content)
    return posts


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search')
def page_tag():
    try:
        logging.info(f'Выполнин поиск по слову - {request.args.get("s")}')
        return render_template('post_list.html', s=request.args.get("s"), posts=search_posts(request.args.get("s")))
    except FileNotFoundError:
        return f'Файл не найден <a href="/" class="link">Назад</a>'
    except JSONDecodeError:
        return f'Файл не удается преобразовать <a href="/" class="link">Назад</a>'
