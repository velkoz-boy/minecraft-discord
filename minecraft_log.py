import datetime
import re


class MinecraftLog:
    """
    [13:29:27] [Server thread/INFO]: Preparing spawn area: 0%
    のように"[時刻] [ログ情報] 内容"でフォーマットされたログが渡される前提。
    それ以外の形式のログが万が一渡ってきた場合は、例外を発生する可能性がある。
    """

    def __init__(self):
        self.timestamp = None
        self.info = ""
        self.content = ""

    def parse(self, line):
        if not line.startswith("["):
            # "["で始まらないログは空文字で返す（使わないので）
            return ""

        block = ""
        for character in iter(line):
            if not self.timestamp or not self.info:
                if character == "[":
                    block = ""
                    continue
                elif character == "]":
                    self._parse(block)
                    block = ""
                else:
                    block += character
            else:
                block += character
        self._parse(block.lstrip(": "))

    def _parse(self, block):
        if not self.timestamp:
            time = block.split(":")
            self.timestamp = datetime.time(
                hour=int(time[0]), minute=int(time[1]), second=int(time[2])
            )
        elif not self.info:
            self.info = block
        elif not self.content:
            self.content = block

    def get_content(self):
        return self.content

    def is_chat(self):
        return re.search("^<.*> .*|^\\[.*\\] .*", self.content)
