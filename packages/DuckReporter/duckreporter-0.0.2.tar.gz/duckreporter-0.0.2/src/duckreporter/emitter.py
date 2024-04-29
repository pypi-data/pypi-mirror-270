import logging

from .worker import Worker
import requests


logger = logging.getLogger(__name__)


class Emitter(object):
    def __init__(self, api_host: str, dsn: str) -> None:
        self._worker = Worker()
        self.api_host = api_host
        self.dsn = dsn

    def emit(self, trace: dict) -> None:

        def _send_trace_task():
            self._send_trace(trace)

        self._worker.add_task(_send_trace_task)

    def _send_trace(self, trace: dict) -> None:
        logger.info(f"Sending trace: {trace}")
        headers = {"dsn": f"{self.dsn}"}
        requests.post(self.api_host + "/i/trace", headers=headers, json=trace)

    def flush(self) -> None:
        self._worker.stop()
