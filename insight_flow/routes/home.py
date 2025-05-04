# home.py - 메인 페이지 라우트
from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return render_template("home.html")

@home_bp.route("/community")
def community():
    return render_template("community.html")