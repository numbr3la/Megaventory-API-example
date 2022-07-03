from flask import Flask, Blueprint, render_template
import src.Test as Test

website = Blueprint('website', __name__, template_folder='templates')

@website.route("/")
def main_page():
    return render_template('index.html')


@website.route('/test')
def test():
    apiTest = Test.Test()
    apiTest.run()


    return '[Test completed]'