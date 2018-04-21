# vs_py_fib

Included are two versions of fibonacci as a service.  
- fib_aas - is on Python 2.7, NGINX and web.py framework.  
- fib_aas3 - is on Python 3.6, NGINX and web.py dev release framework.  

With the retirement of Python 2.x branch in 2020 various 2.x based libraries are starting to migrate to 3.x series, if they haven't already. I believed the running a dev/pre-release version of web.py framework would be unwise in production.  But it would be good to be prepared with a version for Python 3.  This use of NGINX and gunicorn are considered effective methods for Python web applications on Docker.  

Pre-requisites:  Docker (tested on 18.03 and docker compose 3 format)

To use this software.
1. Download this repo.
2. In terminal or command prompt. Change into either fib_aas or fib_aas3 directory.
3. Type docker-compose build (you can do docker-compose up --build or docker-compose up -d --build)
4. Type docker-compose up or docker-compose up -d (daemonized mode).

You should be able to access from http://localhost/<number>
Example http://localhost/15

Note: This attempts to bind NGINX to port 80 on the host.  If this is unacceptable modify docker-compose.yml accordingly and the hostname in web_app/tests/test_fib.py. 

Included is a unit test script that runs valid and invalid data against the fib_aas service.  

To run the test suite 
On macOS/LINUX
1. In terminal or command prompt. Change into either fib_aas or fib_aas3 directory.
2. ./run_unit_test.sh 

On Windows
1. Command prompt. Change into either fib_aas or fib_aas3 directory.
2. run docker-compose up -d
3. run docker-compose exec web python tests/test_fib.py

Remember to type docker-compose down to destroy the running containers when done or if you wish to switch versions.  
