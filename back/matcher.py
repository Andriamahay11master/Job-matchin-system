from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class ResumeJobMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 3),
            min_df=1,
            sublinear_tf=True,
            norm="l2"
        )

    def fit_transform(self, resume_text: str, job_text: str):
        texts = [resume_text, job_text]
        tfidf = self.vectorizer.fit_transform(texts)
        return tfidf

    def compute_similarity(self, resume_text: str, job_text: str) -> float:
        tfidf = self.fit_transform(resume_text, job_text)
        similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return similarity

    def match_score(self, resume_text: str, job_text: str) -> int:
        similarity = self.compute_similarity(resume_text, job_text)
        score = min(similarity * 150, 100)  # soft UX scaling
        return int(score)

    def explain(self, resume_text: str, job_text: str, top_n=10):
        tfidf = self.fit_transform(resume_text, job_text)

        feature_names = self.vectorizer.get_feature_names_out()

        resume_vec = tfidf[0].toarray()[0]
        job_vec = tfidf[1].toarray()[0]

        # Terms important in job description
        job_indices = np.argsort(job_vec)[::-1]

        matched = []
        missing = []

        for idx in job_indices:
            term = feature_names[idx]

            if job_vec[idx] <= 0:
                continue

            if resume_vec[idx] > 0:
                matched.append(term)
            else:
                missing.append(term)

            if len(matched) >= top_n and len(missing) >= top_n:
                break

        return {
            "matched_skills": matched[:top_n],
            "missing_skills": missing[:top_n]
        }
