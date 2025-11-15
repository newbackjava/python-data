
## data01: 기본 데이터 분석 입문
이 폴더는 Python 데이터 분석의 기초를 다지는 데 초점을 맞춥니다. 사용자 정보와 판매 기록을 통해 간단한 통계 분석을 실습합니다.

### 디렉토리 구조
```
data01/
├── data/
│   ├── dataset1.csv          # 사용자 정보: 1000행, 컬럼 - user_id (고유 ID), age (20-60세), gender (M/F), purchase_history (총 구매 횟수, 0-50)
│   └── dataset2.csv          # 판매 기록: 5000행, 컬럼 - product_id (상품 ID), quantity (수량, 1-10), sale_date (YYYY-MM-DD 형식), revenue (매출액, 1000-50000원)
└── scripts/
    ├── data_cleaning.py      # 결측값 처리 (fillna), 이상치 제거 (IQR 방법), 데이터 타입 변환 (to_datetime)
    └── basic_analysis.py     # 평균/중앙값 계산 (pandas describe), 상관관계 분석 (corr), 기본 시각화 (matplotlib bar/line plot)
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `dataset1.csv` | CSV | 1000 | `user_id`, `age`, `gender`, `purchase_history` | user_id: U001, age: 25, gender: M, purchase_history: 5 |
| `dataset2.csv` | CSV | 5000 | `product_id`, `quantity`, `sale_date`, `revenue` | product_id: P001, quantity: 2, sale_date: 2018-01-15, revenue: 20000 |

### 활용 예시
- 사용자 연령대별 구매 패턴 분석: `dataset1`과 `dataset2` 조인 후 groupby 사용.
- 매출 추이 그래프: `sale_date` 기준 시계열 플롯.

---

## data02: 중급 데이터 클리닝과 분석
고객 피드백과 마케팅 데이터를 다루며, 데이터 클리닝과 고급 분석을 실습합니다.

### 디렉토리 구조
```
data02/
├── data/
│   ├── dataset3.csv          # 고객 피드백: 2000행, 컬럼 - customer_id (고유 ID), product_satisfaction (1-5점), feedback_text (텍스트 리뷰, 50자 이내)
│   └── dataset4.csv          # 마케팅 캠페인: 1500행, 컬럼 - campaign_id (캠페인 ID), open_rate (개봉률, 0-100%), click_rate (클릭률, 0-50%), conversion (전환 여부, Y/N)
└── scripts/
    ├── advanced_data_cleaning.py  # 중복 제거 (drop_duplicates), 형식 변환 (str.lower), 텍스트 클리닝 (정규표현식)
    ├── advanced_data_analysis.py  # 클러스터링 (KMeans, scikit-learn), 예측 모델 (LinearRegression)
    └── advanced_data_visualization.py  # Seaborn heatmap, boxplot으로 상관/분포 시각화
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `dataset3.csv` | CSV | 2000 | `customer_id`, `product_satisfaction`, `feedback_text` | customer_id: C001, product_satisfaction: 4, feedback_text: "좋은 제품" |
| `dataset4.csv` | CSV | 1500 | `campaign_id`, `open_rate`, `click_rate`, `conversion` | campaign_id: Camp01, open_rate: 45, click_rate: 12, conversion: Y |

### 활용 예시
- 만족도 기반 세그먼테이션: `dataset3`에서 KMeans 클러스터링.
- 캠페인 ROI 계산: `dataset4`에서 conversion 비율 분석 및 히트맵.

---

## data03: 시계열 및 머신러닝 입문
고객 세그먼테이션과 시계열 데이터를 통해 머신러닝 기초를 배웁니다.

### 디렉토리 구조
```
data03/
├── data/
│   ├── dataset5.csv          # 고객 세그먼테이션: 800행, 컬럼 - segment_id (세그먼트 ID), income_level (소득 수준, Low/Mid/High), loyalty_score (1-10점)
│   └── dataset6.csv          # 시계열 판매: 365행, 컬럼 - date (YYYY-MM-DD), daily_sales (일 매출, 50000-200000원), trend_factor (계절성 요인, 0.5-1.5)
└── scripts/
    ├── enhanced_data_cleaning.py  # 결측 보간 (interpolate), 스케일링 (MinMaxScaler)
    ├── machine_learning_analysis.py  # 분류 모델 (DecisionTree), 시계열 예측 (ARIMA)
    └── interactive_visualization.py  # Plotly로 인터랙티브 라인 차트, 대시보드
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `dataset5.csv` | CSV | 800 | `segment_id`, `income_level`, `loyalty_score` | segment_id: S01, income_level: Mid, loyalty_score: 7 |
| `dataset6.csv` | CSV | 365 | `date`, `daily_sales`, `trend_factor` | date: 2020-01-01, daily_sales: 120000, trend_factor: 1.0 |

### 활용 예시
- 세그먼트별 충성도 분석: `dataset5` groupby 및 DecisionTree.
- 판매 예측: `dataset6` ARIMA 모델 적용.

---

## data04: 소셜 미디어와 시장 연구
소셜 미디어 행동과 소비자 선호 데이터를 분석합니다.

### 디렉토리 구조
```
data04/
├── data/
│   ├── dataset7.csv          # 소셜 미디어 행동: 3000행, 컬럼 - user_handle (유저 핸들), post_engagement (좋아요/공유 수, 0-1000), hashtag_usage (해시태그 개수, 0-20)
│   └── dataset8.csv          # 시장 연구: 1200행, 컬럼 - survey_id (설문 ID), preference_score (선호도 1-5), demographic (인구통계, Age/Gender)
└── scripts/
    ├── data_feature_engineering.py  # 피처 추출 (TF-IDF 텍스트), 원-핫 인코딩
    ├── deep_learning_models.py  # 간단한 Neural Network (Keras)로 감성 분석
    └── advanced_visualization.py  # NetworkX 그래프, Folium 지도 시각화
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `dataset7.csv` | CSV | 3000 | `user_handle`, `post_engagement`, `hashtag_usage` | user_handle: @user1, post_engagement: 150, hashtag_usage: 5 |
| `dataset8.csv` | CSV | 1200 | `survey_id`, `preference_score`, `demographic` | survey_id: SUR01, preference_score: 3, demographic: 25-34/F |

### 활용 예시
- engagement 예측: `dataset7` Neural Network.
- 선호도 분포: `dataset8` demographic별 히스토그램.

---

## data05: 재무 데이터 분석
재무 보고서와 주식 데이터를 다루며, 회계 지표 분석을 실습합니다. (이전 패턴 기반 확장)

### 디렉토리 구조
```
data05/
├── data/
│   ├── financial_reports.csv  # 재무 보고: 500행, 컬럼 - company_id (회사 ID), quarter (분기), revenue (매출, 1B-10B), profit_margin (이익률, 5-20%)
│   └── stock_prices.csv       # 주식 가격: 2520행 (1년 거래일), 컬럼 - ticker (티커), date (YYYY-MM-DD), close_price (종가, 10000-50000원), volume (거래량, 1M-10M)
└── scripts/
    ├── financial_cleaning.py   # 이상치 필터링 (Z-score), 날짜 정렬
    ├── ratio_analysis.py       # 재무비율 계산 (ROE, EBITDA), 포트폴리오 최적화 (mean-variance)
    └── stock_viz.py            # 이동평균 (SMA/EMA), 캔들스틱 차트 (mplfinance)
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `financial_reports.csv` | CSV | 500 | `company_id`, `quarter`, `revenue`, `profit_margin` | company_id: COMP01, quarter: Q1-2022, revenue: 5B, profit_margin: 12 |
| `stock_prices.csv` | CSV | 2520 | `ticker`, `date`, `close_price`, `volume` | ticker: AAPL, date: 2022-01-03, close_price: 15000, volume: 5M |

### 활용 예시
- 분기별 수익성 추이: `financial_reports` 라인 플롯.
- 주식 변동성 분석: `stock_prices` 볼린저 밴드.

---

## data06: 의료 데이터 분석
환자 기록과 진단 데이터를 통해 의료 통계를 실습합니다.

### 디렉토리 구조
```
data06/
├── data/
│   ├── patient_records.csv   # 환자 기록: 1500행, 컬럼 - patient_id (환자 ID), age (0-100세), diagnosis (질병 코드, ICD-10), treatment_outcome (성공/실패)
│   └── vital_signs.csv       # 바이탈 사인: 3000행, 컬럼 - measurement_id (측정 ID), heart_rate (심박수, 60-100), blood_pressure (혈압, 90/60-140/90)
└── scripts/
    ├── medical_cleaning.py    # 익명화 (hashing), 범주화 (age bins)
    ├── survival_analysis.py   # Kaplan-Meier 생존 곡선, Cox 회귀
    └── health_viz.py          # 히트맵 (상관), 산점도 (vitals vs outcome)
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `patient_records.csv` | CSV | 1500 | `patient_id`, `age`, `diagnosis`, `treatment_outcome` | patient_id: PAT001, age: 45, diagnosis: E11, treatment_outcome: Success |
| `vital_signs.csv` | CSV | 3000 | `measurement_id`, `heart_rate`, `blood_pressure` | measurement_id: MS001, heart_rate: 72, blood_pressure: 120/80 |

### 활용 예시
- 진단별 성공률: `patient_records` crosstab.
- 바이탈 트렌드: `vital_signs` 시계열 플롯.

---

(이하 data07 ~ data21은 유사한 패턴으로 확장. 공간 절약을 위해 data07 예시만 추가하고, 나머지는 "유사 구조"로 요약. 실제 MD에서 전체 나열 추천.)

## data07: e-commerce 추천 시스템
구매 이력과 사용자 선호를 기반으로 추천 알고리즘 실습.

### 디렉토리 구조
```
data07/
├── data/
│   ├── purchase_history.csv  # 구매 이력: 10000행, 컬럼 - user_id, item_id (상품 ID), rating (1-5), timestamp
│   └── user_preferences.csv  # 사용자 선호: 2000행, 컬럼 - user_id, category_pref (카테고리 선호도, Electronics/Fashion 등)
└── scripts/
    ├── rec_cleaning.py        # 희소 행렬 변환 (pivot)
    ├── collaborative_filtering.py  # Surprise 라이브러리 SVD, KNN
    └── rec_viz.py             # 매트릭스 팩토라이제이션 히트맵
```

### 데이터 설명
| 파일명 | 형식 | 행 수 | 주요 컬럼 | 샘플 데이터 예시 |
|--------|------|-------|----------|-----------------|
| `purchase_history.csv` | CSV | 10000 | `user_id`, `item_id`, `rating`, `timestamp` | user_id: U001, item_id: I001, rating: 4, timestamp: 2024-01-01 |
| `user_preferences.csv` | CSV | 2000 | `user_id`, `category_pref` | user_id: U001, category_pref: Electronics:0.8 |

### 활용 예시
- 사용자 기반 추천: `purchase_history` SVD 적용.

---

## data08 ~ data21: 고급 주제 확장
- **data08**: NLP 텍스트 분석 (리뷰 감성, Word2Vec).
- **data09**: 이미지 처리 (OpenCV, CNN 분류).
- **data10**: 네트워크 분석 (그래프 이론, PageRank).
- **data11**: 빅데이터 처리 (Dask, Spark-like).
- **data12**: A/B 테스트 (통계 검정, Bayesian).
- **data13**: 시뮬레이션 모델링 (Monte Carlo).
- **data14**: API 데이터 수집 (Requests, ETL 파이프라인).
- **data15**: 대시보드 빌드 (Dash/Streamlit).
- **data16**: 이상 탐지 (Isolation Forest).
- **data17**: 강화학습 기초 (Q-Learning).
- **data18**: 멀티모달 데이터 (텍스트+이미지).
- **data19**: 윤리적 AI (바이어스 감지).
- **data20**: 배포 및 MLOps (Docker, MLflow).
- **data21**: 종합 프로젝트 (E2E 분석 워크플로우).

