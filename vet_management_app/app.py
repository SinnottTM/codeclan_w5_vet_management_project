# app file, TBC

from flask import Flask, render_template
from controllers.kaiju_controller import kaiju_blueprint
from controllers.vet_controller import vet_blueprint

app = Flask(__name__)

app.register_blueprint(kaiju_blueprint)
# app.register_blueprint(vet_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
