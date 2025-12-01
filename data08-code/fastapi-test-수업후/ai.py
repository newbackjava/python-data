from konlpy.tag import Okt
import re
import joblib
import random  # 랜덤 추천용

#전처리
# Okt()객체 생성
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


# okt에 의해서 토큰으로 끊어주는 함수 처리
def okt_tokenize_to_str(text: str):
    # 형태소 분석 후 공백으로 이어서 하나의 문자열로 변환
    morphs = okt.morphs(text)
    return " ".join(morphs)

# 모델파일과 사전파일을 load(불러옴)
tfidf = joblib.load("movie_tfidf_vectorizer.joblib")
sentiment_model = joblib.load("movie_sentiment_model.joblib")

# 외부에서 ai처리기능을 부르고 싶으면 함수를
# 만들어주어야함.
def ai_run(text): #text에는 댓글텍스트

    # 정규식에 의해서 한글만 남김
    # 1) 특수문자 제거 (한글/공백만 남기기)
    clean = re.sub(r'[^ ㄱ-ㅎ가-힣]+', " ", text)

    # okt로 토큰화처리
    # 2) 학습 때와 똑같이: 먼저 Okt로 형태소 분석 → 문자열로 변환
    tokenized_str = okt_tokenize_to_str(clean)

    # 사전에 의해서 입력된 값 변환해주어야함.
    # 3) TF-IDF 변환
    # (12만개의 컬럼이 생김) --> 원핫인코딩 형태
    X = tfidf.transform([tokenized_str])

    # 예측하면됨.
    # 4) 감성 예측 (배열 → 스칼라)
    pred = int(sentiment_model.predict(X)[0])

    movie = None; #결과 넣을 변수
    # 결과 리턴함.
    if pred == 0:
        print("부정")
        movie = random.choice(NEGATIVE_RECOMMENDATIONS)
        # random.choice([1,2,3])
        # 이 리스트에서 아무거나 선택함.
    else:
        print("긍정")
        movie = random.choice(POSITIVE_RECOMMENDATIONS)

    return movie #{title:dksl, poster_url :dddkdkk}

# main.py에서 이 함수를 불러야함.
# 그전에 자체 테스트해보자.!!


if __name__ == '__main__':
    st = "우와 인생 역작이다.! 짱이다!! 흥해라!"
    result = ai_run(st)
    print(result)
    # print("welcome")