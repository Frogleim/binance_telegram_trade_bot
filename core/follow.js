import fetch from 'node-fetch'
import fs from 'fs'

async function getPostions() {
    const response  = await fetch("https://www.binance.com/bapi/futures/v1/public/future/leaderboard/getOtherPosition", {
        "headers": {
          "accept": "*/*",
          "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
          "bnc-uuid": "4da27b9e-9ee1-4005-bd5d-5d90814bcdff",
          "clienttype": "web",
          "content-type": "application/json",
          "csrftoken": "d41d8cd98f00b204e9800998ecf8427e",
          "device-info": "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiZW4tVVMiLCJ0aW1lem9uZSI6IkdNVCs0IiwidGltZXpvbmVPZmZzZXQiOi0yNDAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTExLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6IjkzYjZhY2I5Iiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKE5WSURJQSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChOVklESUEsIE5WSURJQSBHZUZvcmNlIFJUWCAzMDcwIExhcHRvcCBHUFUgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL1llcmV2YW4iLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTExLjAuMC4wIChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiYTE3MmNlOTAyMDBjNzU2YmY0NmFkZGE1NjczY2Y1ZmUiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIxNjc3NDA0OTM1MjQxeVNqTXZOd01Qd2NzN0JnYkk2QiJ9",
          "fvideo-id": "33645e3ce44ca5508f840e854d3987204e1ef25a",
          "lang": "en",
          "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"Windows\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "x-trace-id": "9c8c9f99-24c7-4a62-bdaa-bd260d312338",
          "x-ui-request-trace": "9c8c9f99-24c7-4a62-bdaa-bd260d312338",
          "cookie": "cid=WSWXEMvt; BNC-Location=BINANCE; OptanonAlertBoxClosed=2023-01-25T16:31:31.897Z; __BNC_USER_DEVICE_ID__={\"2f4ffe7625ae747b9ccfac992798b7e2\":{\"date\":1677404935497,\"value\":\"1677404935241ySjMvNwMPwcs7BgbI6B\"}}; bnc-uuid=4da27b9e-9ee1-4005-bd5d-5d90814bcdff; source=referral; campaign=www.binance.com; _gcl_au=1.1.1413447064.1677418526; userPreferredCurrency=USD_USD; fiat-prefer-currency=EUR; changeBasisTimeZone=; BNC_FV_KEY=33645e3ce44ca5508f840e854d3987204e1ef25a; _gid=GA1.2.1919903588.1678180125; se_gd=hcOAgRgNRFXWVZQ5bAwRgZZHgFRcTBQVVoQddUEVVlVWwFlNXV9d1; _cq_duid=1.1678180523.jskxrGmb0Z4q3M6f; se_gsd=BwAiOyhmIjo2BiwxIwMxCgAqCQcaBgQYU15AW1RXVFlTElNS1; _cq_suid=1.1678275695.ofw1JWEkw9rDDwAs; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22462266685%22%2C%22first_id%22%3A%221868def78f95b8-0b5ff0448c2f7a8-26031951-2073600-1868def78fa1660%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2OGRlZjc4Zjk1YjgtMGI1ZmYwNDQ4YzJmN2E4LTI2MDMxOTUxLTIwNzM2MDAtMTg2OGRlZjc4ZmExNjYwIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiNDYyMjY2Njg1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22462266685%22%7D%2C%22%24device_id%22%3A%221868def78f95b8-0b5ff0448c2f7a8-26031951-2073600-1868def78fa1660%22%7D; monitor-uuid=f247fff8-dab7-41ac-a5f0-698dde775421; BNC_FV_KEY_EXPIRE=1678406817306; se_sd=VMGUwBBxbHACRYHIOGxQgZZCQARYVEWUlAIJcVEJVlXWwDFNXV9X1; _gat_UA-162512367-1=1; _uetsid=c7f78260bcc711ed9f96e11617b977da; _uetvid=498787e0b1e211ed84162192f87923d1; lang=en; theme=dark; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+09+2023+22%3A22%3A14+GMT%2B0400+(Armenia+Standard+Time)&version=6.39.0&geolocation=AM%3BER&isIABGlobal=false&hosts=&consentId=fdfb3e9d-c56e-4bea-ae71-a3cf3825d1f4&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; _ga=GA1.1.715125311.1677418525; _ga_3WP50LGEEC=GS1.1.1678385217.10.1.1678386134.51.0.0",
          "Referer": "https://www.binance.com/en/futures-activity/leaderboard/user/um?encryptedUid=563E68C9500A9A6ED60728058172D7DF",
          "Referrer-Policy": "origin-when-cross-origin"
        },
        "body": "{\"encryptedUid\":\"563E68C9500A9A6ED60728058172D7DF\",\"tradeType\":\"PERPETUAL\"}",
        "method": "POST"
      });

      const result = await response.json();
      const jsonData = JSON.stringify(result);
      console.log(jsonData);
}


getPostions()
