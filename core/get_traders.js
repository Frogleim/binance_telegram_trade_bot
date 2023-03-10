import fetch from 'node-fetch'
import fs from 'fs'



 async function getResult(type)  {
    const response = await fetch("https://www.binance.com/bapi/futures/v3/public/future/leaderboard/getLeaderboardRank", {
  "headers": {
    "accept": "*/*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "bnc-uuid": "25577671-3e75-44e5-8e98-9d980653b090",
    "clienttype": "web",
    "content-type": "application/json",
    "csrftoken": "d41d8cd98f00b204e9800998ecf8427e",
    "device-info": "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoidHItVFIiLCJ0aW1lem9uZSI6IkdNVCs0IiwidGltZXpvbmVPZmZzZXQiOi0yNDAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6IjIyNjYyZWFiIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKE5WSURJQSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChOVklESUEsIE5WSURJQSBHZUZvcmNlIFJUWCAzMDcwIExhcHRvcCBHUFUgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL1llcmV2YW4iLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTEwLjAuMC4wIChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiOTY5OThhNjI4MzRmZDlkODJjYTFkNDFkNTVlN2MxZDQiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==",
    "fvideo-id": "3333e7218ce8ab04967a34ac7bc9a13086634acb",
    "lang": "en",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-trace-id": "d7c531b8-a503-4ce7-be3c-914b6079358e",
    "x-ui-request-trace": "d7c531b8-a503-4ce7-be3c-914b6079358e",
    "cookie": "cid=M8HN64zN; _gcl_au=1.1.1542318403.1678194258; bnc-uuid=25577671-3e75-44e5-8e98-9d980653b090; monitor-uuid=7b89657a-5ed0-4ffe-a2a9-4bad8180fbe2; userPreferredCurrency=USD_USD; BNC_FV_KEY=3333e7218ce8ab04967a34ac7bc9a13086634acb; BNC_FV_KEY_EXPIRE=1678215859835; _gid=GA1.2.880426425.1678194264; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186bc2c4edf358-010a76f99bd8f35-26031951-2073600-186bc2c4ee0143e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2YmMyYzRlZGYzNTgtMDEwYTc2Zjk5YmQ4ZjM1LTI2MDMxOTUxLTIwNzM2MDAtMTg2YmMyYzRlZTAxNDNlIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22186bc2c4edf358-010a76f99bd8f35-26031951-2073600-186bc2c4ee0143e%22%7D; OptanonAlertBoxClosed=2023-03-07T13:05:10.378Z; source=referral; campaign=www.binance.com; lang=en; theme=dark; _ga_3WP50LGEEC=GS1.1.1678194263.1.1.1678194622.56.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Mar+07+2023+17%3A10%3A23+GMT%2B0400+(Ermenistan+Standart+Saati)&version=6.39.0&isIABGlobal=false&hosts=&consentId=a700cfbf-4ef4-4965-8f9a-c7e0d63afd40&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=AM%3BER&AwaitingReconsent=false; _ga=GA1.2.1228483097.1678194263",
    "Referer": "https://www.binance.com/en/futures-activity/leaderboard/futures",
    "Referrer-Policy": "origin-when-cross-origin"
  },
  "body": `{\"tradeType\":\"${type}\",\"statisticsType\":\"ROI\",\"periodType\":\"DAILY\",\"isShared\":true,\"isTrader\":false}`,
  "method": "POST"
});

const result = await response.json();
const jsonData = JSON.stringify(result);
console.log(jsonData);
fs.writeFile('response.json', jsonData, "utf8",  (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Response saved to response.json file');
  });
return result["data"]
}


const args = JSON.parse(process.argv[2]);
const data = args[0] 
const result = getResult(data)
console.log(result);
// process.stdout.write(result.toString());