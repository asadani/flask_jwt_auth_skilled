from flask import Flask

from routes.employee import employee_blueprint

app = Flask(__name__)
app.register_blueprint(employee_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
