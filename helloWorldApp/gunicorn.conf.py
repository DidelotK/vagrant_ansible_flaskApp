bind = "0.0.0.0:5000"

workers = 2
worker_class = 'gevent'

max_requests = 1000
timeout = 30
keep_alive = 2

preload = True