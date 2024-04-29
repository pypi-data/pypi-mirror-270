import logging
import threading
import queue

_SHUTDOWN = object()

logger = logging.getLogger(__name__)


class Worker:
    def __init__(self):
        self._queue = queue.Queue()
        self.lock = threading.Lock()
        self._thread = None
        self.running = False

    def start(self):
        with self.lock:
            if not self.running:
                self._thread = threading.Thread(
                    target=self._run, name="TraceDuck-BackgroundWorker"
                )
                try:
                    self._thread.start()
                    self.running = True
                except RuntimeError:
                    self._thread = None

    def stop(self):
        with self.lock:
            if self.running:
                self._queue.put_nowait(_SHUTDOWN)
                self.running = False

    def add_task(self, task):
        self.start()
        self._queue.put_nowait(task)

    def _run(self):
        while True:
            task = self._queue.get()

            if task is _SHUTDOWN:
                break

            try:
                task()
            except Exception as e:
                logger.error(f"Error while executing task: {e}")
            self._queue.task_done()
