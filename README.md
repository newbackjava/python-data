
## data01: 기본 데이터 분석 입문
기초 통계, 데이터 클리닝, 간단한 시각화 실습.

### 디렉토리 구조
```
data01/data/
├── users.csv             # 사용자 프로필 (1000행)
└── sales.csv             # 판매 기록 (5000행)
data01/scripts/
├── clean.py              # 결측치 처리, 타입 변환
└── analyze.py            # 기초 통계, 상관분석, 막대그래프
```

### 데이터 설명
| 파일 | 행 수 | 주요 컬럼 | 샘플 데이터 |
|------|------|----------|------------|
| `users.csv` | 1000 | `user_id`, `age`, `gender`, `join_date`, `total_spent` | `U001, 28, M, 2023-01-15, 450000` |
| `sales.csv` | 5000 | `order_id`, `user_id`, `product_id`, `quantity`, `price`, `order_date` | `ORD001, U001, P101, 2, 25000, 2023-02-10` |

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />


## data02: 중급 데이터 클리닝과 탐색
텍스트 처리, 중복 제거, 피벗 테이블 실습.

### 디렉토리 구조
```
data02/data/
├── reviews.csv           # 상품 리뷰 (3000행)
└── campaigns.csv         # 마케팅 캠페인 (1500행)
data02/scripts/
├── clean_text.py         # 소문자 변환, 특수문자 제거, 정규표현식
└── pivot_analysis.py     # 피벗 테이블, 그룹화, 교차 분석
```

### 데이터 설명
| 파일 | 행 수 | 주요 컬럼 | 샘플 데이터 |
|------|------|----------|------------|
| `reviews.csv` | 3000 | `review_id`, `product_id`, `rating`, `comment`, `review_date` | `R001, P101, 4, "배송 빠르고 좋아요!", 2023-03-05` |
| `campaigns.csv` | 1500 | `campaign_id`, `sent_date`, `open_rate`, `click_rate`, `conversion` | `CAMP01, 2023-04-01, 42.3, 15.7, Y` |

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data03: 시계열 분석 입문
날짜 처리, 이동평균, 계절성 분석.

### 디렉토리 구조
```
data03/data/
├── daily_sales.csv       # 일일 매출 (365행)
└── weather.csv           # 날씨 데이터 (365행)
data03/scripts/
├── time_series.py        # to_datetime, resample, rolling
└── correlation.py        # 날씨 vs 매출 상관관계
```

### 데이터 설명
| 파일 | 행 수 | 주요 컬럼 | 샘플 데이터 |
|------|------|----------|------------|
| `daily_sales.csv` | 365 | `date`, `sales`, `holiday` | `2023-01-01, 120000, True` |
| `weather.csv` | 365 | `date`, `temp`, `rainfall_mm` | `2023-01-01, 5.2, 0.0` |

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data04: 소셜 미디어 분석
해시태그, 참여도, 네트워크 분석 기초.

### 디렉토리 구조
```
data04/data/
├── posts.csv             # 소셜 포스트 (5000행)
└── interactions.csv      # 좋아요/댓글 (20000행)
data04/scripts/
├── hashtag_analysis.py   # 해시태그 빈도, 워드클라우드
└── engagement_rate.py    # 참여율 계산, 상위 포스트 추출
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data05: 재무 데이터 분석
재무비율, 주식 가격, 이동평균.

### 디렉토리 구조
```
data05/data/
├── financials.csv        # 분기 재무제표 (200행)
└── stock_prices.csv      # 일별 주가 (2520행)
data05/scripts/
├── ratios.py             # ROE, EBITDA, 부채비율 계산
└── technical.py          # SMA, EMA, 볼린저 밴드
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data06: 의료 데이터 분석
환자 기록, 생존 분석, 바이탈 사인.

### 디렉토리 구조
```
data06/data/
├── patients.csv          # 환자 정보 (1500행)
└── vitals.csv            # 바이탈 기록 (10000행)
data06/scripts/
├── survival.py           # Kaplan-Meier 곡선
└── risk_model.py         # 로지스틱 회귀로 재입원 예측
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data07: 추천 시스템 기초
협업 필터링, 사용자 기반 추천.

### 디렉토리 구조
```
data07/data/
├── ratings.csv           # 사용자-상품 평점 (50000행)
└── items.csv             # 상품 정보 (1000행)
data07/scripts/
├── collaborative.py      # Surprise SVD 모델
└── evaluate.py           # RMSE, Precision@K 계산
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data08: 자연어 처리 (NLP) 입문
텍스트 전처리, 감성 분석, 토픽 모델링.

### 디렉토리 구조
```
data08/data/
├── product_reviews.csv   # 상품 리뷰 (10000행)
└── news_articles.csv     # 뉴스 기사 (5000행)
data08/scripts/
├── preprocess.py         # 토큰화, 불용어 제거, 어간 추출 (NLTK)
├── sentiment.py          # KoNLPy + Logistic Regression 감성 분석
└── topic_model.py        # LDA (Gensim)로 주제 추출
```

### 데이터 설명
| 파일 | 행 수 | 주요 컬럼 | 샘플 데이터 |
|------|------|----------|------------|
| `product_reviews.csv` | 10000 | `review_id`, `text`, `sentiment` | `R1001, "정말 좋아요! 강력 추천", 긍정` |
| `news_articles.csv` | 5000 | `article_id`, `title`, `content`, `category` | `N001, "AI 시장 급성장", "...", 경제` |

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data09: 이미지 처리 및 컴퓨터 비전
이미지 리사이징, 필터링, 간단한 CNN.

### 디렉토리 구조
```
data09/data/
├── images/               # 500장 상품 이미지 (224x224)
│   ├── electronics/
│   └── fashion/
└── labels.csv            # 이미지 라벨 (500행)
data09/scripts/
├── preprocess_img.py     # OpenCV 리사이징, 정규화
├── cnn_classifier.py     # Keras로 전이학습 (MobileNetV2)
└── gradcam.py            # Grad-CAM으로 해석 가능성 시각화
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data10: 네트워크 분석
소셜 그래프, 중심성, 커뮤니티 탐지.

### 디렉토리 구조
```
data10/data/
├── edges.csv             # 사용자 간 팔로우 관계 (10000행)
└── nodes.csv             # 사용자 프로필 (2000행)
data10/scripts/
├── centrality.py         # Degree, Betweenness, PageRank
└── community.py          # Louvain 알고리즘 (community-louvain)
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data11: 빅데이터 처리 기초
Dask로 대용량 CSV 처리, 병렬 연산.

### 디렉토리 구조
```
data11/data/
├── large_sales_*.csv     # 10개 파티션, 각 1M 행 (총 10M)
data11/scripts/
├── dask_load.py          # Dask DataFrame로 로드
├── dask_aggregate.py     # groupby, 병렬 집계
└── memory_profile.py     # 메모리 사용량 비교 (Pandas vs Dask)
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data12: A/B 테스트 및 통계 검정
가설 검정, p-value, 효과 크기.

### 디렉토리 구조
```
data12/data/
├── experiment_a.csv      # A그룹 사용자 행동 (5000행)
└── experiment_b.csv      # B그룹 사용자 행동 (5000행)
data12/scripts/
├── ttest.py              # t-test, Mann-Whitney U
├── power_analysis.py     # 사전 샘플 사이즈 계산
└── bayesian_ab.py        # 베이지안 A/B 테스트 (PyMC)
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data13: 시뮬레이션 및 몬테카를로
리스크 분석, 확률 모델링.

### 디렉토리 구조
```
data13/data/
├── demand_history.csv    # 과거 수요 데이터 (1000행)
data13/scripts/
├── monte_carlo.py        # 재고 최적화 시뮬레이션 (10000회)
└── risk_dashboard.py     # 손실 분포 히스토그램, VaR 계산
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data14: API 데이터 수집 및 ETL
공공 API 호출, JSON 파싱, DB 저장.

### 디렉토리 구조
```
data14/data/
├── raw_api_responses/    # 저장된 JSON 응답
└── weather_api.db        # SQLite DB
data14/scripts/
├── extract.py            # 공공데이터 API 호출 (Requests)
├── transform.py          # JSON → DataFrame 정제
└── load.py               # SQLite INSERT
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data15: 인터랙티브 대시보드
Dash/Streamlit으로 실시간 시각화.

### 디렉토리 구조
```
data15/data/
├── dashboard_data.csv    # 전처리된 통합 데이터
data15/scripts/
├── app_dash.py           # Dash 대시보드 (드롭다운, 그래프)
└── app_streamlit.py      # Streamlit 대시보드 (슬라이더, 캐싱)
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data16: 이상 탐지 (Anomaly Detection)
비지도 학습으로 이상치 탐지.

### 디렉토리 구조
```
data16/data/
├── sensor_readings.csv   # 센서 데이터 (10000행)
data16/scripts/
├── isolation_forest.py   # Isolation Forest 모델
├── autoencoder.py        # Keras Autoencoder 재구성 오차
└── alert_system.py       # 실시간 이상 알림 로직
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data17: 강화학습 기초
Q-Learning, 환경 설계.

### 디렉토리 구조
```
data17/data/
├── game_logs.csv         # 게임 플레이 기록
data17/scripts/
├── grid_world.py         # 5x5 그리드 환경
├── q_learning.py         # Q-Table 학습
└── policy_viz.py         # 최적 정책 시각화
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data18: 멀티모달 데이터 분석
텍스트 + 이미지 결합 분석.

### 디렉토리 구조
```
data18/data/
├── posts_with_images.csv # 포스트 + 이미지 경로 (3000행)
└── images/               # 실제 이미지
data18/scripts/
├── multimodal_model.py   # CLIP (텍스트-이미지 임베딩)
└── similarity_search.py  # "고양이 사진" 검색
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data19: AI 윤리 및 공정성
바이어스 탐지, 공정성 지표.

### 디렉토리 구조
```
data19/data/
├── loan_applications.csv # 대출 심사 데이터 (5000행)
data19/scripts/
├── bias_detection.py     # Disparate Impact, Equal Opportunity
└── fair_ml.py            # AIF360으로 공정성 개선
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data20: MLOps 및 모델 배포
Docker, MLflow, FastAPI.

### 디렉토리 구조
```
data20/data/
├── model_artifacts/      # 저장된 모델 (pickle)
data20/scripts/
├── train_log.py          # MLflow 추적
├── api.py                # FastAPI 엔드포인트
└── Dockerfile            # 컨테이너화
```

<img width="1000" height="13" alt="image" src="https://github.com/user-attachments/assets/bde53837-35c3-447c-8b14-bc67d8254304" />

## data21: 종합 프로젝트 (E2E 파이프라인)
데이터 수집 → 전처리 → 모델 → 배포.

### 디렉토리 구조
```
data21/
├── pipeline/
│   ├── 01_extract.py
│   ├── 02_transform.py
│   ├── 03_train.py
│   └── 04_deploy.py
├── dashboard/
│   └── app.py
└── tests/
    └── test_pipeline.py
```


