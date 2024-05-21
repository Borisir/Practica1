from flask import Flask
from controllers.factura_controller import factura_blueprint

app = Flask(__name__)
app.register_blueprint(factura_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
