# chatbot

![status](https://img.shields.io/badge/updated-2025-11-10-informational)  ![license](https://img.shields.io/badge/edu-example-blue)

## 목적
간단한 **규칙 기반/ML 기반** 챗봇 예제와 데이터 전처리, 의도/응답 매핑 샘플을 담습니다.

## 설치
```bash
pip install numpy pandas scikit-learn
```

## 예제: 규칙 기반 매칭
```python
def reply(text):
    rules = { "안녕": "안녕하세요!", "bye": "또 봐요!" }
    for k, v in rules.items():
        if k in text.lower():
            return v
    return "무슨 뜻인지 잘 모르겠어요."
print(reply("안녕"))
```

## 체크리스트
- [ ] 데이터/의도 라벨링 파일 포함
- [ ] 평가 스크립트 제공
