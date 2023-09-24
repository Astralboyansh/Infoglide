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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhbnNoMTIzaWNpY2lAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItNGY3emp0aXNncXRCNGxRdnlEQ09VSTRQIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNDI3MDI2OTE0NTcyOTI2MTgwOSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTUyMzQyMjgsImV4cCI6MTY5NjQ0MzgyOCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.sDDPotgoFJDSIHw_MHI69R-H6k5hTrzOHYLtbv90VzdRx05stfYCpETQBSWtaxRLD916VmjVhryhKcYModQwb8h0wehzTxFUsG6n9CiroYrcM7S6aIZbAsC_LLdhQfBl35RZhji5LA-DkJ7vqhVCYpqasXBMv6fK3zpBHs7gNomyAlvENFBog1XEf-ZnvRpPa0AfafLcAAkWovcgJm8goU68WXApCBGpS5X-theUJ5zzhVEiX55oCjJASkihLYdphJuD2dR22obCxYkfVAalgLmtyNhhUfoBmgjvS14e0vRhYJP2hA5lEGjRd5HqXpKyaI4rz_K_GGwU7sa0P2WzZw",
        "Content-Length": "442",
        "Origin": "https://chat.openai.com",
        "Alt-Used": "chat.openai.com",
        "Connection": "keep-alive",
        "Cookie": 'cf_clearance=du4xUQKsO9uc21EQi3WWnTjjtQNtMsaPI8KaB6wyXtg-1695234217-0-1-3de43fc1.1f739ae6.6ae56021-0.2.1695234217; cf_clearance=3.M_MZhS.APJdqeO9F4uE.d9CZMGZWrPTYY0L1aMqYI-1694932433-0-1-3de43fc1.1f739ae6.6ae56021-0.2.1694932433; intercom-session-dgkjq2bp=MEZyWFJwUkh4WXlCUDNkMk8wNU1oTmZpdko1UzBobVFsbW5WMk1abzFRc09uNkQrNEhYVUdXZ0FPOEo0R1lTYy0td0UvRnc0VkhPeWhNWDFwamZYUUVoUT09--5b71a7aac603ded54368e88461e63c9e5dea3d36; intercom-device-id-dgkjq2bp=961fcc48-a2bc-46d9-9b7e-4499cd9d627e; __Host-next-auth.csrf-token=34ff332bd89b883250f50553e4f0d4dec5f6c9b491c413c10d683adf4bbf545e%7C1d67676376dc48c0ca90004ac1ba47f9bf8b3cb16b10755ba6031e0bfd421133; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2Fc%2F295acdf8-3c9c-4c36-be3a-3772e62ccda9; _cfuvid=y0yhpD0flFU.A2LBzhf9lROubO6EcdC.e51UHHwHs.Q-1695322089651-0-604800000; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..MvBq3nJlMMbBUlqE.c7SbUIlEBq6Dk2KXOoZeb_hTFu9dfrn5AeJoZiD_4XoVDnpT1dbV4Bs1dFSmHKTnXcMNC18JUE3yCJ49ICuOA_ljBN3kXsFPka1BB_cNRuhZI3xbmOairGAot55Ir-K1YAb_btoiLjmmboYmJOGmEJZZBo42ySvJ-TRrZVXi42BLBQn10lExvXSEpQmMjlH98fQTa2P8r2gRWS0YzFsfXcRmacdF6hbUxmThsIKuqcAacenpIyzINBQGFSUJZbj6hNLZjPBCqvuMYx-4AOEauR0cEVY30Au9_ykdQPQ_b8-3CZmg5MKkFAjofPSQN1DySq5BgBoNMel4XqK7b6dKt7hw4fVG1JhOMCjqzr-_WkUFpZCNe4pMIwi0TZkLjrvcjznswPrrae_pttvN-41OUQjWZ_Mrb8FqiSpf0AWyrWuVFmfiLKvI_wypJPDkLSZPGQTUqwkIRPnhVvyhCZBwiigbBxCfHgBqDcZWl9F_FDIJ0QcbrKRmm4KRIeDFf4WSGOA_8AKwffBIUgQ62GWaE5x8r6S9bu13swWdAKYjkIHQV8x0GuqIny0dambYgrdC1IWkJhxWmfCqLuHt3tC36ZmKyEr4qHZDDqZEyILGoQ_r5na1lXqgPjc_ecPqs08mJq3Q4AJvXrel6GI1qURlaecSaryFlTBgInvnY9AJN5Q2BWeVVHJF3_o8stoiYVxlBAFucwHfHZKoDucdiTVfvwCWS4nuIkMjBmrCTS8CAJwPCg9vtErbyl67tZO11Fm8qdGJ8KUantlNDhxROsrMzUZbuVKYdqno2NE3V8I6IsvfR3L8TCB1hW4a3TEABcVdyzpqxNotS-uN9ulwRRsksVlrSXsT6SPNSLukg8bhrPUR7wBH7Y5yooHGsk7BzKzMpQcNiRUtowfKpdkdDkEZiQ_nD__6LXLxXTqBlqzRhDAsXhyqKvW_PytWEaaZDO8BV9rDOrIy93mHKce9yq495TdmHTr8ZDz1abow6NnjM-PzXDFwBnuKt6AOAYYgTBfczDRjVasnsQ4hjFmE0pSwm3tsreUaewe0eWBc5OAhC2VJ_kVk8JylCUWegVOs1dwA-UTvkMRmY8JlLQYHna5C_yMySKXp40nTc6u9X0DXJD3HzTNAlXwbZNHlEEx6gOP6LG6DymLenwbNr2wyXqRUNmNGK4EGPRapvEcNz_6AnIfdxNLy_nI7RzUuMP9crmCIWi7kICYqHISJXQBZsPb6OWD_VwBNVCQjuf1Fr2lMd93yQtmfmSjzoXeJRSEgM6Ru9pTezeJjIRdXyHpYL-8f0A3-9os8wIQ0pFo0YFCaheITAkH1BJ7eaT87WUrbDFCH3pZzbNFJsKVe2q27mO-olkTwHC16XUFZ8qbjDFr0ISSvF4RUY4KKppQuXvO0iTx491zua6b6EGJMiKCm-Q01Blb3aqVVrNEj32XbffACNAUgJaLhW5YNRNJA_RWOMc9lXlsExEYlrc-J8Int4TVkWlhhvNnQnld7NVbIspipHOfgUjvou_9q6XgVefPlRF5kXyYCG5vFVOtsxlNr29qpQot8bLTZwYKR1_6OJrntsOhvTFJnYppjPK6-x6kpA-6bDrSY5HtM3sywazN9t_Uqeb35mp-Ll2z9UNBGMKG9QifeaDlAemVYlfAxpeYgvbobWSbLXh-nVbw7GJ_eHS7OS-jpLBOPoEM5bXv0yK4-yPPQJ80H_r_xDCEnaBozOIYyLgW-UhqazxaUo1T50939JS6MvmsdGeaDIK4r9Ig09Mv8q0-t93SD9p1KMhJ9J5fUXMeA0xg0uBNPFZC_4ce0iVvWF2-XaYlo02sVO0RRxiatlWKXZHU5_7l53nQk8EyXyKP-STOFNcb1xJG1OJSPjPRhfCyEwaca1HhJDfErpAlKcJpnnfxZ3xMiWVIpfmnWr31Q3_ozU8-9LPOKRN-mTham-5AXBdwSKZ5hlb9_bOpSEGcwo1Y_HVOYcAyY9j6hrSEcsu2cbbNixGYJc9TU64PGOCUS4ZG0zG07NFjUaEyrHPdXCWovJxd8HaGJXymTznW12pIt9I3YC6rfCaH3mP6smSEfbus240-xnzJr7wmFR231FUzJ3z0nVHX0NH0RnkvrXFUthtgfdTNLchMG0NpzlY0ajtvi_BmR2FgJ0ABLNq4PrJuS3J4Ep_YzycH1QVNqUBslVYiWuStOPWf0kIzMSxbffR5FIskyfouqHCEW6FKEym6SX-v6vU8qvo2u_XEW8ptYQjnV8iPpAdqsoelfhBQqbHkAvLqNlM30R9RcYu8KFzbO4URLbKMj0ECf7aWqUlWN2CgyGRQ1nhBL1XD3OSgTjW_840JJnDOMTXMX8Fl204N0C1n3Ai-a1cRWkSQCRxxDVF0vu6Bh9vFtGN9yPfdpJLlNHm4zkSEnI2IQq4qb90o2ipn_qH7MhL0uWYDmnqn_Qkn4tuw5r60dytixyUOaKdYGd5i1D4prJ2R8VFKdI8kxsgm5RqSQp1jlyKfVL_0wkrushGSjziPQ9IYFXJU-Lzmh0obxANJcs8HikO9g_Slkh1-rliroH5YQRCa-rVAE3lV-AjMNm0-amXfbR1OGIZeS8sNzC-l51PFCTv6SjoQVbCPs1nFW96fI56Wg_lQrxJd1mcA_7VGURaaW_XpjXzZe6EYQChJ8iUR-nN_pQ4qYmEQDAeS-rPCqRZB8-HFVJDhl51sxk-DmQu6sSyIUawGzmzo3NQ9oSmICu70wClfxrDF_QPfVzA.WtBLJ12o3yZEyXE56EOQyA; _uasid="Z0FBQUFBQmxES2lfMFVKb3RKcklKTWNTWHpab3NtZXM2M0lfbVNISzFPRkFlOWtzVkdXVnY4WHpKT05aLVpuenZGU09LN3VvekdDdFhWUXNmX1Zkc1FURXVXak1wSGRSMVNsMHlEUmVReFNhRzlfRTNkejhqc2VkNjQxa25fc2pVZFdMZkctN2dOUjJncml4MEN0Ny1BNENNWTQ0MXFOVHdIUC1NSEVzSm1DMW1vQXM1aXJrUzBaR2FYd0ZnOXpLdmJxcTg1WWhCQWozX1ZkamVOUFllaUFSc3VpWndQTVdQa0l6ZGtKbjgwT2xMUE1WU21CelFtNWpGTkNTSHNKWFZTRUJDZFVPZ2hYUlR1MWJNOGxyRlkyRVItcmJZM1V2WjFQNmxDRXFmbC0wRVRsbzJaRzFsc0IzT1hySVM2WFNCOERJUlNjMUU3QjVMN2h1RGJDaVBNVjlIZVpDa05JcF9nPT0="; __cf_bm=Jix8UmwDTxg1BSw.Q3D2nWJEkd7ZSCveSQ.JtmdB95E-1695328447-0-AQxjOk4oPYvr+QBcnzRK6vTDB7jGTU9iSPubz6z1cRMdgD9eVZyPvH8iEU7yjiyURrq0eg3+WpIy9DAj3k23SKg=; _dd_s=rum=0&expire=1695329354073'.encode("utf-8"),
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
