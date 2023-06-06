FROM golang

WORKDIR /app

ADD web-server.go /app

RUN go mod init web-server && go get github.com/gorilla/handlers && go build web-server.go

EXPOSE 8080

ENTRYPOINT [ "/app/web-server" ]