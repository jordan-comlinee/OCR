EasyOCR 및 다른 모든 OCR을 Test해보기 위한 repo

최근에 개발된 오픈소스 OCR.
Detection은 Clova AI의 CRAFT 알고리즘을 사용하고 있으며, Recongnition model은 CRNN이다.
Tesseract와 달리 GPU를 지원한다.

Tesseract와 비교하여 좋았던 점은 한 번 실행에 여러 언어 인식을 제공한다는 점이었다.
Tesseract도 kor+eng 모델로 실행을 할 수 있었으나, 하나의 모델로 실행할 때보다 인식률이 매우 낮았다.
우리가 하고자 하는 프로젝트에서는 두 가지 언어를 인식하는 점이 중요한데, 이 점에서 EasyOCR이 더 낫다고 판단하여 변경하게 되었다.

다만 텍스트 인식까지 오랜 시간이 소요된다는 점은 EasyOCR의 아쉬운 점인 것 같다.