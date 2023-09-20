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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhbnNoMTIzaWNpY2lAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItNGY3emp0aXNncXRCNGxRdnlEQ09VSTRQIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDI3MDI2OTE0NTcyOTI2MTgwOSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTM4NTQ1MjMsImV4cCI6MTY5NTA2NDEyMywiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.heQabZdQH4A4LdO-nrRlMVNCBWj1rPZd9snZYLp6WtFIBLt-MvLxCsDikOkVCZk9gD8vIGiXZu-47sDAjgoXo9ArvsWYZDMqd0IwlwVaotsamBpAxP0KBRYnoqF_WSG1WWfYzhshYZ1xwzWpGW2kJBTHHNALYxE_pOlJd5jxzxNE0SMGpTUZAeAYv899B5LkK2FrDanQw5EYRwEBUdplih_aAtV0iwuFbKPiGmby4W8dIHUOBmxDrD9AEbUzezkHnaeshFLG4MpMytWFWj8byCOkrZtGWRX1x3NKqzZqOoGSs-J2a_gpa0TP725OnxzTUevGxIbnCvF1mG_buhE-tw",
        "Content-Length": "442",
        "Origin": "https://chat.openai.com",
        "Alt-Used": "chat.openai.com",
        "Connection": "keep-alive",
        "Cookie": 'cf_clearance=cA3EJayyodCiEFVZtNPPCyjdMwvJXooMBE25ahZSM_k-1694989608-0-1-d3261aab.1c84a7d.8427454b-0.2.1694989608; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..OAEglpNiLGR7a-_v.jG3yGNMvCuya3Nh6J7J-rmvPjbz5Iqz-H2WlUaUtY4aVzF0YmAoUbjXUfd7OCrApgXMvCUNDaeLQOY7wChJbZYLgh6B1aDjvWWHMrrCS_Ic7yTNw31iDZcNvLbuQv44fckgAXU9UjpZSovALCsabVhPprqQDPLqy1_Cut--fqx_tZFWGPIu1OHJNrhv5ZMUu1kSsVakhONGXla5jv8Ncm7_G_J7LlAKi2-O5l70dXo1B5A8TfeuDnGPhQOtVItlb61Kj_jixUSZO8fmByb6rxZdkIchqTkMe5nZzrOaOVtAgLwgUswhu7LrX4OQIYKXhl3n0UK43M-CAv6uoUnPinY-zNJdEz4y5LQk-KMsWB5y8TLMInDls2X-dylFssFaW0YgPqhhsT4FR7wtUjVujy9aQrW8sDUTj8bpzYwCzvi7oA0BsWJDS9FdXBkY8bBBMy8A5jb0LYmATsF8H30Ol02FiJHZqzGFCpMtrRR1Xy1mgcJR4VZuoqbziSxpunTUgiH9kK0-acN6cSq0xjkNXt8urlnz81BRcf9rCMOSeueB-ASxOIUCMSUYpgx63YHTLl2xLQ8e2M0eof5FNtZhfgDLIMHL3exwpMVHNEXsm7F6T0Cx2XkPiQVWdacrUSwk_vH626zz7EsT_qd7PkPRvKxGIPnZ9Y4ML3Nmq-cjE3Nn1SjYNK7DB4Li9DgsVhq5seXiXKochuS2saBjm8hDoSAvZvQxMrEf35iLUWQ6FgWvjJxdRjSbtU7bm5855PwemlJohSt0JY3_PjafbmMYRqZU_6q_UtqsYbmOXEg_UbuZ60WUZ8i7q5zEb1VadQHb8dqU8WrVUaEo_XoI0aLddAvOTNeQ_QW9LIKH_POoXhK5hyxGZOK1WCE2JAzFz7CfjK73SzPa81pRQTpKNbYCpnopgV8dMTFr7iVITvcY4IzRdj4ubHqr8Nh7X8hx7Mim4Sum6Jwov4QCw4FqJ0_hFzuUJIdVllTqBY60DrDll-i458jvw_lbHAILKL_N9c4OZlcfjwTAlmxugTmZwIiQAHSDrbxDNx8E2MP7qU3nhF1sF0AMX61GcOTKIrpIfUBj5A3qonnYrVXJer0HbMoxUKUhCriLf4FNhr0oHQWl5sFyoczTDYtOdFM8gGZ4nmQcWpYTCJ3F8PBVgK16VGeRqYAwaKN4m0S1ftyMVjKE2SogDa5XWTgN9a7sd1D1E8kgEuH2Cv_v8Yvxh2_e4Z-bfICIWC01tvJ7-1rlb77aykir6udPnx__k0UtkeektcdWY2KnArBahzmlEfdMnyPw07pYgsorAufq-VxKSFtsH2osr1igPfVc_CUgsO77ueIbwI-3aOZkP8VYw0Vm79h46uOqarKpkHo2QzsOg7Qsm6kK2brfSKgfgHLoOuMgM6-hH3RKnJsn6N5wUDFpIelBGVyC7fJ5QYM4zcSKMmL6iyLzn6oLJtED_J7trXUXXwlahVHdRyBE-UHZeeaXI0-LByxAxDgiGdCLMftXwz_csa0ZBkxP2GiXl11DVNGVpaNRwkAHAejuv-4WWIk_EQwmFQMFpozeexfg6vgwhl1ZWzOIR3PbiVj7K-dP6vyLAouPp32PeQMm1qurMXMkFn3YObrtghIPxryBrppKAfpcjmxanX1xJWVqswe4Ehd62poB61jNYmR6C1v5unXMfsZgvKfaYLZp213tyEJqZCzGqPuWvruAAOIepTuenRHG27r4hAPQ6MuVooFXI8xdgn3moCklL0zh60eGRLA6MA1MBIR8g9ylrqpYrXn_NoMqMCAM2lf_kbXTHxbGIw9GHv2e13TsWnRbDZD3XjUgHlNWWNk56dhjRWgv4eFdNE5SbiIQdy8JJtUKol4CBbuO1cxafMaZ9WizKYMHcWZnhD2ea6_2Tq8OeabHNt8nCYHBvTvZEC3fWzzWz-v7RN0o2NRpwrRv7QikkPkmm1xDj8n2riY8l94tc_im7dXYWQLh7IbTFidFxCU8T5IEu8ECNRr12oA7QCyiuYzUvCgomLl95o0E_e5sdVb4lSvN7kKvmh-7K8U-NmWgkyanRZLiE6xeOFWTmTjGhaK3zSu8yM5MCknSeGRE4vhjzSi_lpHmAkDJ-lPR9dO0Blcu7WqkF9inGK5fNxRzLsaZxkyKYp2YV0Orc8JVo1RKMT69XIYGuQewCP6I9A7xv6gz8rzbhBP8Uycr6X30HogPyTceSWypOToKS4c5liqaSOtkvvwZ30FWVTlqxxYhywne2_JNqxT-E8k8FO9c4cl72k9YHnaI9S47e4iRYPVaOAf6JInO0apBxi1uD3CK_CiPGbb8DCIMd_0ZE9u455rZub4V0C1arkC3PQcHAPuyGl2Y7EOZoP3vguGloyDKMn7YIMKWvRJwGkDSzpwkwDmaB0rOBEQRbpaLit6ZTEvnJENkbyOy2X_1VN6WOsnYcqi9TvPv-b7ntBkt4eh5JtMfNqTJnjS8-y-EByFqABwOZS9BlMOdfzDlMKnvqmPPpBvOobzkanh2dXYDmtmYBEkc8YOKP007Ocn57EpXhjwPrty73tkBZIT1l2NXumOuyx8FMMm0A1Z60KPnKUmQBUARRZrckS2Ui2_3-z9hZR7-gMK1uuNbymOpnmq70TYMWe6WnSPDVbCI5shr_owF_i7a_3nB5pkNEciiMBAQN5SeGX9UH529G8KtjUHl4C1pIeYe7242EBhDtZBffc5po_QPL-zetOD5I5mtYLKyMJdFTXquTsnIVIg.zUVQM8HgXGq-FxfMaMoIaQ; cf_clearance=3.M_MZhS.APJdqeO9F4uE.d9CZMGZWrPTYY0L1aMqYI-1694932433-0-1-3de43fc1.1f739ae6.6ae56021-0.2.1694932433; intercom-session-dgkjq2bp=aDh1RnQ3bHZpYkRsb2xjSVpsSkN4S0lsaFVURjRCTWhsUU10SVJ5QTI2OTBMeWFOaGcvL2hkYnNtTjlod3VGbC0tN1I1STBoS3dHc0cxZDNSQzR1ckc2dz09--bebb1e44ba7d20ff322e2d5fa56f9b53cfebca1b; intercom-device-id-dgkjq2bp=961fcc48-a2bc-46d9-9b7e-4499cd9d627e; __Host-next-auth.csrf-token=34ff332bd89b883250f50553e4f0d4dec5f6c9b491c413c10d683adf4bbf545e%7C1d67676376dc48c0ca90004ac1ba47f9bf8b3cb16b10755ba6031e0bfd421133; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com; __cf_bm=WArZofaRlGErBnVfjWQL3VQke2uhD29HaQ9AliOsPqQ-1694989602-0-ASyWJEJrqWVJfRMQezqZ6YM0WL+V0zZ0RIMxieX5ZLqkTGhBjT8g0hkM9iFXQ1nSfxFYAK3JbYLI1daLIXY/4Ho=; _cfuvid=.kqf2AZ8h4PGlSycX0tTNf4dc0Ndo3rmb17THc5k4tU-1694989602408-0-604800000; _dd_s=rum=0&expire=1694990557929; _uasid="Z0FBQUFBQmxCMzBrbmNCempvVWtfeEw0WWp4d1JJVkg4UElIWVIwX3hvWVM0YmxuQlBDQ1VjS1dUa2ROdld6VWY5RXdsR0g2blprUkRqTXlNUVdCMDJ1V2JqdFZQWkg4N1hkV1k5RVc4TFNFZmtXTlY0VElZbWdKRGUzV0Nxa0RSZ29jRXA2Wk5lb1RsTDhHZDNjQllVUXRvWTItbTVlTndVZGNNZjhaWnJ2bUR5cmRLQXZWOGs3SzZPRGJUZWloeEFFd1JLRDJlcUZDOGRDY2d1bzlzM1R3cmJXbGZiaFJtUDJncy1KT0dCRmxGYUFNcWZlWU1WUzFWbTk1WGRyZGtxd2I3RlNRaE9ycGt3YmkwN2ZkWC1VQ1RLOUY2UTRzZ2FKNXhVUVcyT1RjMEVkejFsN184UUw0clZuMXRZVVNUM1pHbmtIeENSZ3ZwTkdtcmRNTmFvaDBGekJ4QTQ2cnZBPT0="',
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
