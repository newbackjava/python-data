from konlpy.tag import Okt
import re
import joblib
import random  # 랜덤 추천용

okt = Okt()

NEGATIVE_RECOMMENDATIONS = [
    {
        "title": "인사이드 아웃 (Inside Out, 2015)",
        "poster_url": "https://upload.wikimedia.org/wikipedia/sco/0/0a/Inside_Out_%282015_film%29_poster.jpg",
    },
    {
        "title": "월터의 상상은 현실이 된다 (The Secret Life of Walter Mitty, 2013)",
        "poster_url": "https://upload.wikimedia.org/wikipedia/ms/e/ed/Poster_Filem_The_Secret_Life_of_Walter_Mitty%2C_2013.jpg",
    },
    {
        "title": "리틀 포레스트 (Little Forest, 2018)",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/a/a4/Little_Forest_%28%EB%A6%AC%ED%8B%80_%ED%8F%AC%EB%A0%88%EC%8A%A4%ED%8A%B8%29.jpg",
    },
    {
        "title": "먹고 기도하고 사랑하라 (Eat Pray Love, 2010)",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/7/7e/Eat_pray_love_ver2.jpg",
    },
    {
        "title": "어바웃 타임 (About Time, 2013)",
        "poster_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQISeoVD--jC4jXqYUl8ZbT7l2IT2lEZBE5_IEmFYgvcUFc8_95",
    },
]

POSITIVE_RECOMMENDATIONS = [
    {
        "title": "라라랜드 (La La Land, 2016)",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    },
    {
        "title": "아이언맨 (Iron Man, 2008)",
        "poster_url": "https://i.namu.wiki/i/9fRVC4nF0Eo8rDr5uEgc-FpxVvsx-rTY-Y2WftS7Bc9K6qZcm4S-nGuBOqEea64E2WHJYldQ_cbBhBWIG40tWihaksxyCBXKVz2kItLdo10FhWdR01wFjWYv-U7FMpR838UiPJuk2uFKeQngB6K4Qg.webp",
    },
    {
        "title": "해리 포터와 마법사의 돌 (Harry Potter and the Sorcerer's Stone, 2001)",
        "poster_url": "https://i.namu.wiki/i/VgLLX3uY3clssY0hY-PATgqZlDxuN5eY3x3Uji2LIaZWPrZporjmP-hblThSJmRq6QD277Xxn1IxBb8W8urVYHyUYS-Mt19ERC-ibdJ1e4sg6elauepP6ukb1FJIOM3vls7qa3EoYqsiXEGoSA7TfA.webp",
    },
    {
        "title": "인터스텔라 (Interstellar, 2014)",
        "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oW0XQlu1lo1G_49M-YwGzKR6rUg-CtflZj07HfbT8d2GwKWg",
    },
    {
        "title": "스파이더맨: 노 웨이 홈 (Spider-Man: No Way Home, 2021)",
        "poster_url": "https://i.namu.wiki/i/OLJuk2LJUIQ428Ps3hqQOl8EfREPcdkBpWnBi9BlxspiVKdhNSZ1z0n0z8SGmzqqjiRpxNrDsBkv71lJdT6qk-4vJ81WfJTgLfcQJLzAXZuBUEO5rE1sZqjOXtwHgCdzt3S8algu3B4AYeI4UQm1sQ.webp",
    },
]



def okt_tokenize_to_str(text: str) -> str:
    # 형태소 분석 후 공백으로 이어서 하나의 문자열로 변환
    morphs = okt.morphs(text)
    return " ".join(morphs)

# 2. 학습된 TF-IDF 벡터라이저 & 감성 모델 로드
tfidf = joblib.load('movie_tfidf_vectorizer.joblib')
sentiment_model = joblib.load('movie_sentiment_model.joblib')


def ai_run(text: str):
    """
    한 문장을 입력받아 감성 분석 결과를 반환
    """
    # 1) 특수문자 제거 (한글/공백만 남기기)
    clean = re.sub(r'[^ ㄱ-ㅎ가-힣]+', " ", text)

    # 2) 학습 때와 똑같이: 먼저 Okt로 형태소 분석 → 문자열로 변환
    tokenized_str = okt_tokenize_to_str(clean)

    # 3) TF-IDF 변환
    X = tfidf.transform([tokenized_str])

    # 4) 감성 예측 (배열 → 스칼라)
    pred = int(sentiment_model.predict(X)[0])

    if pred == 0:
        label = "부정 감성"
        movie = random.choice(NEGATIVE_RECOMMENDATIONS)
    else:
        label = "긍정 감성"
        movie = random.choice(POSITIVE_RECOMMENDATIONS)

    print(clean, "->>", label)
    return movie


# 단독 테스트용
if __name__ == "__main__":
    st = "완전 ^o^ 짜증 잔뜩. 재미없어100%! ^^*"
    print(ai_run(st))