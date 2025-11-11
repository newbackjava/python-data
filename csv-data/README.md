# csv-data

![status](https://img.shields.io/badge/updated-2025-11-10-informational)  ![license](https://img.shields.io/badge/edu-example-blue)

## 목적
CSV 파일 처리/변환/정리 예제 모음입니다. JSON→CSV, CSV→Parquet 등의 변환 스크립트를 포함할 수 있습니다.

## 설치
```bash
pip install pandas pyarrow
```

## 예제: JSON → CSV
```python
import pandas as pd
df = pd.read_json('sample.json', lines=False)
df.to_csv('sample.csv', index=False, encoding='utf-8')
```

## 체크리스트
- [ ] 구분자(콤마/탭) 확인
- [ ] 인코딩/줄바꿈 규칙 명시
