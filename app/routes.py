from flask import render_template

def register_routes(app):
    
    @app.route("/")
    def home():
        return render_template("home/index.html")

    @app.route("/jobs")
    def jobs():
        return render_template("jobs/index.html")

    @app.route("/companies")
    def companies():
        return render_template("companies/index.html")

    @app.route("/resume-builder")
    def resume_builder():
        return render_template("resume_builder/index.html")

    @app.route("/ai-tools")
    def ai_tools():
        return render_template("ai_tools/index.html")

    return app