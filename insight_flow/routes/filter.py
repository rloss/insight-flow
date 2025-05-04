# filter.py - 카테고리/태그 필터 라우트
from flask import Blueprint

filter_bp = Blueprint("filter", __name__)

@filter_bp.route("/category/<name>")
def category(name):
    return f"카테고리: {name}"
