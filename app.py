from flask import Flask, render_template, request
from back.preprocessing import clean_text
from back.matcher import ResumeJobMatcher

app = Flask(
    __name__,
    static_folder="assets",
    static_url_path="/static"
)

matcher = ResumeJobMatcher()

@app.route("/", methods=["GET", "POST"])
def index():
    resume_text = ""
    job_text = ""
    score = None
    explanation = None

    if request.method == "POST":
        resume_text = request.form["resume"]
        job_text = request.form["job"]

        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_text)

        score = matcher.match_score(resume_clean, job_clean)
        explanation = matcher.explain(resume_clean, job_clean)

    return render_template(
        "index.html",
        resume=resume_text,
        job=job_text,
        score=score,
        explanation=explanation
    )

if __name__ == "__main__":
    app.run(debug=True)
