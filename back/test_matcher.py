from preprocessing import load_text
from matcher import ResumeJobMatcher

resume = load_text("data/resumes/resume_1.txt")
job = load_text("data/jobs/job_1.txt")

matcher = ResumeJobMatcher()

score = matcher.match_score(resume, job)
explanation = matcher.explain(resume, job)

print(f"Match score: {score}%\n")

print("Matched skills:")
for s in explanation["matched_skills"]:
    print("-", s)

print("\nMissing skills:")
for s in explanation["missing_skills"]:
    print("-", s)
