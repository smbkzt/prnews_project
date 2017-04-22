from flask import Flask

from users.models import db
from users.views import users

app = Flask(__name__)

# Регистрация конф.файла
app.config.from_object('config')

# Регистрация бд для тек. апп
db.init_app(app)

app.register_blueprint(users, url_prefix='/api/v1/users')


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
