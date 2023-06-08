package main

import "net/http"

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Disposition", "attachment; filename=agent.zip")
		w.Header().Set("Content-Type", "application/octet-stream")
		http.ServeFile(w, r, "/app/agent.zip")
	})
	http.ListenAndServe(":8080", mux)
}
