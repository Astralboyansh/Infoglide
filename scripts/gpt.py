import requests
import re
import json

def setcookie():
    raw=input()
    raw=raw.split()
    print(raw)
cookie=""
auth='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhbnNoMTIzaWNpY2lAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItNGY3emp0aXNncXRCNGxRdnlEQ09VSTRQIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDI3MDI2OTE0NTcyOTI2MTgwOSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTM4NTQ1MjMsImV4cCI6MTY5NTA2NDEyMywiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.heQabZdQH4A4LdO-nrRlMVNCBWj1rPZd9snZYLp6WtFIBLt-MvLxCsDikOkVCZk9gD8vIGiXZu-47sDAjgoXo9ArvsWYZDMqd0IwlwVaotsamBpAxP0KBRYnoqF_WSG1WWfYzhshYZ1xwzWpGW2kJBTHHNALYxE_pOlJd5jxzxNE0SMGpTUZAeAYv899B5LkK2FrDanQw5EYRwEBUdplih_aAtV0iwuFbKPiGmby4W8dIHUOBmxDrD9AEbUzezkHnaeshFLG4MpMytWFWj8byCOkrZtGWRX1x3NKqzZqOoGSs-J2a_gpa0TP725OnxzTUevGxIbnCvF1mG_buhE-tw'
url="https://chat.openai.com//backend-api/conversation"

headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/event-stream",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://chat.openai.com/c/295acdf8-3c9c-4c36-be3a-3772e62ccda9",
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhbnNoMTIzaWNpY2lAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItNGY3emp0aXNncXRCNGxRdnlEQ09VSTRQIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDI3MDI2OTE0NTcyOTI2MTgwOSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTUyMzQyMjgsImV4cCI6MTY5NjQ0MzgyOCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.sDDPotgoFJDSIHw_MHI69R-H6k5hTrzOHYLtbv90VzdRx05stfYCpETQBSWtaxRLD916VmjVhryhKcYModQwb8h0wehzTxFUsG6n9CiroYrcM7S6aIZbAsC_LLdhQfBl35RZhji5LA-DkJ7vqhVCYpqasXBMv6fK3zpBHs7gNomyAlvENFBog1XEf-ZnvRpPa0AfafLcAAkWovcgJm8goU68WXApCBGpS5X-theUJ5zzhVEiX55oCjJASkihLYdphJuD2dR22obCxYkfVAalgLmtyNhhUfoBmgjvS14e0vRhYJP2hA5lEGjRd5HqXpKyaI4rz_K_GGwU7sa0P2WzZw",
        "Content-Length": "442",
        "Origin": "https://chat.openai.com",
        "Alt-Used": "chat.openai.com",
        "Connection": "keep-alive",
        "Cookie": 'cf_clearance=du4xUQKsO9uc21EQi3WWnTjjtQNtMsaPI8KaB6wyXtg-1695234217-0-1-3de43fc1.1f739ae6.6ae56021-0.2.1695234217; cf_clearance=3.M_MZhS.APJdqeO9F4uE.d9CZMGZWrPTYY0L1aMqYI-1694932433-0-1-3de43fc1.1f739ae6.6ae56021-0.2.1694932433; intercom-session-dgkjq2bp=Wjh6QU56NFVHMEJ1akF1Q3hKVVQ0VFA4cDJtUzE4a0pmM3FzM1A2TmYvaXZZaWJTdEZYZW9DaTFtaTNBNDFZNy0tOE1ma3E3YWxQSHhJeWQxZ2k2Zlg2Zz09--30277657a5f9d4a6e7d2e638f847612f332cda92; intercom-device-id-dgkjq2bp=961fcc48-a2bc-46d9-9b7e-4499cd9d627e; __Host-next-auth.csrf-token=34ff332bd89b883250f50553e4f0d4dec5f6c9b491c413c10d683adf4bbf545e%7C1d67676376dc48c0ca90004ac1ba47f9bf8b3cb16b10755ba6031e0bfd421133; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2Fc%2F295acdf8-3c9c-4c36-be3a-3772e62ccda9; _cfuvid=7C_ofi4QBCbDrxehsWx4ShWfRBgwrssHvmKGmcRN6.E-1695234209486-0-604800000; __cf_bm=XFj86X.yIHUCvzgYvQkgu7mFavFF.1CucTfsWYA1Kto-1695234209-0-AbOJ744auf2J8bLJ1U7pB3foGaEwlDFwrcAk0+qhauc7OVPD3rkVD6LUCDdRR507iSnQRNKkAhe02sBPIKxnP0w=; _dd_s=rum=0&expire=1695235138370; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..H6Rktnmg5VfaBci5.tMO_QkoX7gKXTu0gzeFKqfbLv-m1Umiyn4hN_MuFRX00Iu3PHFRHh-ErQNrvGlQ3J4Nd3dkjxYQKJCoZW4sToKTC1TEfrPE8G8G8-a8lCuyoMZIC-MC7EKug65NCTOVMY4ZixkDv4qiYCDBudAaozhcIotAEw6FHsmZpsQ67jlZgHHezB7AxII0XtwifZYbbdl6sE_6eMbGbW-f4Tla-PKiLw7IhqD4wnmpYhghi69SiyynQdS23Pz-rpD994jCYfMGb5TVQeOFlW8HUVH8y_wG9QWM8eONqvWTE9mxkp8XUnEuuWe-BmD7Tq7R5CnCu5r8xu3-9Hkxkjrd1kWYk951FWei-CwOHqsi5hnIGxdkliLvbFy7yjGlNQAW9_4jNLWc6cM5qJGpPbBjOh0oidKcAhoF6b7q7ObON1cuQxrA1zjru42Yo8YcCRh8gHn1mL54FdhH2_CSSe-u-nXQi6lqi9nGnWlgl37kF3Gndfd0feFcQyAEewfbowRkVPc8-xwV6MbaKx7ltYL3dm46N6ADL3qTwTvH0JI-CXMmfbRHvWXJMmC_eAM63mjlcRS4nQU_xl32osRDvraDSvPT_hb3T7v2j6CUEvbM9nKh2Bsa4crk5Xh-uzxXmP5bV4Cc7YQGPiMZPz8nbcRrUIxaYTmJL3pcFmj3tGgvK5EAzvguINWybLP9nWV5w2r0-V-mVaHSrnngwQ8esWmrVGAM7vgO0IYvvZaAi80Bcrq7HFvvP6bssWUttWdrb7oLXicrzHIapBWG5v-SAoJxNVwY25p6iGTQCWtZ7T4K5UrxFHINmM_6u0uPJINXqOoEFo76UyhqND61d9i1mFxcTvAZ5Db15RnO3sRAlDdjByvCkQ-By-cbjy48kS-yTYAGms8_bsJHlfkJg09u8G6_b-Y7bH6ghI3L5g3RQ2c_EZnDHhfw6TpL7feUmrUnM8VJNZmhNkE1rcxwL27HJPguHdSvmtCd4EM1Rt_TYk_kIraiAwSu8SQI4EsJ-Di7InIi6zP6N2ln3NZfoYZtaxPCeePgRZyPmxRixeBOlATD58N5gRgk3gfavUOEDhh9cx6U4Av7UPDIfksoCWQv7k_BEKYB4yyoo1CHfUNdlB5zLmffA79W26oXWgkYQE32YMmmIf43dfTg3RVOg8bgpe3NPzVlMEDwGHdD21LhWoJgEmifpdlhViJYbnttE7i1BN06p8EyJWvZHvWftZKEyYnOgcrx6_zJMoth2p2SeNEu3w4ndHTeP2xtyvIfERl_HsaY1G7XAKFYbOFq_djJuzmS1RBTOgCt2AnFSl14uA9BnC8LbPBxS1P9Rkj5EJjr51BFdwXmW9CQEarIh3Vxn0qL8nVJMU490Wd2stPlrcfFI-URMUEErgY10loJhWCeqD1k9SzcTEeBP3pjKrz1OAt_cn917A6lIfjLhdOygcTGMTuySoyKIQ4WKeKZInWcyZD191baep5rY6htiNAAUodJdLMGKFCCc_ZV_EpGs_0ulimh8hxWZL0WaP3QB_5tPv0pJnDi9JFo-svvQyX05Hb7s9PQPiyHqJlNGQECSApmHH685_xY9hwGiQuWMHqTG8TzHexn2Vksch6UqiZGA2VVBcOsBsw0EWcCCz-9IKQMtubxwUiVqDydX8qEShIsaV_C3icmzGnXLkVAPiIu_sbKSdybTkbjlwzbEBf7zMy0UXQYnY0LG48GCvy8iGl6qBEks8a0vlOpNsv2yDyhdgHfzuYgjqbiRpsGCxWrJ6-2axg3qqgYjyBB2dilso7T0iGOBiCAxUHcqmJ1-DHCpqI8t0H_LZrvvTSrYQoWdHVDjVRmQoDtfoJuXuIf-yr4FwMbSWRgDpqxVvJLyvpHR8RX0E70RIgfNgkidFSePQG_TFMOXydz0H-GYDYLXJa5J4nXmqS_tAyoAT2EtJjhzauP9p3f07GwIL9KKoLkVHObcXS1Epa86pift4lBHrvtdfHEOVO5ruCjWbmsMm3EzOldb5jt_Mi_3_8br83FtNrdUvcH-MQBeAjALXN6Ck97GdJj_nj6MiL1nXUbb5_y9-U_EeAXELL9EdbDkyLUWue-R_AwME7glaJxJQ9xSa4ObOl7rba0BwS5taw0VcxWbHeolh141XRSRetWsEQP3Usrxp3jZzlsd--EtADZQnyN7EwB3BPWEhfqdJ-CjNHYXDex15j7xYijWrtjP0X59n39lJJbg0sLC7_rYIjR8MmW02sC6VAYD4XIFM9DbvDKFT6mfQzoS80_3-CqAWwNxfuojDBNkSeiuu917-3tqNv3okU_tmW-AfnYY08pkuyegAao70iw5Dlm7vxKPJRF-n99b82i59BSUJ_xoe4GnjXa7Gpu1J3XIwOOb_QWF1ULCmcwNYp3EgS2jf4tLBWkOt0x_B7F6Gald7_xLJinIa58UfZkaPrOHSTQhXLx7jRmJlajrUxC0zfJtjJCndq0emuuVAsLRbzu2qEWnEv50xNi02HRy_QFtcnHllLr5k1Jnh3SAqkXrHg8dAkw6rAfkHlzA7yhEWeEE0HELFBdqnf85UHREArCBKZbNpRBs6vz4n_pDM9liB0bqOunWQ_v3xr8Pa-j4KyegK1hkLgdj55OiWhHM49QXXs5QG3T0yoCn_Waiqmjnnqnh_B6SjlZojVIqeS2qtdAwrkRnTJ08ruEJSgZ0U1yFfou7-PlqIKn3EXggrzApAZeSa61klEkSZw8nirHDnlIZ-BnluQpngFl-6ZGALA.nf1wPYgJxbpE-Zi7zsQsVQ; _uasid="Z0FBQUFBQmxDemk1SXY3b0tIOVZ5MzAwelJMMmJXUWVHOXQ5NEFGN0c1T3ppVWNHNUhvS3hEbEtPR2k3RVFCcXh6SGZhUm1zbVEzOEVjbzNTbTJZWXFCdEY3cF9pM2MydURzODhEVzRUWXY5Z1NBLThBbGlaRXNDQ2kxTVZCS0paXzdtclZkUkVoU3p2aHhEY3NHY3NjRzhMdThUNXdnckJ4YVh0WXNVdTNnckVFQWh2aDNHWjhnWk1vRWZwdWxQRXdUV2FXYXFnNmVTbGNyTndwcVdTU0FVZ3hFb0c3UlVKNkFKOFl4RlE1X01CaS1sUFVYTV9mZEZkS2dNX0xZa0NaTUZDSUMyS3lTUEdfeDRlNDEtRFFZWFMtWWluWHFNM0xYX3BldXBBMjlkMWxjWk0xeURzc2xiRlBsczQ4YVNEQ1k5U2VvWUplanMzdl9EMFl0SUt1d3ZzU2RrLXV2SzJnPT0="',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1"
}
while True:
    test=input()
    payload='{"action":"next","messages":[{"id":"aaa288ab-dd58-4c02-918e-486a45f6f7c2","author":{"role":"user"},"content":{"content_type":"text","parts":["%s"]},"metadata":{}}],"conversation_id":"295acdf8-3c9c-4c36-be3a-3772e62ccda9","parent_message_id":"e20afd97-b5c1-4d55-b8e3-a3c8d0698246","model":"text-davinci-002-render-sha","timezone_offset_min":-330,"suggestions":[],"history_and_training_disabled":false,"arkose_token":null,"force_paragen":false}'%(test)

    response = requests.request("POST", url, headers=headers, data=payload)
    parsed=response.text.split("\n")
    parsed=parsed[-7]
    a=re.search(r'parts',parsed)
    x= a.span(0)
    x=x[1]
    parsed=parsed[x+5:]
    a=re.search(r']',parsed)
    y=a.span(0)
    y=y[0]

    parsed=parsed[:y-1]

    parsed="\n"+json.loads(json.dumps(parsed))+"\n"
    parsed=parsed.replace('\\n','\n')
    parsed=parsed.replace('\\"','\"')
    print(parsed)
