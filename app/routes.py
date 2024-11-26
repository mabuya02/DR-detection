from flask import Blueprint, jsonify, current_app,render_template

bp = Blueprint('test', __name__)




@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/config')
def config():
    config_data = {
        'DB_USER': current_app.config['DB_USER'],
        'DB_NAME': current_app.config['DB_NAME'],
        'SECRET_KEY': current_app.config['SECRET_KEY'],
        'DEBUG': current_app.config['DEBUG']
    }
    return jsonify(config_data)


@bp.route('/test')
def test_page():
    return render_template('index.html')

