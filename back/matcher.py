from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ResumeJobMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            min_df=1
        )

    def compute_similarity(self, resume_text: str, job_text: str) -> float:
        texts = [resume_text, job_text]

        tfidf_matrix = self.vectorizer.fit_transform(texts)

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        return similarity

    def match_score(self, resume_text: str, job_text: str) -> int:
        similarity = self.compute_similarity(resume_text, job_text)
        return int(similarity * 100)
