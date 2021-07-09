from flask import Flask, Blueprint, render_template
from app.forms import SimpleForm
from app.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
bp = Blueprint("init", __name__, url_prefix="")

# app.init_app

bp.route("/", methods=["GET"])
def get_main_page():
    return render_template("main_page.html")


bp.route("/simple-form", methods=["GETS"])
def get_simple_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)
