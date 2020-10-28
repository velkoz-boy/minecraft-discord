# minecraft-discord
minecraftとdiscordのチャットを連動するbotをつくる。

## つかいかた
yamlにいろいろ設定する。
bot.py起動する。exe化したい。

## Discord -> Minecraft
RCONを使って、コマンドでチャット内容を送信する

## Minecraft -> Discord
latest.logを監視し、ユーザーのチャットと同じフォーマットの行をパースする

## 使用ライブラリ
https://github.com/Rapptz/discord.py  
https://github.com/serverstf/python-valve  
https://github.com/gorakhargosh/watchdog  
https://github.com/yaml/pyyaml  
