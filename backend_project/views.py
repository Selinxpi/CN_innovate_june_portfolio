from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/contactus')
def contactus():
    return render_template("contactus.html")

@my_view.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@my_view.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@my_view.route('/admin')
def admin():
    return render_template("admin.html")

@my_view.route('/jscods')
def jscods():
    return render_template("jscods.html")

@my_view.route('/chat')
@my_view.route('/bot')
@my_view.route('/help')
def chatbot_redirect():
    return redirect(url_for("my_view.chatbot"))

@my_view.route('/contact')
@my_view.route('/call')
@my_view.route('/contacts')
def contactus_redirect():
    return redirect(url_for("my_view.contactus"))

@my_view.route('/about')
@my_view.route('/aboutus')
@my_view.route('/aboutme')
def about_redirect():
    return redirect(url_for("my_view.aboutus"))

@my_view.route('/javascript')
@my_view.route('/js')
@my_view.route('/home')
def index_redirect():
    return redirect(url_for("my_view.index"))

