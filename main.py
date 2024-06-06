from flask import Flask

app = Flask(__name__)

@app.route("/")
# @app.route("/<name>/")
# def hello_world(name="незнакомец"):
#     return f"Привет, {name}"

# @app.route("/<password>/")
# def password(password=None):
#     if password == "1234":
#         return f"Доступ разрешён"
#     else:
#         return f"Доступ запрещён"

def hello_world():
    html = """
    <h1>Тестовый запуск локального сервера</h1>
    <p>А это просто текст</p>
    """
    return html

if __name__ == "__main__":
    app.run()
