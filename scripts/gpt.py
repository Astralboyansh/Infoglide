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
"Referer": "https://chat.openai.com/",
"Content-Type": "application/json",
"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhbnNoMTIzaWNpY2lAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy1YT2RZM1dYd3JadU9CQ2ZQd1J2ZTJmdHIiLCJ1c2VyX2lkIjoidXNlci00Zjd6anRpc2dxdEI0bFF2eURDT1VJNFAifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTE0MjcwMjY5MTQ1NzI5MjYxODA5IiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5ODQ3MDU1OCwiZXhwIjoxNjk5MzM0NTU4LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9yZ2FuaXphdGlvbi53cml0ZSBvZmZsaW5lX2FjY2VzcyJ9.X7gGtbeb7aPI7Ecawl3xHHfu7I2XSNB-Ebkn96OOUf1G36U6eSIuQRDt-OOUAzWtPirSgvZ4h_74XrL0B942zXoruTK9RDlMbxvt4ueJwDwMp1CM6II_5SLwpy7_jKOmW0yPUFurdk1bYXJhHuKMa6REb5pyVKBImR1iXDAppm1y9z9qEUf3CVECVYr6uIG3oa8HX1L4hzPkTxqTnjN0jqiaJR-mD0Y4mtM2SmOEoWMxOXQRyC282TJL4jlG4q6t4XW7HnZrBbpcjBgyo6GTewxJvkLsHImYl_rdN_KdNksHRuo9bcmfHX_-26wuafpfEN_do2w5Ai39HnO_NEIYzw",
"Content-Length": "1131",
"Origin": "https://chat.openai.com",
"Alt-Used": "chat.openai.com",
"Connection": "keep-alive",
"Cookie": "cf_clearance=52pCtPSvNkmEUHqRMq3i4gcNmzoYY0ysipWCKWUnNX4-1698470559-0-1-d823a8cc.89046238.a1852719-0.2.1698470559; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..1SeVGPZpGTQmHRVw.Kx39sKeIUnkO6DY-f61O58X2FRx_2HK7aJEiJlBuCWYKGHOJW3rZ3d6KPd5cMxDC6FLpFPsd-I1a-LYTwQTCaeR8dNn0PASypYEEQKtd5x--pB6geyUTcusqLr1MmYX6wly3xQmVluSNlzE0TUuOk3L5R4riQy-E5CA0vFWPxwdmkqa4HCZzUq2tkVHYwUfTgLY76rSN7K7bH_6rcvhPeZne9mEZn6OTSwcHMWOyjZWilSImw_d8bh8kVteB5-6PVGlPoE1o3PAafJhEFlH8NHOUfq-0PhUW3onUWRpe6a8TSBXPaWaEILyWwTo2G_5MQquRtMMhb6Ift9dyMUdW57B6TicJQx_idbefYTmhCOnetP9KuE3Ocf0Njccwa5QOBjfcP971cR9yR7jQOnTOBY0aN3zDr4O4dl5T0f6c5F1rBSV1osI8bbMLwEVoV0JzhTPRpxKFk6HlHD7X_faqYxytk0t29kVrTEQ7fas12ihvsfLTypLE16X9xEFd5CCxz0m7gxgRCYcFdVPTIwgdoezX5DgmlyMG2grBG9YHT9edtW_xIZFV1Wpbj1NHn-V79_auOduKO-zTQFwgQzONNSRrfaipUU-TerCEd5GobQ34y7-PjFACJUzEeH8AmhemCGNfWrV3LHuMFes64r3cicNWlrB68TU9iiII1rrzlh3lPZMokJxXlVoW3RkesVVqsRszxk1Q2ziQZub_EbwsxLTQGkBe7BcXxfn6_fGQb8jpyztGYOos9xoW_iAf1Xi7zMED-Yy8OZgl8T2678PJVxMIkUqBd54gERsMTsCRiQp9-Tu5_Wh7fUMeYNUwiV4Y5E_4nXOm8D4iR-BqRwbFwIO63JuykBCd5mN_9uWvxlm8P437B72W32YiUmyx35dVB43SnvQpVEx0yrjvyujVHxIiq3G_Aru-L5Do-Y_i3Y4uJrGyzL8MT9uqFY8dq6xeB81-GuIXJr_rXI35GEFpsWx8nR_OLIxcQhLpM_YscTeSTYPJ3QaE0Ib8fqerVj5qnD5DGBQzG2x8HtrYzDqtZWZ7vNOwS8g-PXpwEdkI1iUb6zGz9MquCQYT_1KTHsXWEsLaeehiXJH-3f9-Vr6PJpx_kfhO1FV32IysSp11rAuA2jPdOlYd0ASNA8gg7m61pXkivxl1BxQ5Y4E9RaAjsZp3hiaYcYF4NGaszYOTomWEuZvMdnsLrf0EppHqszEFqe1qhEYgXwUYfUZZ5VE_u--f6MIen3FQsfnaNVatJFItqo04Fkyrg1f5ZfugiPETLwMK7lkaJVd6l9qhPX2u3-e160oJrU1b0rA-1qSIPvGsGHjfrHHyQmwqRZ16soeawmXM_Bcu8dZEYl3BrKGPtN6ezvd5sRjqQsh2xCjU4dzxZrfoFBWy79-f0GyqE28DNxbFHIc8ETXS8PbXUyIsmNVIqsOIUgdI4OnQoXyM8HCXImd3BXwsPSrn-IfeahXxi0q0MFvl4cKwLNwr3kz8eYMcOdz72YtXpKbnG-h21R2e3x1oKkt_SRT9yu33IQty2pgt7i8gzQjUDOd1UYHMxG1oBN9NapSc9O7OrFa2n87YCWwVWrnb_AcEZYANFf0xbDrRE7NCtKzlZFadn2fNgijD6d20QuTUBbUFnfLop43yV3VFKqr7DFXjKq_bHURNh7XcctAdF-8F-BRj_DDBbl0qkhULMZnH2Yn8nIVBqECqq2qtVE8pGP7wkRZrSaBK4omWBVeenW06GAAmc6kI2oH8y6Ac1ZUJWiFgxD12YnuLPWABh2ETVP39SgbsozWwu7GdbnQDsvFr7uAc_TooXo0Twvt2TEcc6KnTYz9kTCYVtfpqGWXs9utt-jY-25UEYSgv9DZLNfcAhCafGEUrBTihZv37GP08g5pwNGBrHhe_wt6KV9nw9Ru1inb2p8cp4EJlhr2WqtDFu9sBLXbXSYcNauktFPm1-sCL23Yb7DoHpaLB33eG5GVzrUSQg_LUTZLfQ9l82mxLpMEv15q1u5JHz6tFS7jOJEDObUGRmUqS4K8_WvQCCJQDXaihEdn_tfGRpubIzf8ImHgAEZchh19l2N5JYEUl8JXLKbuhzuqlh2FGEuYTd47UdLbhyymhOmafIPVStue97QfbDyJRwBdVUTHx_jKERI8WQwMHXv5DmSk_MyUKYL6Q7Jgw4HCzb0IN7BcKjCToMK7GKOyuZ9d_9U6gRapHRnmvs-SxquqcjqsSY2GOCtPvVnwR49_ZjajpLPfeg1HKiKhPkN_SD73ol5_IMOdWfl3MuJFdDuek9w4Y3lpikAbQ4MI69tM2I-hEen_yE_YxgC0bx7JXruc8hGH0w6tdvzmkn74_1oonHb9cLu8n0LtD-G1WdzDIkTeHiPcAOGhbeJ4EVJG4br0MhTBZNRImVuun-2tf2BfeXHNgDZSztmu0bhQsfFpBDrRDWNlcBrExvnZiO_LBqtkvee488VGM-dFXSn5BGIpfNtbr8rSCaf70lPetBdQm7c9lDB7LwggOLeM1pzOEHTCTo56E43m0W8MDEByHnCC8huCEf7Z_b903LM-CctWvaU_CjTb_D9g_OTERzZV_zzG5YxwUurvE-FwQyPWI2QP8RgeLbwacvpXEv8-qMJSozbZKCUNk0Ru6Mqq7CMbIZYFk2mzM8GH1A_1xFyER-TAQBAI45cSenOACyzvHwnb74LMkYCfbHl7oDiXms5gPI2WAPjS6YyreAefnezkssT8wXfoj0h2Si8GBYtkqcugqVJVd4UGxb3pGGJn484cBfpnAxjHeiitUvmvVT9xXLQZrhNo6fnpXNWMx-fjs8rfo.kuKrcOjFU-ufzyIZsgH6mw; cf_clearance=Ty4h5CLWNyI2kfE0FCcDrfUrw1vQmG4VeTPhE3ECOCg-1696267616-0-1-3de43fc1.22b7ae0.6ae56021-0.2.1696267616; __Host-next-auth.csrf-token=703f705e5ba5051531954d5396f9b0e20def3ba33cdbbc8ce903f2dbc0ad8254%7Cadc6d165f3f9588bbc04117a798f6045d092c64fdd5d610bf50f2658e8ced130; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com; __cf_bm=phvYAVzZfJhkhDY3LOUAlEM_GAVaFnnQmxGXwEqxPKc-1698470558-0-AZ7Z7PG2n8GuJ596AwZJmP1XQjLJLGEqUgM0RS52sBi8xpiK7Y4s1LbXm+wefN5zjLiNsZweC9k7Ucjuqu2nvK8=; _cfuvid=57wJsqdsHZCyUR4fQokNVF7.mGUSIMfjcCqkfOYJ5yM-1698470558900-0-604800000; _dd_s=rum=0&expire=1698471482694; ajs_user_id=user-4f7zjtisgqtB4lQvyDCOUI4P; ajs_anonymous_id=317a56ed-da61-449a-82a8-52f570535c5b; intercom-session-dgkjq2bp=ZDdUdDBSa1BId3d4Qk1WZmxsYVo5Y3NPTzQwbzJXOXJRZk1SV3V5Sy9EbWFaelczaUJ6Z3F0NVNuZ0hlNm1qQi0tNys3RVZTZWJVTFhxWjFOdkVqWE4ydz09--0dd2f29aaa2671ab1d8f09d1bd87acc09add9d14; intercom-device-id-dgkjq2bp=fac1187c-85bc-47e8-837d-9066812e0df1",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"Sec-GPC": "1",
"TE": "trailers"
}


def cgpt(test):
    test=test.replace('\"','\\\"')
    test=test.replace("\'","\\\"")
    payload='{"action":"next","messages":[{"id":"aaa2d3df-a294-46f9-b03b-4f1d1c69210e","author":{"role":"user"},"content":{"content_type":"text","parts":["hello"]},"metadata":{}}],"parent_message_id":"aaa14829-a8e2-413f-bbe1-da906e5ee919","model":"text-davinci-002-render-sha","timezone_offset_min":-330,"suggestions":["Explain why popcorn pops to a kid who loves watching it in the microwave.","Design a database schema for an online merch store.","Come up with 5 concepts for a retro-style arcade game.","Can you recommend me some appetizer options to bring to a potluck? "],"history_and_training_disabled":false,"arkose_token":"12517922dff639379.5802308104|r=ap-southeast-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|guitextcolor=%23000000|pk=3D86FBBA-9D22-402A-B512-3420086BA6CC|at=40|sup=1|rid=87|ag=101|cdn_url=https%3A%2F%2Ftcr9i.chat.openai.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-ap-southeast-1.arkoselabs.com|surl=https%3A%2F%2Ftcr9i.chat.openai.com|smurl=https%3A%2F%2Ftcr9i.chat.openai.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager","conversation_mode":{"kind":"primary_assistant"},"force_paragen":false,"force_rate_limit":false}'
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
