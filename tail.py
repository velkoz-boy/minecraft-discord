import os
import sys
import time
import re
import asyncio
import discord
import chardet

from config import get_config
from minecraft_log import MinecraftLog
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler


config = get_config()


class TailHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path
        # Windowsしか想定していないのでshift_jisだが、macとかを考えると環境で変えるべき
        self.file = open(path, 'r', encoding='shift_jis')
        self.pos = os.stat(path)[6]
        self.lines = []
    
    def get_lines(self):
        self.file.seek(self.pos)
        # EOLは取得しない
        for line in re.findall(".*?\n", self.file.read()):
            yield line
        self.pos = self.file.tell()
    
    def on_modified(self, event):
        lines = []
        for line in self.get_lines():
            lines.append(line.rstrip())
        self.lines = lines


async def observe_chat(path, discord_client):
    event_handler = TailHandler(path)
    observer = PollingObserver()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        pos = 0
        while True:
            if pos != event_handler.pos:
                for line in event_handler.lines:
                    log = MinecraftLog()
                    log.parse(line)
                    channel = discord_client.get_channel(770624629412593666)
                    if log.is_chat():
                        await channel.send(log.get_content())
                event_handler.lines = []
                pos = event_handler.pos
            await asyncio.sleep(0.01)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()