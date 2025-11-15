# Data02 - Python 데이터 분석 실습 자료

이 저장소는 **Python 데이터 분석 실습**을 위한 샘플 데이터셋과 예제 스크립트를 제공한다.  
`data02` 디렉토리 안 데이터는 교육·학습용으로 구성했다.

---

## 디렉토리 구조

```
data02/
├── sales_data.csv          # 가상 쇼핑몰 매출 데이터 (2019년)
├── customer_info.xlsx      # 고객 정보 (이름, 나이, 지역, 가입일)
├── product_catalog.json    # 상품 카탈로그 (상품ID, 이름, 카테고리, 가격)
├── survey_responses.csv    # 고객 만족도 설문 응답 데이터
├── images/
│   ├── chart_example.png   # 예제 시각화 이미지
│   └── dashboard_mockup.jpg
└── scripts/
    ├── data_cleaning.py    # 데이터 전처리 예제
    ├── analysis.ipynb      # Jupyter Notebook 분석 예제
    └── visualization.py    # Matplotlib/Seaborn 시각화 스크립트
```

---

## 데이터 설명

| 파일명 | 형식 | 설명 | 주요 컬럼 |
|--------|------|------|----------|
| `sales_data.csv` | CSV | 2019년 가상 쇼핑몰 일별 매출 | `date`, `product_id`, `quantity`, `revenue`, `customer_id` |
| `customer_info.xlsx` | Excel | 고객 기본 정보 | `customer_id`, `name`, `age`, `region`, `join_date` |
| `product_catalog.json` | JSON | 상품 정보 | `product_id`, `name`, `category`, `price`, `stock` |
| `survey_responses.csv` | CSV | 고객 만족도 설문 | `customer_id`, `q1 ~ q5`, `comment`, `timestamp` |

---

## 시작하기

### 1. 저장소 클론
```bash
git clone https://github.com/newbackjava/python-data.git
cd python-data/data02
```

### 2. 필요 패키지 설치
```bash
pip install pandas matplotlib seaborn openpyxl jupyter
```

### 3. 예제 노트북 실행
```bash
jupyter notebook scripts/analysis.ipynb
```

---

## 활용 예시

- **매출 추이 분석** → `sales_data.csv` + `visualization.py`
- **고객 세그먼트 분석** → `customer_info.xlsx` + `sales_data.csv` 조인
- **NPS 계산 및 시각화** → `survey_responses.csv`
```






<img width="1035" height="944" alt="스크린샷 2025-11-13 22 47 36" src="https://github.com/user-attachments/assets/0b4cc251-9f9e-4c5f-bafc-285a4aa5974b" />
<img width="1050" height="1129" alt="스크린샷 2025-11-13 22 47 52" src="https://github.com/user-attachments/assets/dc786135-437e-44ce-bfc4-11946ac96429" />
<img width="1050" height="1129" alt="스크린샷 2025-11-13 22 48 05" src="https://github.com/user-attachments/assets/ba502fa0-bd06-4de7-ae70-faa66535cffb" />
<img width="1050" height="1129" alt="스크린샷 2025-11-13 22 48 20" src="https://github.com/user-attachments/assets/e035c54e-a035-415b-99b3-403881f9dc63" />
<img width="1050" height="774" alt="스크린샷 2025-11-13 22 49 17" src="https://github.com/user-attachments/assets/002eef23-78af-444b-b138-15673772b57c" />

