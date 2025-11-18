# server/threadpool.py
import threading
import queue
import time
from typing import Callable

class ThreadPool:
    def __init__(self, num_workers: int = 10):
        self.num_workers = num_workers
        self.tasks = queue.Queue()
        self.workers = []
        self.shutdown_flag = threading.Event()

        for i in range(self.num_workers):
            w = threading.Thread(target=self._worker, daemon=True)
            w.start()
            self.workers.append(w)

    def _worker(self):
        while not self.shutdown_flag.is_set():
            try:
                func, args, kwargs = self.tasks.get(timeout=0.2)
            except Exception:
                continue
            try:
                func(*args, **(kwargs or {}))
            except Exception:
                # swallow, worker must stay alive
                pass
            finally:
                self.tasks.task_done()

    def submit(self, func: Callable, *args, **kwargs):
        self.tasks.put((func, args, kwargs))

    def get_queue_size(self):
        return self.tasks.qsize()

    def shutdown(self, wait: bool = False):
        self.shutdown_flag.set()
        # optionally wait for workers to stop
        if wait:
            for w in self.workers:
                w.join(timeout=1)
