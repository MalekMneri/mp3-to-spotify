package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/callback", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w,"copy link to the terminal or use the code below")
		fmt.Fprintln(w, "code is:\n" +r.URL.Query().Get("code"))
	})


	http.ListenAndServe(":8000",nil)
}
