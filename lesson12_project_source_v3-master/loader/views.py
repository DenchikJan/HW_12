from flask import render_template, Blueprint, request
import json
import logging

logging.basicConfig(filename="log.log", level=logging.INFO)


def upload_post(new_post):
    with open('posts.json', 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
    with open("posts.json", 'w', encoding="utf-8") as file:
        content.append(new_post)
        json.dump(content, file, ensure_ascii=False)


ALLOWED_EXTENSIONS = {'png', 'jpeg'}


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/GET/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/POST/post', methods=["POST"])
def page_post_upload():
    if request.files.get("picture"):
        picture = request.files.get("picture")
        filename = picture.filename
        if is_filename_allowed(filename):
            picture.save(f"./static/uploads/images/{filename}")
            upload_post(new_post={"pic": f"./static/uploads/images/{filename}", "content": request.form['content']})
            return render_template('post_uploaded.html', content=request.form['content'], filename=picture.filename)
        else:
            extension = filename.split(".")[-1]
            logging.info(f'Загруженный файл не картинка')
            return f"Тип файлов {extension} не поддерживается"

    else:
        return "ошибка загрузки"
        logging.ERROR(f'Ошибка загрузки файла')
