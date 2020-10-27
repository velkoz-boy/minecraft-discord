#!/usr/bin/env python
from __future__ import print_function

import sys
import time
import subprocess
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("a")


def watch():
    event_handler = MyHandler()
    observer = PollingObserver()
    observer.schedule(event_handler, "./test.txt", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

watch()