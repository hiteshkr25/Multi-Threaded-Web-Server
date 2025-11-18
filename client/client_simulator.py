# client/client_simulator.py
import socket, threading, time, random

running = False
_worker_threads = []

def send_once(host, port, path):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))
        req = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        s.sendall(req.encode())
        try:
            _ = s.recv(4096)
        except:
            pass
        s.close()
    except:
        pass

def worker(mode, host, port, path, stagger_ms):
    global running
    while running:
        send_once(host, port, path)
        if mode == "continuous":
            time.sleep(max(0.001, stagger_ms/1000.0))
        elif mode == "burst":
            # many rapid requests (short sleeps)
            time.sleep(random.uniform(0.01, 0.06))
        elif mode == "spike":
            # mostly idle, occasional bursts
            if random.random() < 0.8:
                time.sleep(random.uniform(0.3, 0.9))
            else:
                time.sleep(0.005)

def run_load_test(client_count=50, server_host='127.0.0.1', server_port=8081,
                  path='/', rounds_per_thread=1, stagger_ms=10, mode="continuous"):
    """
    Starts the simulated load. For 'continuous' the function returns after threads launched
    and threads run until stop() is called. For burst/spike, it will run a bounded time
    and return when finished.
    """
    global running, _worker_threads
    if running:
        return
    running = True
    _worker_threads = []

    for i in range(client_count):
        t = threading.Thread(target=worker, args=(mode, server_host, server_port, path, stagger_ms), daemon=True)
        _worker_threads.append(t)
        t.start()
        # small stagger on startup
        if (i + 1) % 10 == 0:
            time.sleep(0.02)

    if mode == "continuous":
        # return immediately; dashboard should call stop() when needed
        return
    else:
        # finite run for burst/spike: attempt to run for a few seconds
        total_loops = max(1, rounds_per_thread)
        try:
            for _ in range(total_loops * 5):
                if not running:
                    break
                time.sleep(0.25)
        finally:
            running = False

def stop():
    global running
    running = False
