import os
from flask import Flask
from flask_cors import CORS

app = Flask(
    __name__,
    instance_relative_config=True,
    static_url_path=''
)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('FLASK_SECRET'),
)
CORS(app)

from controller import (
    main, pwa
)
app.register_blueprint(main.bp)
app.register_blueprint(pwa.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)