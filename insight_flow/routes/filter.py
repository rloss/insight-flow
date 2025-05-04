# routes/filter.py - 카테고리/태그 필터 라우트

from flask import Blueprint, render_template
import sqlite3
import os

filter_bp = Blueprint("filter", __name__, url_prefix="/filter")

# DB 경로 설정
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "posts.db")

@filter_bp.route("/category/<name>")
def category(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT id, title, content, author, tags, created_at
        FROM posts
        WHERE categories LIKE ?
        ORDER BY created_at DESC
    """, (f"%{name}%",))
    posts = c.fetchall()
    conn.close()

    # 템플릿으로 글 리스트 + 현재 카테고리명 전달
    return render_template("post_list.html", posts=posts, current_category=name)
