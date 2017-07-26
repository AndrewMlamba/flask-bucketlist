from flask import render_template


def index_view():
    """ Render index view """
    return render_template('index.html')


def register_view():
    """ Render register view """
    return render_template('register.html')


def about_view():
    """ Render about view """
    return render_template('about.html')


def init_website_views(app):
    """ Adds website views to Flask app """
    if app:
        app.add_url_rule('/', 'index_view', index_view, methods=['GET'])
        app.add_url_rule('/register', 'register_view', register_view, methods=['GET'])
        app.add_url_rule('/about', 'about_view', about_view, methods=['GET'])
