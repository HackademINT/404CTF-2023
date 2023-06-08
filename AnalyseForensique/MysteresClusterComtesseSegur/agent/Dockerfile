FROM golang

WORKDIR /app

ADD agent.zip /app
ADD serve.go /app

EXPOSE 8080

CMD go run /app/serve.go