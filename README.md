# 8de server, client, AI 코드 전부 합친 배포버전
* 소스코드는 배포 직전 이곳에 올릴 예정.
* private repository로, key 파일과 keyword.csv파일을 포함해서 올라옵니다.

## 사용 전
* 80번, 3306번, 8000번 포트가 비어있는지 확인합니다. 실행중인 프로세스가 있을 시, 종료할 수 있는 것은 종료합니다.

<br/><br/>

## 소스코드 클론 방법 및 파일 구조
<p align="center"><img width="30%" src="https://user-images.githubusercontent.com/57509844/180640251-522c259a-8475-4417-87a7-5d30abc47371.png" alt="전체 파일 구조"/></p>
<br/>전체 파일 구조는 client, db, nginx, server 4개의 폴더로 이루어져 있습니다.

<br/><br/>

## 실행 방법
1. [server repository](https://github.com/Silicon-Valley-Team-A/server)에서 server 파일들을 클론해옵니다.

2. docker-compose가 있는 폴더 위치로 간 뒤, [client repository](https://github.com/Silicon-Valley-Team-A/client)에서 client 파일들을 클론해옵니다.

3. 그 후 파일 구조는 다음과 같이 이루어져있어야 합니다.<br/>
<p align="center"><img width="30%" src="https://user-images.githubusercontent.com/57509844/180640190-f1e9924f-5451-4483-bf19-3ef851fa6168.png" alt="클라 파일 구조"/></p>

4. 사진과 같이 key.json과 keywords.csv파일을 넣어둡니다. 이 두 파일은 깃허브 공개 리포로 업로드하지 않았습니다.
    * key.json은 장고의 시크릿 키, 스포티파이 api 키가 들어있으며 /server/ 에 위치합니다. manage.py와 같이 있습니다.
    * keywords.csv는 모델에서 사용하는 키워드 파일입니다. /server/model/ 에 위치합니다.
    * 파일이 포함된 /server 폴더 내 구조입니다.<br/>
    <p align="center"><img width="30%" src="https://user-images.githubusercontent.com/57509844/180640285-33ee895b-450b-4db7-9ca1-dae2ca9526cb.png" alt="키 파일 구조"/></p>

5. `docker-compose up` 명령어를 docker-compose.yml 파일이 있는 경로에서 실행시킵니다.

6. 빌드가 완료되면, [https://localhost](https://localhost)에서 웹사이트를 확인합니다.

<br/><br/>

## 빌드 과정
* 빌드한 후 각 컨테이너가 순서대로 실행되며, 모든 빌드가 종료되면 client 컨테이너인 re01은 종료됩니다. 종료되지 않고 실행중이면 빌드 중인 것입니다.
* 최초 빌드 시, 10분~20분이 소요됩니다.

<br/><br/>

## 다른 포트 이용 
특수한 경우로 80번포트를 사용하지 못한다면, 다른 포트를 이용할 수 있습니다.

* ./docker-compose.yml 파일의 27번줄, nginx 컨테이너의 ports를 "80:8080" 에서 "(원하는포트):8080" 으로 변경합니다.

* 접속할 때 https://localhost:(변경한포트) 로 접속합니다.
