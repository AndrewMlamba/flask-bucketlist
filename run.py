import os

from flask import Flask, render_template

from app.views import init_website_views

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

init_website_views(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    port = port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
