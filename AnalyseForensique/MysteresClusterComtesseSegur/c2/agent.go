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
	mysecret, err := os.ReadFile("flag.txt")
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s", mysecret)
	knock, err := net.Dial("tcp", "127.0.0.1:1337")
	if err != nil {
		panic(err)
	}
	knock.Close()
	time.Sleep(time.Second)
	knock2, err := net.Dial("tcp", "127.0.0.1:1338")
	if err != nil {
		panic(err)
	}
	knock2.Close()
	time.Sleep(time.Second)
	knock3, err := net.Dial("tcp", "127.0.0.1:1339")
	if err != nil {
		panic(err)
	}
	knock3.Close()
	time.Sleep(time.Second)
	conn, err := net.Dial("tcp", "127.0.0.1:31337")
	if err != nil {
		panic(err)
	}
	conn.Write(mysecret)
	flag, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		panic(err)
	}
	conn.Close()
	if flag != "404CTF{command_&_~~conquer~~_control}\n" {
		fmt.Print("NOK\n")
		os.Exit(1)
	}
	fmt.Print("OK\n")
}
