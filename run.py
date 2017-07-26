from flask import Flask

from app.views import init_website_views

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

init_website_views(app)

if __name__ == "__main__":
    app.run(debug=True)
