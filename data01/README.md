# 프로젝트명: Python 데이터 분석 프로젝트

## 개요
이 프로젝트는 파이썬을 사용하여 데이터 분석 및 처리의 기초를 배우기 위해 설계되었습니다. 다양한 데이터셋을 사용하여 데이터 정제, 분석, 시각화 등의 과정을 포함합니다.

## 사용 방법
1. **리포지토리 클론**:
   ```bash
   git clone https://github.com/newbackjava/python-data.git
   cd python-data/data01
   ```

2. **필요한 라이브러리 설치**:
   프로젝트에서 사용되는 라이브러리를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```

3. **스크립트 실행**:
   원하는 분석 작업에 맞는 스크립트를 실행합니다.
   ```bash
   python scripts/data_cleaning.py
   python scripts/data_analysis.py
   python scripts/data_visualization.py
   ```

## 기여 방법
기여를 원하시는 분은 다음 단계를 따라 주세요:
1. 이 리포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. 변경 사항을 커밋합니다:
   ```bash
   git commit -m "Add some feature"
   ```
4. 브랜치를 푸시합니다:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Pull Request를 제출합니다.

## 라이선스
이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다.

## 문의
질문이 있으신 경우, GitHub 이슈 페이지를 통해 문의해 주세요.


### 각 스크립트에 대한 구체적인 설명

1. **data_cleaning.py**
   - **목적**: 데이터셋에서 결측치 및 중복 데이터를 처리하여 분석에 적합한 형태로 만듭니다.
   - **주요 라이브러리**: 
     - `pandas`: 데이터 프레임을 사용하여 데이터를 조작합니다.
   - **주요 함수**:
     - `load_data()`: 데이터를 로드하는 함수.
     - `clean_data()`: 결측치 및 중복을 처리하는 함수.
     - `save_cleaned_data()`: 정제된 데이터를 저장하는 함수.

2. **data_analysis.py**
   - **목적**: 데이터셋을 분석하고 통계치를 계산하여 인사이트를 도출합니다.
   - **주요 라이브러리**:
     - `pandas`: 데이터 조작 및 분석.
     - `numpy`: 수치 계산을 위한 라이브러리.
   - **주요 함수**:
     - `perform_analysis()`: 데이터셋에 대한 다양한 분석을 수행하는 함수.
     - `generate_statistics()`: 평균, 중앙값, 표준편차 등을 계산하는 함수.

3. **data_visualization.py**
   - **목적**: 분석 결과를 시각적으로 표현하여 인사이트를 더 쉽게 이해할 수 있도록 돕습니다.
   - **주요 라이브러리**:
     - `matplotlib`: 데이터 시각화.
     - `seaborn`: 통계적 데이터 시각화를 위한 라이브러리.
   - **주요 함수**:
     - `create_charts()`: 다양한 차트를 생성하는 함수.
     - `show_visualizations()`: 생성된 차트를 화면에 표시하는 함수.

