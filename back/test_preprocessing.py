from preprocessing import load_text

resume = load_text("data/resumes/resume_1.txt")
job = load_text("data/jobs/job_1.txt")

print("Resume:", resume)
print("Job:", job)
