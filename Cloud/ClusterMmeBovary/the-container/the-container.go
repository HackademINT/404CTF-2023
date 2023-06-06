package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

const path = "/opt/my_secret_dir/"
const flag = "404CTF{A_la_decouv\nLe reste du flag est dans le conteneur 404ctf/web-server"
const env_name = "SUPER_ENV"
const env_value = "SECRET"
const namespace = "404ctf"

func main() {
	if _, err := os.Stat("/var/run/secrets/kubernetes.io"); os.Getenv("KUBERNETES_SERVICE_HOST") == "" || os.IsNotExist(err) {
		panic("not running in Kubernetes")
	}
	for {
		currentNamespace, err := ioutil.ReadFile("/var/run/secrets/kubernetes.io/serviceaccount/namespace")
		if err != nil {
			fmt.Println(err)
		}
		if string(currentNamespace) != namespace {
			fmt.Printf("err: not in namespace %s\n", namespace)
		} else {
			_, err := os.Stat(path)
			if os.IsNotExist(err) {
				fmt.Printf("err: %s does not exist\n", path)
			} else if err != nil {
				fmt.Println(err)
			} else {
				if os.Getenv(env_name) != env_value {
					fmt.Printf("Env %s is not set to %s\n", env_name, env_value)
				} else {

					f, err := os.Create(fmt.Sprintf("%sflag.txt", path))
					if err != nil {
						fmt.Println(err)
					}
					defer f.Close()
					_, errW := f.Write([]byte(flag))
					if errW != nil {
						fmt.Println(errW)
					}
					fmt.Printf("Flag written to %sflag.txt\n", path)
				}
			}
			time.Sleep(time.Second)
		}
	}
}
