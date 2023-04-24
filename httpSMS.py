"""Thie is an example to send a text message to a phone
via textbelt HTTP text server
試著經 textbelt HTTP 服務器，發簡訊到一個手機號"""

from sample.credentials import mobile_number
import requests


def send_text(msg):
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': msg,
        'key': 'textbelt'
    })
    print(resp.json())


# 設定資料夾位置及檔案名稱
path_dir = 'sample'  # relative to the current dir
file_text = f'{path_dir}/test.txt'

with open(file_text, 'r') as f:
    body = f.read().strip()


print(f"經 textbelt HTTP 服務器，發簡訊到 {mobile_number}...")

# Max length of a SMS is normally 160 characters or less (80 only for textbelt)
send_text(body[0:80])
