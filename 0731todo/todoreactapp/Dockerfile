#노드 설치
FROM node:alpine

#경로 설정 
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install --force 
RUN npm install react-scripts@5.0.1 -g


#3000번 포트로 npm start 하겠다
EXPOSE 3000
CMD ["npm", "start"]