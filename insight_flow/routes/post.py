from flask import Blueprint, render_template, request, redirect
import sqlite3
from datetime import datetime
import os

post_bp = Blueprint("post", __name__, url_prefix="/post")

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "posts.db")

@post_bp.route("/write", methods=["GET", "POST"])
def write_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        author = request.form["author"]
        categories = ",".join(request.form.getlist("categories"))
        tags = request.form["tags"]
        created_at = datetime.now().isoformat()

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            INSERT INTO posts (title, content, author, categories, tags, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, content, author, categories, tags, created_at))
        conn.commit()
        conn.close()

        return redirect("/post")

    # 카테고리 리스트 (UI에서 표시용)
    category_options = ["기술", "경제", "트렌드", "사회", "기타"]
    return render_template("post_form.html", categories=category_options)

@post_bp.route("/")
def post_list():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, title, author, tags, created_at FROM posts ORDER BY created_at DESC")
    posts = c.fetchall()
    conn.close()

    # posts = [(1, "제목", "작성자", "GPT,AI", "2024-05-01T10:30:00"), ...]
    return render_template("post_list.html", posts=posts)

@post_bp.route("/<int:post_id>")
def post_detail(post_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    post = c.fetchone()
    conn.close()

    if not post:
        return "해당 글을 찾을 수 없습니다.", 404

    return render_template("post_detail.html", post=post)
