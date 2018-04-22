#!/bin/bash
echo 'Starting Docker Compose in Daemon mode if not already started'
docker-compose up --build -d
docker-compose exec web python tests/test_fib.py
echo 'Tests complete'
echo 'run docker-compose down to shutdown docker stack'
