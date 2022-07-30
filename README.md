# Recommade
![VAP video2233947482](https://user-images.githubusercontent.com/63364990/181917485-07c54adb-9af6-4796-a356-47bc417af467.gif)

# Demo
[Demo Youtube Link](https://youtu.be/vs-1vnmwkQk)


# Contact Information

| Name    | 신주영 | 김하은 | 최윤지 | 황규현 | 김지연 | 한도현 | 구예찬 | 이효태 |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Profile | ![스크린샷 2022-07-30 오후 11 00 08](https://user-images.githubusercontent.com/63364990/181917794-96e0a3ca-4080-4e8d-818c-b10b8343358b.png)|![스크린샷 2022-07-30 오후 10 59 44](https://user-images.githubusercontent.com/63364990/181917796-8f584971-7014-4300-bef8-b799d886bf3a.png)| ![스크린샷 2022-07-30 오후 11 00 24](https://user-images.githubusercontent.com/63364990/181917822-8d2d56b8-3c9f-4023-84dc-be32a71d8cd1.png)| ![스크린샷 2022-07-30 오후 11 00 29](https://user-images.githubusercontent.com/63364990/181917840-5a973a25-a15d-4069-997d-d6a005561757.png)| ![스크린샷 2022-07-30 오후 11 00 19](https://user-images.githubusercontent.com/63364990/181917821-a2244100-90ee-4b2c-ac7a-1a82575b1031.png) | ![스크린샷 2022-07-30 오후 11 00 42](https://user-images.githubusercontent.com/63364990/181917857-6f3ff876-00fc-4f65-a22e-e48c5e0efa1e.png) | ![스크린샷 2022-07-30 오후 11 00 34](https://user-images.githubusercontent.com/63364990/181917850-dc4a9939-d9ef-40b9-a39a-5be3a87007d2.png) | ![스크린샷 2022-07-30 오후 11 00 38](https://user-images.githubusercontent.com/63364990/181917856-3691f8fc-f693-4574-a075-2f91541858a1.png) |
| role    | Frontend | Frontend | Leader, Backend | Backend | Backend | AI | AI | AI |
| Github  | [@juyeong-s](https://github.com/juyeong-s) | [@harloxx](https://github.com/harloxx) | [@choiyounji](https://github.com/choiyounji) | [@hgyuhyeon](https://github.com/hgyuhyeon) | [@jyjyeon](https://github.com/jyjyeon) | [@Gulitter](https://github.com/Gulitter) | [@Sleepyofvz](https://github.com/Sleepyofvz) | [@LEEHYOTAE](https://github.com/LEEHYOTAE) |


# 8de server, client, AI 코드 전부 합친 배포버전
* ~~배포 및 보관을 위한 소스코드 통합본.~~
* ~~private repository로, key.json 파일과 keyword.csv파일을 포함해서 올라옵니다.~~
* 실행 방법을 간단하게 써 두는 것으로 변경했습니다.

## 사용 전
* 80번, 3306번, 8000번 포트가 비어있는지 확인합니다. 실행중인 프로세스가 있을 시, 종료할 수 있는 것은 종료합니다.

<br/><br/>

## 실행 방법
<p align="center"><img width="30%" src="https://user-images.githubusercontent.com/57509844/180640251-522c259a-8475-4417-87a7-5d30abc47371.png" alt="전체 파일 구조"/></p>

* 루트에서의 파일 구조는 client, db, nginx, server 4개의 폴더와 docker-compose.yml 파일로 이루어져 있습니다.
* AWS 배포 직전 빠른 배포를 위해 여기에 모든 코드를 올렸으나, 유지보수에 불편함이 있어 현재는 삭제했습니다. 따라서 아래의 방법을 따라주시면 됩니다.

1. `git clone https://github.com/Silicon-Valley-Team-A/server.git` 을 실행하여 서버 소스코드를 클론해옵니다.
2. `docker-compose.yml`이 있는 위치에서 `git clone https://github.com/Silicon-Valley-Team-A/client.git`을 실행하여 클라이언트 소스코드를 클론해옵니다.
3. [AI 리포지토리](https://github.com/Silicon-Valley-Team-A/AI)에서 `keywords.csv`랑 `moodmodel`을 다운받아 /server/model/ 디렉토리에 넣어줍니다.
4. `docker-compose up` 명령어를 docker-compose.yml 파일이 있는 경로에서 실행시킵니다.
5. 빌드가 완료되면, [http://localhost](http://localhost)에서 웹사이트를 확인합니다.

<br/><br/>

## 빌드 과정
* 빌드한 후 각 컨테이너가 순서대로 실행되며, 모든 빌드가 종료되면 client 컨테이너인 re01은 종료됩니다. 종료되지 않고 실행중이면 빌드 중인 것입니다.
* 최초 빌드 시, 오랜 시간이 소요됩니다.

<br/><br/>

## 다른 포트 이용 
특수한 경우로 80번포트를 사용하지 못한다면, 다른 포트를 이용할 수 있습니다.

* `./docker-compose.yml` 파일의 27번줄, nginx 컨테이너의 ports를 `"80:8080"` 에서 `"(원하는포트):8080"` 으로 변경합니다.
* `/nginx/default.conf` 파일의 `listen 80;` 을 `listen (변경한포트);` 로 변경합니다.

* 접속할 때 `http://localhost:(변경한포트)` 로 접속합니다.
