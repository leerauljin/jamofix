# Jamofix
# 한글 자음 모음 분리현상 수정 파이썬 스크립트

## 개요
NFC(Normalization Form Canonical Composition) 방식과 NFD(Normalization Form Canonical Decomposition) 방식의 인코딩 차이에서 발생하는 파일명 자음 모음 분리현상(예: 안녕하세요 -> ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ)을 수정하기 위한 파이썬 스크립트입니다.

## 요구사항
- Python >= 3.9
- macOS (?)
- (Windows PC를 보유하고 있지 않아서 Windows에서도 작동하는지는 확인해 보지 못했습니다.)

## 사용방법
파일 및 폴더명을 변경하고자 하는 최상위 폴더에 jamofix.py를 복사하고 python jamofix.py로 실행합니다.

## 스크립트 동작과정
1. jamofix.py가 있는 폴더 내의 파일과 폴더를 스캔합니다.
2. 파일 혹은 폴더 이름에 한글이 포함되어 있는지를 확인합니다.
3. 한글이 포함되어 있다면, 파일 혹은 폴더 이름을 NFC 인코딩으로 변경합니다
4. 변경된 파일 혹은 폴더 이름을 출력합니다.
5. 본 과정을 jamofix.py가 있는 폴더 내의 모든 파일과 폴더에 반복합니다
6. 최종적으로 몇 개의 파일과 폴더가 변경되었는지 출력합니다.

## 추후 과제
- Windows에서 작동되는 것을 확인하기
- 좀 더 사용하기 편리한 (CLI or App) 형태로 개발
- Cleaner Code

