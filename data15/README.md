
# Data15 - Python 데이터 분석 실습 자료

이 저장소는 **Python 데이터 분석 실습**을 위한 샘플 데이터셋과 예제 스크립트를 제공한다.  
`data15` 디렉토리 안 데이터는 교육·학습용으로 구성했다.

---

## 디렉토리 구조

```
data15/
├── sales_data.csv          # 가상 쇼핑몰 매출 데이터 (2032년)
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
| `sales_data.csv` | CSV | 2032년 가상 쇼핑몰 일별 매출 | `date`, `product_id`, `quantity`, `revenue`, `customer_id` |
| `customer_info.xlsx` | Excel | 고객 기본 정보 | `customer_id`, `name`, `age`, `region`, `join_date` |
| `product_catalog.json` | JSON | 상품 정보 | `product_id`, `name`, `category`, `price`, `stock` |
| `survey_responses.csv` | CSV | 고객 만족도 설문 | `customer_id`, `q1 ~ q5`, `comment`, `timestamp` |

---

## 활용 예시

- **매출 추이 분석** → `sales_data.csv` + `visualization.py`
- **고객 세그먼트 분석** → `customer_info.xlsx` + `sales_data.csv` 조인
- **NPS 계산 및 시각화** → `survey_responses.csv`
```
