from flask import Blueprint, jsonify, current_app

bp = Blueprint('test', __name__)

@bp.route('/config')
def config():
    config_data = {
        'DB_USER': current_app.config['DB_USER'],
        'DB_NAME': current_app.config['DB_NAME'],
        'SECRET_KEY': current_app.config['SECRET_KEY'],
        'DEBUG': current_app.config['DEBUG']
    }
    return jsonify(config_data)


@bp.route('/test-logging', methods=['GET'])
def test_logging():
    current_app.logger.debug('This is a DEBUG message.')
    current_app.logger.info('This is an INFO message.')
    current_app.logger.warning('This is a WARNING message.')
    current_app.logger.error('This is an ERROR message.')
    current_app.logger.critical('This is a CRITICAL message.')

    return jsonify({'message': 'Logging messages have been sent!'})