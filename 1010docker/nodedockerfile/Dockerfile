FROM node

#작성자 알려주는 명령 - 선택적
MAINTAINER recordhyo <gytla1@naver.com>

#명령어 실행 - 디렉토리 생성
RUN mkdir -p /app
#작업디렉토리 설정
WORKDIR /app
#로컬 파일 추가 - package.json, app.js 를 app 디렉토리로 복사
ADD . /app
#라이브러리 설치 
RUN npm install

#포트 개방 
EXPOSE 3000 80

#컨테이너에서 실행할 명령 - 컨테이너로 만들어질 때 수행해서 웹 서버 역할을 수행
CMD ["npm", "start"]