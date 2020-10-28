import os
import sys
import time
import re
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler


class TailHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'r')
        self.pos = os.stat(path)[6]
    
    def get_line(self):
        self.file.seek(self.pos)
        for line in re.findall(".*?\n", self.file.read()):
            yield line
        self.pos = self.file.tell()

    def on_modified(self, event):
        count = 0
        for tset in self.get_line():
            print(count)
            print(tset)
            count = count + 1


def tail(path):
    event_handler = TailHandler(path)
    observer = PollingObserver()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.01)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

tail(r"./server/logs/latest.log")