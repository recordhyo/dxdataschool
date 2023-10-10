FROM golang:1.15-alpine3.12 AS gobuilder-stage 

#작업 디렉토리 설정 
WORKDIR /usr/src/goapp

#파일 복사
COPY main.go .

#GO 파일 빌드해서 바이너리 프로그램을 생성
#주의 : 자신의 시스템이 아니라 DOCKER의 시스템을 설정해야 함 그래서 GOOS=linux 
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /usr/local/bin/gostart


FROM scratch AS runtime-stage
COPY --from=gobuilder-stage /usr/local/bin/gostart /usr/local/bin/gostart

CMD ["/usr/local/bin/gostart"]
