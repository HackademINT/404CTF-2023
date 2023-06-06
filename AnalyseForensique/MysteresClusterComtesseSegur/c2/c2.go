package main

import (
	"bufio"
	"fmt"
	"net"
	"time"
)

const knock1 = "1337"
const knock2 = "1338"
const knock3 = "1339"
const port = "31337"
const flag = "404CTF{command_&_~~conquer~~_control}"

func handleTCPKnock(conn net.Conn, port string, ipChan chan string, ipArray []string, errChan chan string) {
	ipSrc := conn.RemoteAddr().(*net.TCPAddr).IP.String()
	conn.Close()
	errChan <- fmt.Sprintf("%s knock on port %s\n", ipSrc, port)
	//prevent a port scan from trigerring the knock sequence
	time.Sleep(500 * time.Millisecond)
	//For the first knock, ipArray is empty
	if port == knock1 {
		ipChan <- ipSrc
		return
	}

	//verify that the ipSrc has done the previous knocks
	for _, ip := range ipArray {
		if ip == ipSrc {
			ipChan <- ipSrc
			return
		}
	}
}

func listenTCPKnock(port string, ipSendChan chan string, ipRecvChan chan string, errChan chan string) {
	//we listen for incoming TCP conn on specified port
	ln, err := net.Listen("tcp", fmt.Sprintf(":%s", port))

	if err != nil {
		panic(err)
	}

	//Array to store the IPs
	ipArray := make([]string, 0, 20)

	//ticker to empty periodicaly the ipArray
	ticker := time.NewTicker(time.Minute)

	for {
		//new conn
		conn, err := ln.Accept()
		if err != nil {
			errChan <- err.Error()
		}

		select {
		//when the ticker is up, we empty ipArray
		case <-ticker.C:
			ipArray = make([]string, 0, 20)
		default:

		}

		if ipRecvChan != nil {
			select {
			//when we receive an ip
			case ipRecv := <-ipRecvChan:
				ipArray = append(ipArray, ipRecv)
				if ln.Close() != nil {
					panic(err)
				}
				ln, err = net.Listen("tcp", fmt.Sprintf(":%s", port))

				if err != nil {
					panic(err)
				}
			default:

			}

		}

		//handle conn
		go handleTCPKnock(conn, port, ipSendChan, ipArray, errChan)
	}
}

func handleTCPConn(conn net.Conn, ipArray []string, errChan chan string) {
	ipSrc := conn.RemoteAddr().(*net.TCPAddr).IP.String()
	defer conn.Close()
	errChan <- fmt.Sprintf("%s connects\n", ipSrc)

	//verify that the ipSrc has done all the knocks
	for _, ip := range ipArray {
		if ip == ipSrc {
			password, err := bufio.NewReader(conn).ReadString('\n')
			if err != nil {
				errChan <- err.Error()
				return
			}
			errChan <- fmt.Sprintf("%s gave password %s", ipSrc, password)
			if password == "404CTF{K8S_checkpoints_utile_pour_le_forensic}\n" {
				conn.Write([]byte(fmt.Sprintf("%s\n", flag)))
				return
			}
			return
		}
	}
}

func listenTCP(port string, ipRecvChan chan string, errChan chan string) {
	//we listen for incoming TCP conn on specified port
	ln, err := net.Listen("tcp", fmt.Sprintf(":%s", port))

	if err != nil {
		panic(err)
	}

	//Array to store the IPs
	ipArray := make([]string, 0, 20)

	//ticker to empty periodicaly the ipArray
	ticker := time.NewTicker(time.Minute)

	for {

		//new conn
		conn, err := ln.Accept()
		if err != nil {
			fmt.Print(err)
		}

		select {
		//when the ticker is up, we empty ipArray
		case <-ticker.C:
			ipArray = make([]string, 0, 20)
			if ln.Close() != nil {
				panic(err)
			}
			ln, err = net.Listen("tcp", fmt.Sprintf(":%s", port))

			if err != nil {
				panic(err)
			}
		default:

		}

		select {
		//when we receive an ip
		case ipRecv := <-ipRecvChan:
			ipArray = append(ipArray, ipRecv)
		default:
		}

		//handle conn
		go handleTCPConn(conn, ipArray, errChan)
	}
}

func main() {
	c1 := make(chan string, 100)
	c2 := make(chan string, 100)
	c3 := make(chan string, 100)
	err := make(chan string, 100)
	go listenTCPKnock(knock1, c1, nil, err)
	go listenTCPKnock(knock2, c2, c1, err)
	go listenTCPKnock(knock3, c3, c2, err)
	go listenTCP(port, c3, err)
	for {
		fmt.Print(<-err)
	}
}
