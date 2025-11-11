
````markdown
# 🐍 Python Data Repository — 전체 통합 README

---

## 🧭 목차 (Table of Contents)

1. [📘 개요](#-개요)
2. [🚀 빠른 시작](#-빠른-시작)
3. [📂 폴더 개요](#-폴더-개요)
4. [🧠 00-이미지인식](#-00-이미지인식)
5. [🌐 WebDriver](#-webdriver)
6. [💬 chatbot](#-chatbot)
7. [📊 csv-data](#-csv-data)
8. [📁 data01~data21](#-data01data21)
9. [🖋 nanum](#-nanum)
10. [📝 note1](#-note1)
11. [📓 notebook-2](#-notebook-2)
12. [📚 pandas-start](#-pandas-start)
13. [💻 pc2](#-pc2)
14. [🌍 site](#-site)
15. [🧾 요약표](#-요약표)
16. [✅ 공통 체크리스트](#-공통-체크리스트)
17. [📄 License](#-license)

---

## 📘 개요

`python-data`는 **파이썬 데이터 분석, 웹 자동화, 이미지 인식, 챗봇, 판다스 실습용 예제**를 한데 모은 교육용 레포지토리입니다.  
각 폴더는 독립된 실습 단위로 구성되어 있으며, 실제 수업·자율학습 환경에서 재활용 가능하도록 제작되었습니다.

---

## 🚀 빠른 시작

```bash
git clone https://github.com/newbackjava/python-data.git
cd python-data

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -U pip setuptools wheel
pip install pandas numpy matplotlib seaborn scikit-learn selenium opencv-python jupyter
````

---

## 📂 폴더 개요

| 📁 폴더명                          | 🔍 분류       | 🧩 주요 내용             | 💡 권장 패키지                       |
| :------------------------------ | :---------- | :------------------- | :------------------------------ |
| [00-이미지인식](#-00-이미지인식)          | 컴퓨터 비전      | OpenCV 이미지 처리, 객체 탐지 | `opencv-python`, `numpy`        |
| [WebDriver](#-webdriver)        | 웹 자동화       | Selenium 크롬 드라이버 제어  | `selenium`, `webdriver-manager` |
| [chatbot](#-chatbot)            | 대화형 AI      | 규칙 기반/ML 기반 챗봇       | `pandas`, `scikit-learn`        |
| [csv-data](#-csv-data)          | 데이터 변환      | JSON ↔ CSV 변환        | `pandas`, `pyarrow`             |
| [data01~data21](#-data01data21) | 데이터 실습      | EDA, 시각화, 통계분석       | `pandas`, `matplotlib`          |
| [nanum](#-nanum)                | 폰트          | 그래프 한글 폰트 설정         | -                               |
| [note1](#-note1)                | 수업 노트       | 실습 코드 메모             | -                               |
| [notebook-2](#-notebook-2)      | Jupyter 노트북 | 분석, 시각화, 모델링         | `jupyterlab`, `pandas`          |
| [pandas-start](#-pandas-start)  | 판다스 기초      | DataFrame 문법 예제      | `pandas`                        |
| [pc2](#-pc2)                    | 실습 파트2      | 중급 파이썬 문법            | -                               |
| [site](#-site)                  | 정적 리소스      | HTML 튜토리얼, 예시 페이지    | -                               |

---

## 🧠 00-이미지인식

📸 **OpenCV 기반 이미지 인식/처리 실습 폴더**

```bash
pip install opencv-python numpy matplotlib scikit-image
```

```python
import cv2
img = cv2.imread('images/sample.jpg')
print(img.shape if img is not None else "이미지 경로를 확인하세요.")
```

✅ **체크리스트**

* [ ] 이미지 파일 경로 확인
* [ ] GPU/CUDA 환경 점검
* [ ] 모델/데이터 라이선스 명시

---

## 🌐 WebDriver

🕹️ **Selenium을 활용한 웹 자동화 실습 폴더**

```bash
pip install selenium webdriver-manager
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

✅ **체크리스트**

* [ ] 브라우저/드라이버 버전 일치
* [ ] Headless 모드 옵션 확인

---

## 💬 chatbot

🤖 **규칙 기반 및 머신러닝 기반 챗봇 예제**

```bash
pip install numpy pandas scikit-learn
```

```python
def reply(text):
    rules = { "안녕": "안녕하세요!", "bye": "또 봐요!" }
    for k, v in rules.items():
        if k in text.lower():
            return v
    return "무슨 뜻인지 잘 모르겠어요."

print(reply("안녕"))
```

✅ **체크리스트**

* [ ] Intent / Response 데이터 구조 확인
* [ ] 모델 학습 코드 포함 여부 점검

---

## 📊 csv-data

🗂️ **CSV 파일 입출력, JSON 변환, 구분자 실습 폴더**

```bash
pip install pandas pyarrow
```

```python
import pandas as pd
df = pd.read_json('sample.json')
df.to_csv('sample.csv', index=False, encoding='utf-8')
```

✅ **체크리스트**

* [ ] 구분자(`,`/`;`/`\t`) 확인
* [ ] UTF-8 / CP949 인코딩 점검

---

## 📁 data01~data21

📈 **EDA 및 시각화 실습용 데이터 폴더**

```python
import pandas as pd
df = pd.read_csv('data/sample.csv', encoding='utf-8')
print(df.head())
```

📌 **전처리 팁**

* `df.columns = df.columns.str.strip()`
* `parse_dates=['날짜']`
* `df.fillna()` / `df.dropna()`

✅ **체크리스트**

* [ ] 데이터 파일 경로 확인
* [ ] 결과물(outputs/) 폴더 구성

---

## 🖋 nanum

🖼️ **한글 폰트 깨짐 방지를 위한 폴더**

```python
import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams

font_manager.fontManager.addfont('nanum/NanumGothic.ttf')
rcParams['font.family'] = 'NanumGothic'

plt.title("한글 폰트 테스트")
plt.plot([1,2,3])
plt.show()
```

✅ **체크리스트**

* [ ] 폰트 파일 경로 확인
* [ ] 라이선스 포함

---

## 📝 note1

📒 **수업 노트 및 코드 정리용 폴더**
간단한 스크립트, 테스트 코드, 강의 요약 등이 포함됩니다.

---

## 📓 notebook-2

📚 **Jupyter 기반 데이터 분석 노트북 폴더**

```bash
pip install jupyterlab ipywidgets pandas matplotlib
jupyter lab
```

✅ **체크리스트**

* [ ] 커널 환경(Python 3.x) 명시
* [ ] 데이터 파일 상대 경로 확인

---

## 📚 pandas-start

🧩 **Pandas 기초 문법 실습**

```python
import pandas as pd
s = pd.Series([1, 2, 3], name="s")
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
print(df.describe())
```

✅ **체크리스트**

* [ ] DataFrame 생성/조작 예제 확인
* [ ] groupby, merge, pivot 실습 포함

---

## 💻 pc2

🧠 **중급 파이썬 실습용 폴더**
파일 입출력, 클래스, 예외 처리, 함수형 프로그래밍 등을 다룹니다.

✅ **체크리스트**

* [ ] 실행 가능한 `.py` 스크립트 포함
* [ ] 모듈 의존성 확인

---

## 🌍 site

🌐 **정적 HTML 튜토리얼 / 예시 페이지 폴더**

```bash
python -m http.server 8000
# http://localhost:8000
```

✅ **체크리스트**

* [ ] CSS/JS 상대경로 확인
* [ ] 이미지·폰트 라이선스 명시

---

## 🧾 요약표

| 폴더           | 주제             | 핵심 패키지                 |
| ------------ | -------------- | ---------------------- |
| 00-이미지인식     | OpenCV, 딥러닝 예제 | `opencv-python`        |
| WebDriver    | 웹 자동화, 크롤링     | `selenium`             |
| chatbot      | 규칙 기반/ML 챗봇    | `scikit-learn`         |
| csv-data     | 데이터 변환         | `pandas`               |
| data01~21    | 분석/시각화 실습      | `pandas`, `matplotlib` |
| nanum        | 폰트 설정          | -                      |
| note1        | 수업 노트          | -                      |
| notebook-2   | Jupyter 노트북    | `jupyterlab`           |
| pandas-start | 판다스 기초         | `pandas`               |
| pc2          | 고급 파이썬         | -                      |
| site         | HTML 자료        | -                      |

---

## ✅ 공통 체크리스트

* [ ] 인코딩(UTF-8/CP949) 일관성 유지
* [ ] 경로 오류 없는지 확인
* [ ] 데이터 출처 및 저작권 명시
* [ ] Python 3.9 이상 환경 사용
* [ ] `requirements.txt` 최신화

---

## 📄 License

본 저장소는 **교육 및 학습 목적**으로만 사용됩니다.
모든 외부 데이터 및 예제의 저작권은 각 원저자에게 귀속됩니다.

---

⭐ **Tip:** 각 폴더 내부에 개별 README가 필요할 경우,
본 문서의 해당 섹션을 복사해 `README.md`로 저장하면 자동으로 목차 링크가 연결됩니다.

```

---


