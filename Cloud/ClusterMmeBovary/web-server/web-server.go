package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/gorilla/handlers"
)

func racine() {

}

func main() {
	if _, err := os.Stat("/var/run/secrets/kubernetes.io"); os.Getenv("KUBERNETES_SERVICE_HOST") == "" || os.IsNotExist(err) {
		panic("not running in Kubernetes")
	}
	r := http.NewServeMux()

	r.Handle("/", handlers.LoggingHandler(os.Stdout, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Le drapeau est dans /flag\n")
	})))

	r.Handle("/flag", handlers.LoggingHandler(os.Stdout, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "erte_de_k8s}\n")
	})))

	fmt.Printf("Starting server at port 8080\n")
	if err := http.ListenAndServe(":8080", r); err != nil {
		panic(err)
	}
}
