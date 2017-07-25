from flask import render_template


def index_view():
    """ Render index view """
    return render_template('index.html')


def init_website_views(app):
    """ Adds website views to Flask app """
    if app:
        app.add_url_rule('/', 'index_view', index_view, methods=['GET'])
