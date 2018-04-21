#Fibonacci sequence as a restful web service



####To download the code and setup a basic server

Either download as a zip from github or run in the desired locaton on the server <br>
```git clone https://github.com/njspencer79/fib_as_a_service.git```

To launch into dev/adhoc mode<br>
```cd fib_as_a_service```

```python fib_web.py tcpport ```

i.e. ```python fib_web.py 1234 ```

```curl http://localhost:1234/12```
That would provide 12 results.  Like the set below.  We include zero as it is the first Fibonacci number.

```[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]```


**Note: Your firewall may block certain tcp ports.  If you have problems verify that your firewall is not blocking the port you selected.  Also no commas in the number.**

You can also use your browser and go to http://localhost:1234/(number of fibs).  <br>
You can also access from the machine's IP or DNS name.


The web services limits an output of 10,000 Fibonacci numbers and that produces a 10MB download.  This limit can be altered in the fib.web.py file.  If you choose 100,000 numbers that will produce a 1GB download.  Please use a rational limit.  
___

####To test the Fibonacci generator via automated unit tests (test suite).

run ```python test_fib.py```

This process sends garbage input and valid input to the fib_gen.py library.  It then on valid input tests each and every number produced to see if it is a valid Fibonacci number.  
