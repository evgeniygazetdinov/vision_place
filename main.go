package main 
import (serv "lib"
		"fmt")



func main(){
	server := serv.Init("127.0.0.1:0")
	if err := server.Start(); err != nil {
		fmt.Println(err)
	}
	// fmt.Println("here")
	// url := "http://" + server.Addr
	// if _, err := http.Get(url); err != nil {
	// 	fmt.Println(err)
	// }
	// if _, err := http.Get(url); err == nil {
	// 	fmt.Println("error expected")
	// }

}