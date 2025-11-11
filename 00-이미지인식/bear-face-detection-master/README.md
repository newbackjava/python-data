# 00-이미지인식

![status](https://img.shields.io/badge/updated-2025-11-10-informational)  ![license](https://img.shields.io/badge/edu-example-blue)

## 목적
간단한 **컴퓨터 비전** 실습을 위한 폴더입니다. 예: 얼굴/객체 감지, 이미지 분류 등.  
하위에 `bear-face-detection-master`와 같은 예제가 있을 수 있습니다. (예: OpenCV/딥러닝 기반)

## 권장 설치
```bash
pip install opencv-python numpy matplotlib scikit-image
# 딥러닝 예제가 포함되면
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## 예시: OpenCV로 이미지 불러오기
```python
import cv2
img = cv2.imread('images/sample.jpg')
print(img.shape if img is not None else "이미지 경로를 확인하세요.")
```

## 체크리스트
- [ ] 이미지/모델 파일 경로 확인
- [ ] GPU 사용 시 CUDA 호환성 확인
- [ ] 라이선스(모델/데이터) 확인
