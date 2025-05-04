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
