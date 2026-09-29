import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer

# 문장에서 수식 제거 & 공백 자유도 제거
def clean_text(text):
    # $ ... $ 형태의 LaTeX 수식 제거
    text = re.sub(r"\$.*?\$", " ", text)

    # 공백 여러 개 → 하나
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# 흔히 사용되는 단어 제거
stopwords = set(ENGLISH_STOP_WORDS)
stopwords.update({
    "paper", "study", "result", "results",
    "present", "presented", "obtained",
    "observed", "shown", "data"
})

# 주제랑 무관한 phrase 제거
exclude_phrases = {
    "different values",
    "experimental results",
    "numerical results",
    "good agreement",
    "previous work",
    "present work",
    "recent years",
    "new method",
    "et al",
    "high resolution",
}

# main method
def get_words_freq(start_year, end_year, criterion="topics"):
    global stopwords
    global exclude_phrases

    df = pd.read_csv(f"physics_{start_year}_{end_year}.csv")
    # print(df.shape)
    # print(df.head())
    # print(df["subfield"].value_counts())
    # print(df["year"].value_counts().sort_index())
    df = df.dropna(subset=["title"])

    if criterion == "topics":
        # 각 셀의 topic들을 분리
        topics = df["topics"].str.split(" | ", regex=False)

        # 논문별 list를 하나의 긴 Series로 펼치기
        all_topics = topics.explode()

        # 각 topic의 등장 비율
        topic_frequency = all_topics.value_counts() / len(df)

        # ("topic", frequency) 형태의 list로 변환
        return list(topic_frequency.items())

    df[f"clean_{criterion}"] = df[criterion].apply(clean_text)

    vectorizer = CountVectorizer(
        stop_words=list(stopwords),
        ngram_range=(2, 5),
        min_df=5,
        binary=True     # 등장했다 안 했다만 구분함
    )

    X = vectorizer.fit_transform(df[f"clean_{criterion}"])
    terms = vectorizer.get_feature_names_out()

    mask = [
        term not in exclude_phrases
        for term in terms
    ]

    terms = terms[mask]     # exclude_phrases에 있는 phrase들은 제거
    X = X[:, mask]  # X[i][j] = i번째 논문에서 j번째 phrase 등장 여부 (0 또는 1)
    phrase_frequency = np.asarray(X.mean(axis=0)).ravel()   # phrase_frequency[i] = i번째 phrase 등장 빈도수 (0 - 1 사이)

    # [("phrase", float(frequency)),..] : 빈도수를 기준으로 내림차순 정렬
    words_freq = sorted(
        zip(terms, phrase_frequency),
        key=lambda x: x[1],
        reverse=True
    )

    return words_freq

if __name__ == "__main__":
    words_freq = get_words_freq(2020, 2024, criterion="topics")
    for topic in words_freq:
        print(topic[0], f"{topic[1]:.5f}")