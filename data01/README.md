
# Data01 - Python 웹 크롤링 & 데이터 수집 실습

`data01` 폴더는 **Python을 이용한 웹 크롤링·데이터 수집 연습용 Jupyter Notebook** 모음이다.  
실습을 통해 다음과 같은 내용을 다룬다.

- `urllib.request`로 웹 페이지 요청 보내기
- `BeautifulSoup`으로 HTML 파싱하고 원하는 태그/텍스트 추출하기
- 포털/쇼핑몰/금융 사이트의 메뉴·가격 정보 가져오기
- 크롤링 코드 구조 연습 및 테스트

> 이 자료는 **교육·학습용**으로만 사용하며, 실제 서비스에 대한 과도한 요청·상업적 이용은 지양한다.

---

## 폴더 구조

```

data01/
├── 0-daum-main-menu.ipynb     # 다음(daum) 메인 메뉴 구조 크롤링 연습
├── 1-hottrack-main-menu.ipynb # 교보문고 핫트랙스 메인 페이지 크롤링 연습
├── 2-naver-finance.ipynb      # 네이버 금융 종목 정보 크롤링 연습
├── test01.ipynb               # 크롤링/파이썬 문법 테스트 노트북 1
├── test02.ipynb               # 크롤링/파이썬 문법 테스트 노트북 2
├── test3.ipynb                # 크롤링 결과 가공/출력 테스트 노트북
├── README.md                  # 이 파일
└── .ipynb_checkpoints/        # Jupyter 자동 백업 파일(실습 시 무시해도 됨)

````

각 노트북은 크게 **요청 → 파싱 → 데이터 추출 → 출력** 흐름으로 구성되어 있으며,  
필요한 코드는 셀 단위로 단계별로 실습할 수 있게 작성되어 있다.   

---

## 각 노트북 설명

### 0. `0-daum-main-menu.ipynb` – Daum 메인 메뉴 크롤링

- `https://top.cafe.daum.net/` 등 Daum 페이지에 접속하여 HTTP 응답 코드와 HTML 구조 확인
- `BeautifulSoup`으로 전체 문서 파싱 후
  - 메인 메뉴/링크 목록 추출
  - 특정 태그(`a`, `li`, `div` 등)의 텍스트와 속성(`href`) 가져오기 연습
- `con.status`, `doc.prettify()` 등을 이용해
  - 응답 상태 코드,
  - HTML 포맷 확인 방법을 연습한다.

---

### 1. `1-hottrack-main-menu.ipynb` – 핫트랙스 메인 크롤링

- `https://hottracks.kyobobook.co.kr/` 메인 페이지를 대상으로 크롤링 실습
- 주요 내용
  - `request.urlopen()`으로 페이지 요청 및 응답 확인
  - `BeautifulSoup('html.parser')`로 문서 파싱
  - 메인 페이지에서
    - 메뉴 이름,
    - 상품/카테고리 영역의 텍스트 일부를 추출하는 연습
- 자바스크립트가 섞인 쇼핑몰 페이지에서 **정적 HTML로 보이는 부분만 어떻게 추출할 수 있는지** 감을 잡기 위한 예제이다.

---

### 2. `2-naver-finance.ipynb` – 네이버 금융 종목 정보 크롤링

- `https://finance.naver.com/item/main.naver?code=...` 구조를 이용해
  - 특정 종목 코드(예: 삼성전자, 현대차 등)의 상세 페이지를 요청
  - 회사 이름, 오늘가, 전일가, 고가 등 숫자 데이터 추출

- 주요 학습 포인트
  - CSS 선택자 사용 예:
    - 회사명: `.wrap_company > h2 > a`
    - 오늘가: `div.today span.blind`
    - 시가/고가: `td.first span.blind`
  - 문자열 전처리
    - 쉼표(,)가 들어간 가격 문자열 → `split(',')` → `join()` → `int()` 변환
  - 여러 종목 코드를 리스트(`code_list`)에 넣고 **반복문으로 한꺼번에 수집**하는 패턴
  - 수집한 결과를 리스트/표 형태로 정리하여 DataFrame·CSV로 확장 가능

---

### 3. `test01.ipynb`, `test02.ipynb`, `test3.ipynb` – 테스트/연습 노트북

- 공통적으로 다음 내용을 가볍게 연습하는 데 사용된다.
  - `urllib.request` 기본 사용법
  - `BeautifulSoup` 선택자 실험
  - 크롤링한 텍스트 출력 형식/정리 방식 테스트
- 실험용 코드가 포함되어 있으므로,
  - 자유롭게 수정하면서 **직접 크롤링 패턴을 연습하는 공간**으로 사용하면 된다.

---

## 필요한 환경

### Python & 패키지

- 권장 Python 버전: **3.9+**
- 필수 패키지:
  - `beautifulsoup4`
  - `lxml` (선택이지만 HTML 파싱 속도/안정성 향상)
  - `requests` (추가로 연습하고 싶을 때)
  - `jupyter` or `jupyterlab`

```bash
pip install beautifulsoup4 lxml requests jupyter
````

---

## 활용 방법

* **웹 구조 탐색 연습**

  * HTML 문서 구조를 실제로 찍어 보고 (`doc.prettify()`),
  * 필요한 태그만 골라내는 과정에 집중한다.
* **정적 페이지 vs 동적 페이지 감 구분**

  * Daum, 네이버 금융, 핫트랙스 등 서로 다른 유형의 사이트를 크롤링하면서
  * 어디까지가 `requests/BeautifulSoup`만으로 가능한지 체감할 수 있다.
* **데이터 후처리 연습**

  * 가격, 숫자, 텍스트를 파이썬 기본 문법으로 정리하고,
  * 이후 `pandas` DataFrame으로 확장하여 csv로 저장하는 연습까지 이어갈 수 있다.

---

## 주의사항 (크롤링 에티켓)

* 사이트의 **robots.txt, 이용약관**을 항상 확인하고, 허용된 범위 내에서만 수집한다.
* 짧은 시간에 너무 많은 요청을 보내지 않는다. (학습용으로 간단히 실행하는 수준 권장)
* 수집한 데이터는 **개인 학습용**으로만 사용하고, 상업적 서비스나 대량 배포에는 사용하지 않는다.

---

## 요약 표

| 파일명                          | 유형       | 주요 내용/역할                              |
| ---------------------------- | -------- | ------------------------------------- |
| `0-daum-main-menu.ipynb`     | Notebook | Daum 페이지 응답 코드 확인, HTML 구조 파악, 메뉴 크롤링 |
| `1-hottrack-main-menu.ipynb` | Notebook | 핫트랙스 메인 페이지 구조 탐색, 메뉴·텍스트 크롤링 연습      |
| `2-naver-finance.ipynb`      | Notebook | 네이버 금융 종목 상세에서 회사명·가격 정보 추출           |
| `test01.ipynb`               | Notebook | 크롤링 및 파이썬 기본 실험용                      |
| `test02.ipynb`               | Notebook | 크롤링 코드/선택자 테스트                        |
| `test3.ipynb`                | Notebook | 크롤링 결과 가공·출력·테스트용                     |
| `.ipynb_checkpoints/`        | 폴더       | Jupyter 자동 백업 파일 (실습 시 직접 수정할 필요 없음)  |



