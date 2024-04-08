# MINI_PJ-Cafe_Kiosk
<img src ="https://img.shields.io/badge/Python-071D49?logo=Python&logoColor=white"/><img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/><img src="https://img.shields.io/badge/Bootstrapap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/><img src ="https://img.shields.io/badge/OpenAI-00A3E0?logo=OpenAI&logoColor=white"/>

🛒Kiosk-COCO

## Description

-- Home(주문시작)을 알리는 페이지로 URL은 포트번호로 시작하며 버튼을 누르면 카테고리로 넘어갑니다.

-- 3종류의 카테고리가 있으며 버튼을 누르면 카테고리에 해당하는 메뉴로 넘어갑니다.

-- 메뉴 선택페이지로 해당 카테고리에 메뉴의 정보와 수량을 체크하는 버튼과 현재상태를 저장하는 담기 버튼이 있습니다
**구현하고 싶은 기능**
담기를 누르면 사이드바에 선택했던 메뉴들이 담기며 최종적으로 주문하기를 눌렀을 때 데이터베이스 Order테이블에 저장이 됩니다.
-- 취소와 카드 정보가 입력되었을 때 영수증 페이지로 넘어갑니다

-- 영수증 페이지에 매장 정보와 주문 정보 / 금액(부가세계산) / 결제방법 등 템플릿으로 확인합니다
**구현하고 싶은 기능**
20초를 설정하여 시간이 지나면 처음 페이지로 돌아갑니다.

## 대문페이지
![대문페이지](https://github.com/GordPark/MINI_PJ-Cafe_Kiosk/assets/134121857/fecbf38a-1db9-4f52-9d1a-b82edb2c1298)
## 카테고리 페이지
![카테고리 페이지](https://github.com/GordPark/MINI_PJ-Cafe_Kiosk/assets/134121857/287e89e8-0e01-47b8-815e-9542565294ee)
## 메뉴페이지
![메뉴페이지](https://github.com/GordPark/MINI_PJ-Cafe_Kiosk/assets/134121857/9eedff9d-0bb6-49da-bb93-1b4699660953)


## 📝Conceive
![키오스크1](https://github.com/GordPark/MINI_PJ-Cafe_Kiosk/assets/134121857/87149987-837c-467f-83bf-98627ad4e228)
![키오스크2](https://github.com/GordPark/MINI_PJ-Cafe_Kiosk/assets/134121857/e44e8dbe-73a2-4ec8-98de-708589f10e26)


## Environment

~/miniconda3/python `v.3.10.0`

**requirements.txt**
`asgiref==3.8.1`

`Django==5.0.3`

`django-debug-toolbar==4.3.0`

`pillow==10.3.0`

`sqlparse==0.4.4`

`typing_extensions==4.10.0`

## IDEA

처음 구상했을 당시

카테고리-> 메뉴 -> 옵션

무인카페키오스크

키오스크 - 옆에 머신과 같이 바로 음료 나오고

일반카페랑 차이점 뭔지

과정)주문완료 -> "컵을 받으세요"

몇초 뒤 멘트나오게 ex)에스프레소 나옴 진행도

실시간 반영 되는 커피 / 주문이 완료되고 만들어지는거랑 차이

대기번호!

메뉴사진
