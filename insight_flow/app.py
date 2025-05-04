# app.py - Flask 앱 실행 진입점
from flask import Flask
from routes.home import home_bp
from routes.post import post_bp
from routes.filter import filter_bp
from routes.community import community_bp  # 아직 미구현이지만 구조만 포함

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # CSRF/세션 보호용 키

# 라우트 등록
app.register_blueprint(home_bp)
app.register_blueprint(post_bp)
app.register_blueprint(filter_bp)
app.register_blueprint(community_bp)

# 정적 파일 설정 (static/, templates/)
app.static_folder = "static"
app.template_folder = "templates"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
