import requests
import re
import json
from urllib.parse import quote

url="https://chat.openai.com//backend-api/conversation"

headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/event-stream",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://chat.openai.com/c/188f57c0-18b2-42d3-a4ae-c358823576ef",
        "Content-Type": "application/json",
        "Authorization": "",
        "Content-Length": "442",
        "Origin": "https://chat.openai.com",
        "Alt-Used": "chat.openai.com",
        "Connection": "keep-alive",
        "Cookie": ''.encode("utf-8"),
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "TE": "trailers"
}


def cgpt(test):
    test=test.replace('\"','\\\"')
    test=test.replace("\'","\\\"")
    payload='{"action":"next","messages":[{"id":"aaa2b638-28b8-44ed-a7cb-ae64f7e288cf","author":{"role":"user"},"content":{"content_type":"text","parts":["%s"]},"metadata":{}}],"conversation_id":"188f57c0-18b2-42d3-a4ae-c358823576ef","parent_message_id":"d5bec847-1962-436d-af47-e583c6991648","model":"text-davinci-002-render-sha","timezone_offset_min":-330,"suggestions":[],"history_and_training_disabled":false,"arkose_token":null,"force_paragen":false}'%(test) 
    response = requests.request("POST",url, headers=headers, data=payload)
    parsed=response.text.split("\n")
    parsed=parsed[-7]
    a=re.search(r'parts',parsed)    
    x= a.span(0)
    x=x[1]
    parsed=parsed[x+5:]
    a=re.search(r']}',parsed)
    y=a.span(0)
    y=y[0]

    parsed=parsed[:y-1]

    parsed="\n"+json.loads(json.dumps(parsed))+"\n"
    parsed=parsed.replace('\\n','\n')
    parsed=parsed.replace('\\\"','\"')
    parsed=parsed.replace('\\\'','\'')
    return parsed

cgpt(input())
