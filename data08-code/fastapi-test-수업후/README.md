````markdown
# 🎬 영화 리뷰 감성 분석 FastAPI 프로젝트

> **한글 영화 리뷰 텍스트를 입력하면 감성을 분석하고, 결과에 따라 영화 포스터를 추천해 주는 웹 서비스**  
> FastAPI + Jinja2 템플릿 + 브라우저(HTML/JS) 기반으로 동작하며, 사전에 학습된 감성 분석 모델과 TF-IDF 벡터라이저를 사용합니다.

---

## 1. 프로젝트 개요

- **프로젝트 이름**: 영화 리뷰 감성 분석기 (FastAPI 기반)
- **주요 기능**
  - 사용자가 웹 화면에서 영화 리뷰(한글 문장)를 입력
  - 서버에서 텍스트 전처리 → 형태소 분석(Okt) → TF-IDF 변환 → 감성 모델 예측
  - 결과가 부정 / 긍정인지 판별
  - 감성에 맞는 영화 목록 중 하나를 랜덤 추천
  - 추천 영화의 **제목 + 포스터 이미지 URL**을 웹 페이지에 표시

- **특징**
  - 백엔드는 **FastAPI**, 프론트엔드는 **Jinja2 템플릿 + Bootstrap + Axios**를 사용
  - 감성 분석에는 사전에 학습해 둔
    - `movie_tfidf_vectorizer.joblib`
    - `movie_sentiment_model.joblib`
    를 로드해서 사용
  - 한국어 처리를 위해 **KoNLPy의 Okt** 형태소 분석기를 사용

---

## 2. 디렉터리 구조

압축 파일 기준 주요 폴더/파일 구조는 다음과 같습니다.

```bash
fastapi-test/
├─ main.py                     # FastAPI 엔트리 포인트
├─ ai.py                       # 감성 분석 및 영화 추천 핵심 로직
├─ requirements.txt            # 프로젝트 의존성 목록
├─ movie_tfidf_vectorizer.joblib   # TF-IDF 벡터라이저 (사전 학습)
├─ movie_sentiment_model.joblib    # 감성 분석 모델 (사전 학습)
├─ templates/
│  └─ ai.html                  # 메인 화면(HTML 템플릿)
├─ static/                     # (정적 파일 위치, 필요 시 사용)
├─ .venv1/                     # 로컬 가상환경(저장되어 있으나 일반적으로는 새로 만드는 것을 권장)
└─ 기타 IDE/캐시 파일(.idea, __pycache__ 등)
````

> 실제 버전 관리(GitHub 등)에 올릴 때는 `.venv1/`, `__pycache__/`, `.idea/` 등은 보통 `.gitignore`로 제외합니다.

예시 `.gitignore`:

```gitignore
.venv/
.venv1/
__pycache__/
.idea/
*.pyc
```

---

## 3. 주요 파일 설명

### 3.1 `main.py` – FastAPI 엔드포인트 정의

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import ai

app = FastAPI()
# templates 폴더 지정
templates = Jinja2Templates(directory="templates")

@app.get("/")
def ai_html(request: Request):
    return templates.TemplateResponse("ai.html", {"request": request})


@app.get("/ai/{reply}")
def read_ai(reply : str):
    result = ai.ai_run(reply)
    return {"result" : result}
```

* `app = FastAPI()`

  * FastAPI 애플리케이션 인스턴스를 생성합니다.
* `templates = Jinja2Templates(directory="templates")`

  * `templates/` 폴더 아래 HTML 파일을 템플릿으로 사용하도록 설정합니다.
* `GET /`

  * `ai.html` 템플릿을 렌더링하여 브라우저에 메인 화면을 보여 줍니다.
* `GET /ai/{reply}`

  * 경로 파라미터 `reply`로 영화 리뷰 텍스트(문장)를 전달받습니다.
  * `ai.ai_run(reply)`를 호출해 감성 분석 및 영화 추천을 수행합니다.
  * 결과를 JSON 형태(`{"result": {...}}`)로 반환합니다.

---

### 3.2 `ai.py` – 감성 분석 및 영화 추천 로직

핵심 구조 요약:

```python
from konlpy.tag import Okt
import re
import joblib
import random  # 랜덤 추천용

okt = Okt()

NEGATIVE_RECOMMENDATIONS = [
    {"title": "...", "poster_url": "..."},
    ...
]

POSITIVE_RECOMMENDATIONS = [
    {"title": "...", "poster_url": "..."},
    ...
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

    # 2) Okt로 형태소 분석 후 문자열로 변환
    tokenized_str = okt_tokenize_to_str(clean)

    # 3) TF-IDF 변환
    X = tfidf.transform([tokenized_str])

    # 4) 감성 예측
    pred = int(sentiment_model.predict(X)[0])

    if pred == 0:
        label = "부정 감성"
        movie = random.choice(NEGATIVE_RECOMMENDATIONS)
    else:
        label = "긍정 감성"
        movie = random.choice(POSITIVE_RECOMMENDATIONS)

    print(clean, "->>", label)
    return movie

if __name__ == "__main__":
    st = "완전 ^o^ 짜증 잔뜩. 재미없어100%! ^^*"
    print(ai_run(st))
```

#### 로직 흐름

1. **추천 리스트 정의**

   * `NEGATIVE_RECOMMENDATIONS`: 부정 감성일 때 추천할 영화 목록
   * `POSITIVE_RECOMMENDATIONS`: 긍정 감성일 때 추천할 영화 목록
   * 각각 `{"title": "...", "poster_url": "..."}` 구조의 딕셔너리 리스트입니다.

2. **형태소 분석 함수**

   * `okt_tokenize_to_str(text: str)`

     * KoNLPy의 `Okt` 형태소 분석기로 문장을 토큰화 (`okt.morphs(text)`)
     * 결과 리스트를 `" ".join(morphs)`로 이어서 하나의 문자열로 만듭니다.
     * TF-IDF 학습 단계와 동일한 전처리를 재현하는 역할입니다.

3. **모델 로드**

   * `tfidf = joblib.load('movie_tfidf_vectorizer.joblib')`
   * `sentiment_model = joblib.load('movie_sentiment_model.joblib')`
   * 프로젝트 루트에 있는 `.joblib` 파일을 로드해, 학습된 벡터라이저와 분류 모델을 메모리에 적재합니다.

4. **`ai_run` 함수**

   * 입력: 문자열 `text`
   * 처리 단계

     1. 정규표현식으로 한글/공백만 남기고 나머지 문자 제거

        ```python
        clean = re.sub(r'[^ ㄱ-ㅎ가-힣]+', " ", text)
        ```
     2. `okt_tokenize_to_str(clean)` 호출 → 형태소 분석 문자열 생성
     3. `tfidf.transform([tokenized_str])`로 벡터화
     4. `sentiment_model.predict(X)[0]`으로 감성 예측 (0/1)
     5. 예측 결과에 따라

        * `0`: 부정 감성 → `NEGATIVE_RECOMMENDATIONS`에서 하나를 랜덤 선택
        * `1`: 긍정 감성 → `POSITIVE_RECOMMENDATIONS`에서 하나를 랜덤 선택
   * 반환값:

     * `{"title": "...", "poster_url": "..."}` 형태의 딕셔너리

---

### 3.3 `templates/ai.html` – 웹 화면(프론트엔드)

주요 구성:

* **Bootstrap 5**를 이용한 기본 디자인
* **textarea**로 리뷰 입력
* **버튼**으로 감성 분석 요청
* 결과 영역에 **영화 제목 + 포스터 이미지**를 표시
* **Axios**로 FastAPI 백엔드에 AJAX 요청

핵심 부분 요약:

```html
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>영화 리뷰 감성 분석기</title>

    <!-- Bootstrap 5 CSS -->
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
        ...
    >
    <!-- axios -->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

    <style>
        body { padding: 20px; }
        .result-area {
            min-height: 60px;
            background-color: #f5f5f5;
            color: red;
            ...
        }
    </style>
</head>
<body class="container">

<h1 class="mb-4">영화 리뷰 감성 분석기</h1>

<!-- 리뷰 입력 영역 -->
<textarea id="reviewInput" class="form-control" rows="4"
          placeholder="영화 리뷰를 입력해주세요."></textarea>

<div class="d-flex align-items-center gap-3 mb-3">
    <button id="analyzeBtn" class="btn btn-primary">
        감성 분석하기
    </button>
</div>

<!-- 결과 영역 -->
<h2 class="h6 mb-2">분석 결과</h2>
<div id="resultArea" class="result-area badge-light">
    <p id="resultMessage" class="mb-1 text-muted">
        아직 분석 결과가 없습니다. 위에 리뷰를 입력하고 버튼을 눌러 주세요.
    </p>
    <div style="background: lime; height: 200px; width: 100%;">
        <span id="resultBadge"
              style="background: red; height: 100px; width: 100%; color: white;"></span>
    </div>
</div>

<script>
const analyzeBtn    = document.getElementById("analyzeBtn");
const reviewInput   = document.getElementById("reviewInput");
const resultMessage = document.getElementById("resultMessage");
const resultBadge   = document.getElementById("resultBadge");

analyzeBtn.addEventListener("click", async () => {
    const text = reviewInput.value.trim();
    if (!text) {
        resultMessage.textContent = "리뷰를 먼저 입력해 주세요.";
        return;
    }

    try {
        // 리뷰 문자열을 경로 파라미터로 전달 (인코딩 필요)
        const encoded = encodeURIComponent(text);

        const response = await axios.get(`/ai/${encoded}`);
        const data = response.data;  // { result: { title, poster_url } }

        resultMessage.textContent =
            "입력한 문장: " + text;
        resultBadge.innerHTML =
            data.result.title +
            "<br><img width=700 height=450 src=" + data.result.poster_url + ">";
    } catch (error) {
        console.error(error);
        resultMessage.textContent = "요청 실패";
    }
});
</script>

</body>
</html>
```

#### 프론트엔드 동작 흐름

1. 사용자가 textarea에 리뷰를 입력하고 `감성 분석하기` 버튼 클릭
2. JavaScript에서 입력값을 읽고 `encodeURIComponent`로 인코딩
3. `axios.get("/ai/" + 인코딩된_문자열)` 호출
4. FastAPI에서 `/ai/{reply}`가 호출되어 감성 분석 수행
5. 응답으로 받은 `data.result.title`, `data.result.poster_url`를 화면에 표시

---

## 4. 설치 및 실행 방법

### 4.1 파이썬 가상환경 준비

프로젝트 루트(`fastapi-test/`) 기준:

```bash
cd fastapi-test

# 가상환경 생성 (예: venv)
python -m venv .venv

# 가상환경 활성화 (OS에 따라 명령어 다름)
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

이미 압축 안에 `.venv1/` 폴더가 들어 있지만, 환경이 다른 PC에서는 그대로 쓰면 문제가 생길 수 있으므로
**새로 가상환경을 만들고 `requirements.txt`로 설치하는 방식**을 권장합니다.

### 4.2 의존성 설치

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

`requirements.txt` 내용:

```text
fastapi
uvicorn[standard]

pandas
scikit-learn
joblib

konlpy
JPype1

jinja2
python-multipart
```

### 4.3 Java / KoNLPy (Okt) 환경

`konlpy` + `JPype1`을 사용하므로, 시스템에 **JDK(Java)** 가 설치되어 있어야 합니다.

* Windows:

  * JDK 설치 후, `JAVA_HOME` 환경변수 및 `PATH` 설정 필요
* macOS / Linux:

  * `apt` / `brew` 등을 이용해 `openjdk` 설치 후 `JAVA_HOME` 확인

예시(리눅스):

```bash
sudo apt-get update
sudo apt-get install -y openjdk-11-jdk

echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> ~/.bashrc
echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
```

이후 `python -c "from konlpy.tag import Okt; print(Okt().morphs('테스트'))"`가 정상 실행되면 준비 완료입니다.

---

## 5. 서버 실행 방법

### 5.1 Uvicorn으로 로컬 실행

프로젝트 루트(`fastapi-test/`)에서:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

* `main:app`

  * `main.py` 파일의 `app` 객체를 의미합니다.
* `--reload`

  * 코드 변경 시 서버를 자동으로 재시작해 개발 편의를 높여줍니다.
* `--host 0.0.0.0`

  * 외부 접속도 허용 (로컬에서만 쓸 거면 생략해도 무방)
* `--port 8000`

  * 기본 포트 8000 사용 (필요 시 다른 포트 지정 가능)

### 5.2 브라우저에서 접속

Uvicorn을 성공적으로 실행한 후, 웹 브라우저에서 다음 주소로 접속합니다.

```text
http://127.0.0.1:8000/
```

또는 `http://localhost:8000/`

---

## 6. API 명세

### 6.1 `GET /` – 메인 페이지

* **URL**: `/`
* **Method**: `GET`
* **설명**: 영화 리뷰 감성 분석 입력 화면(HTML)을 반환합니다.
* **응답**: `templates/ai.html` 렌더링 결과 (HTML)

---

### 6.2 `GET /ai/{reply}` – 감성 분석 및 영화 추천

* **URL**: `/ai/{reply}`
* **Method**: `GET`
* **경로 파라미터**

  * `reply` (string): 감성 분석 대상이 되는 한글 리뷰 문장 (URL 인코딩된 상태)
* **처리**

  1. `ai.ai_run(reply)` 호출
  2. 텍스트 전처리, 형태소 분석, TF-IDF 변환, 감성 모델 예측 수행
  3. 부정/긍정에 따라 영화 하나를 랜덤 선택
* **응답 형식 (JSON)**

예시:

```json
{
  "result": {
    "title": "인사이드 아웃 (Inside Out, 2015)",
    "poster_url": "https://upload.wikimedia.org/wikipedia/sco/0/0a/Inside_Out_%282015_film%29_poster.jpg"
  }
}
```

* 프론트엔드에서는 `data.result.title`, `data.result.poster_url`를 사용해서 화면에 출력합니다.

---

## 7. 동작 전체 흐름 정리

1. 사용자가 브라우저에서 `http://localhost:8000/` 접속
2. `main.py`의 `GET /` 엔드포인트가 실행되어 `ai.html` 반환
3. 사용자:

   * textarea에 영화 리뷰 입력
   * `감성 분석하기` 버튼 클릭
4. 브라우저(JavaScript):

   * 입력 텍스트를 읽어 `encodeURIComponent` 적용
   * `axios.get("/ai/" + 인코딩된_리뷰)`로 FastAPI 서버에 요청
5. FastAPI (`main.py`):

   * `/ai/{reply}` 엔드포인트에서 `ai.ai_run(reply)` 호출
6. `ai.py`:

   * 정규표현식으로 특수문자 제거
   * Okt 형태소 분석으로 토큰화 후 문자열로 합침
   * TF-IDF 변환
   * 감성 모델로 0/1 예측
   * 예측 결과에 따라 부정/긍정 영화 리스트에서 랜덤 선택
   * 영화 정보 딕셔너리 반환
7. FastAPI:

   * `{"result": 영화정보}` JSON으로 브라우저에 응답
8. 브라우저(JavaScript):

   * 응답 데이터를 파싱
   * 결과 문장, 추천 영화 제목, 포스터 이미지를 페이지에 표시

---

## 8. 요약 표

마지막으로, 위 내용을 한 번에 볼 수 있도록 표로 정리하면 다음과 같습니다.

| 구분              | 내용                                                                                                   |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| 프로젝트 목적         | 영화 리뷰 텍스트의 감성을 분석하고, 결과에 따라 영화 포스터를 추천하는 웹 서비스                                                       |
| 주요 기술 스택        | FastAPI, Uvicorn, Jinja2 템플릿, Bootstrap, Axios, KoNLPy(Okt), scikit-learn, joblib                    |
| 핵심 파이썬 파일       | `main.py` (API 엔드포인트), `ai.py` (전처리 + 감성 분석 + 영화 추천 로직)                                              |
| 템플릿 파일          | `templates/ai.html` – 리뷰 입력 UI, 버튼, 결과 표시 영역 포함                                                      |
| 모델 파일           | `movie_tfidf_vectorizer.joblib` (TF-IDF 벡터라이저), `movie_sentiment_model.joblib` (감성 분류 모델)            |
| 주요 엔드포인트        | `GET /` → HTML 페이지 반환, `GET /ai/{reply}` → 감성 분석 결과 및 영화 추천 반환(JSON)                                 |
| 입력 형식           | 브라우저에서 textarea로 한글 리뷰 입력, JS에서 `/ai/{인코딩된_리뷰}`로 GET 요청                                              |
| 출력 형식           | `{ "result": { "title": "...", "poster_url": "..." } }` 형태의 JSON 응답                                  |
| 텍스트 처리          | 정규표현식으로 특수문자 제거 → Okt 형태소 분석 → 공백 구분 토큰 문자열 생성                                                       |
| 감성 분석 과정        | TF-IDF 변환 → 사전 학습 모델로 0/1 예측 → 부정/긍정 영화 리스트에서 랜덤 추천                                                  |
| 실행 방법           | 가상환경 생성 → `pip install -r requirements.txt` → `uvicorn main:app --reload --host 0.0.0.0 --port 8000` |
| 접속 주소           | 기본: `http://127.0.0.1:8000/` 또는 `http://localhost:8000/`                                             |
| Java/Konlpy 의존성 | 시스템에 JDK 설치 및 `konlpy`, `JPype1` 설치 필요, `JAVA_HOME` 설정 권장                                            |


