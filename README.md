# 대전광역시 살수차 최적경로 포트폴리오

## 정제 된 데이터들을 DB에 넣기

## 1번 버튼을 누를 때마다 실시간 교통량 업데이트

## 2번 버튼을 누르면 실시간 교통량에 따른 거리와 교통량에 따른 그래프 생성

## 노드 별로




## -----------------------------------------------

## 분석자료 DB 적재

### Insert_row를 통해 CSV에 있는 도로명, 열섬지수, 교통량, 위경도 좌표 DB에 적재
### 실시간교통정보 기능 업데이트 완료. (버튼 클릭시 -> DB접속 -> 실시간 교통량 API 가져옴 -> DB 업데이트 -> 완료 메세지 출력) 
### 19. 11. 30


## ----------------------------------------------

## 경로탐색알고리즘

### 1. 위경도 좌표를 이용하여 노드간 거리 계산
### 2. 실시간 교통량이 3이상인 노드는 제외
### 3. 노드간에 넓이우선탐색 방식을 이용하여 경로 탐색
