from preprocessing import load_text
from matcher import ResumeJobMatcher

resume = load_text("data/resumes/resume_1.txt")
job = load_text("data/jobs/job_1.txt")

matcher = ResumeJobMatcher()
score = matcher.match_score(resume, job)

print(f"Match score: {score}%")
