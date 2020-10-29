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
        target = r"^\[(\d+:\d+:\d+)\] \[(.+)\]: (.+)"
        target_line = re.match(target, line)
        if target_line:
            (time, info, content) = target_line.groups()
            self.timestamp = self._parse_time(time)
            self.info = info
            self.content = content

    def _parse_time(self, time):
        time = time.split(":")
        return datetime.time(
            hour=int(time[0]), minute=int(time[1]), second=int(time[2])
        )

    def get_content(self):
        return self.content

    def is_chat(self):
        return re.search("^<.+> .*|^\\[.+\\] .*", self.content)
