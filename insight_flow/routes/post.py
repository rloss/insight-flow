# post.py - 글 쓰기, 보기, 수정, 삭제
from flask import Blueprint

post_bp = Blueprint("post", __name__, url_prefix="/post")

@post_bp.route("/")
def post_index():
    return "✅ post blueprint 연결됨"
