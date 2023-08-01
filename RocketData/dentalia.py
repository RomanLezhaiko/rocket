# # pip install requests-html

# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

# session = HTMLSession()
# session.cookies['1P_JAR'] = '2023-08-01-12'
# session.cookies['AEC'] = 'Ad49MVGHZ6aj1S7jqpvYJhZckAfU0-oKhYMcYa25nXVO1EYagKHosoz7xw'
# session.cookies['_ga_94GCJ4Q0CE'] = 'GS1.1.1690893002.3.1.1690894721.0.0.0'
# session.cookies['_ga_FMK4KRGVF2'] = 'GS1.1.1690893002.3.1.1690894721.0.0.0'
# session.cookies['NID'] = '511=DyF6mwuNSoAF8n6PQGV7LaMGcfMeLqUc42acLIp1_X07sW4AMom-ULgIbx7SPFi7jQCKdLKZeR1mpGAuIh_-y6yAwvOVkYyv2-GNg-Qo1M_4IW0i0P1sYOeVV2T1cz23b29Dc_Ko3E6PLBssBCl_GbVkLNAFwPqL0NTD71DKp8ZWV00mfHruPOP23sAwY0Q'
# session.cookies['_ga_EN8BN980LH'] = 'GS1.1.1690893002.3.1.1690894720.60.0.0'
# session.cookies['_hjAbsoluteSessionInProgress'] = '0'
# session.cookies['_hjIncludedInSessionSample_3479833'] = '0'
# session.cookies['__hssrc'] = '1'
# session.cookies['__hstc'] = '56232756.202eaf94fe3b65683e3ecfe27b4e5862.1690886745793.1690886745793.1690886745793.1'
# session.cookies['_ga_CQX376V7ST'] = 'GS1.1.1690886745.1.1.1690886783.0.0.0'
# session.cookies['_fbp'] = 'fb.1.1690886745884.276427553'
# session.cookies['_hjSession_3479833'] = 'eyJpZCI6IjZkMDBhN2RhLWRkNmItNGFjMS05MzAzLTE5ZjEyMWY4MDhmMCIsImNyZWF0ZWQiOjE2OTA4OTMwMDgwOTgsImluU2FtcGxlIjpmYWxzZX0='
# session.cookies['_ttp'] = 'UcviFrrVqBtN-EA78WeZwKLrm5B'
# session.cookies['PHPSESSID'] = '67sbc0vkhb1vrit3rjhd5g4cfe'
# session.cookies['hubspotutk'] = '202eaf94fe3b65683e3ecfe27b4e5862'
# session.cookies['_tt_enable_cookie'] = '1'
# session.cookies['_gcl_au'] = '1.1.1898090150.1690886745'
# session.cookies['_hjSessionUser_3479833'] = 'eyJpZCI6ImMyMjFiYTFmLTA0ZTgtNTBmMi1iZmI4LWVhYzgxNWI1MTg0ZSIsImNyZWF0ZWQiOjE2OTA4ODY0MDY3MTMsImV4aXN0aW5nIjp0cnVlfQ=='
# session.cookies['_lscache_vary'] = '7f9211ff83e640e486010157d7d75cd1'
# session.cookies['_hjSessionUser_3444547'] = 'eyJpZCI6IjFlYzQ4ZGMwLTQ5YjMtNTBkMi04ZjJhLWYwMWRmMjVlZGRiOCIsImNyZWF0ZWQiOjE2OTA4ODY3NDQ5NzYsImV4aXN0aW5nIjpmYWxzZX0='
# session.cookies['_ga'] = 'GA1.1.1809879105.1690886405'
# url = 'https://dentalia.com/clinica/'

# r = session.get(url)
# r.html.render(timeout=40)

# # print(r.text)

# html = r.html.html

# soup = BeautifulSoup(html, "html.parser")
# # print(soup.prettify())
# h3 = soup.find_all('h3')
# print(h3)

# # print(soup)
# data = soup.find('div', class_='elementor elementor-5883 elementor-location-archive')
# cards = data.find_all('div', class_='elementor-container elementor-column-gap-default')
# name = data.find_all('h3', class_='elementor-heading-title elementor-size-default')
# print(name)

# for card in cards:
#     name = card.find('h3', class_='elementor-heading-title elementor-size-default')
#     print(name)

# print(cards)


# session.close()




# pip install pyppeteer 

# import asyncio
# from pyppeteer import launch


# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     url = 'https://dentalia.com/clinica/'
#     await page.goto(url)
#     print('Good')
#     content = await page.content()
#     print(content)
#     await browser.close()


# asyncio.get_event_loop().run_until_complete(main())


# import requests

# s = requests.Session()

# s.cookies['_hjSessionUser_3444547'] = 'eyJpZCI6ImQ4ZDU5ODE5LTBiN2YtNDI4MS05ZGIxLTU0NTBmMmI4NjJhYiIsImNyZWF0ZWQiOjE2OTA4ODY0MDY3MTksImluU2FtcGxlIjpmYWxzZX0='
# url = 'https://dentalia.com/clinica/'
# res = s.get(url)

# print(res.text)


# import requests
# from bs4 import BeautifulSoup


# class Client():
    
#     def __init__(self) -> None:
#         self.session = requests.Session()
#         self.session.headers = {
#             'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
#             'Accept-Language': 'ru'
#         }
#         # self.session.cookies['_hjSessionUser_3444547'] = 'eyJpZCI6ImQ4ZDU5ODE5LTBiN2YtNDI4MS05ZGIxLTU0NTBmMmI4NjJhYiIsImNyZWF0ZWQiOjE2OTA4ODY0MDY3MTksImluU2FtcGxlIjpmYWxzZX0='
#         # self.session.cookies['1P_JAR'] = '2023-08-01-12'
#         self.session.cookies['1P_JAR'] = '2023-08-01-12'
#         self.session.cookies['AEC'] = 'Ad49MVGHZ6aj1S7jqpvYJhZckAfU0-oKhYMcYa25nXVO1EYagKHosoz7xw'
#         self.session.cookies['_ga_94GCJ4Q0CE'] = 'GS1.1.1690893002.3.1.1690894721.0.0.0'
#         self.session.cookies['_ga_FMK4KRGVF2'] = 'GS1.1.1690893002.3.1.1690894721.0.0.0'
#         self.session.cookies['NID'] = '511=DyF6mwuNSoAF8n6PQGV7LaMGcfMeLqUc42acLIp1_X07sW4AMom-ULgIbx7SPFi7jQCKdLKZeR1mpGAuIh_-y6yAwvOVkYyv2-GNg-Qo1M_4IW0i0P1sYOeVV2T1cz23b29Dc_Ko3E6PLBssBCl_GbVkLNAFwPqL0NTD71DKp8ZWV00mfHruPOP23sAwY0Q'
#         self.session.cookies['_ga_EN8BN980LH'] = 'GS1.1.1690893002.3.1.1690894720.60.0.0'
#         self.session.cookies['_hjAbsoluteSessionInProgress'] = '0'
#         self.session.cookies['_hjIncludedInSessionSample_3479833'] = '0'
#         self.session.cookies['__hssrc'] = '1'
#         self.session.cookies['__hstc'] = '56232756.202eaf94fe3b65683e3ecfe27b4e5862.1690886745793.1690886745793.1690886745793.1'
#         self.session.cookies['_ga_CQX376V7ST'] = 'GS1.1.1690886745.1.1.1690886783.0.0.0'
#         self.session.cookies['_fbp'] = 'fb.1.1690886745884.276427553'
#         self.session.cookies['_hjSession_3479833'] = 'eyJpZCI6IjZkMDBhN2RhLWRkNmItNGFjMS05MzAzLTE5ZjEyMWY4MDhmMCIsImNyZWF0ZWQiOjE2OTA4OTMwMDgwOTgsImluU2FtcGxlIjpmYWxzZX0='
#         self.session.cookies['_ttp'] = 'UcviFrrVqBtN-EA78WeZwKLrm5B'
#         self.session.cookies['PHPSESSID'] = '67sbc0vkhb1vrit3rjhd5g4cfe'
#         self.session.cookies['hubspotutk'] = '202eaf94fe3b65683e3ecfe27b4e5862'
#         self.session.cookies['_tt_enable_cookie'] = '1'
#         self.session.cookies['_gcl_au'] = '1.1.1898090150.1690886745'
#         self.session.cookies['_hjSessionUser_3479833'] = 'eyJpZCI6ImMyMjFiYTFmLTA0ZTgtNTBmMi1iZmI4LWVhYzgxNWI1MTg0ZSIsImNyZWF0ZWQiOjE2OTA4ODY0MDY3MTMsImV4aXN0aW5nIjp0cnVlfQ=='
#         self.session.cookies['_lscache_vary'] = '7f9211ff83e640e486010157d7d75cd1'
#         self.session.cookies['_hjSessionUser_3444547'] = 'eyJpZCI6IjFlYzQ4ZGMwLTQ5YjMtNTBkMi04ZjJhLWYwMWRmMjVlZGRiOCIsImNyZWF0ZWQiOjE2OTA4ODY3NDQ5NzYsImV4aXN0aW5nIjpmYWxzZX0='
#         self.session.cookies['_ga'] = 'GA1.1.1809879105.1690886405'
	    
    
#     def load_page(self) -> None:
#         url = 'https://dentalia.com/clinica/'
#         res = self.session.get(url)
#         res.raise_for_status()
#         return res.text
    
    
#     def parse_page(self, text: str) -> None:
#         soup = BeautifulSoup(text, "html.parser")
#         section = soup.find('section', class_='elementor-section elementor-top-section elementor-element elementor-element-a7a4f20 elementor-reverse-mobile elementor-section-boxed elementor-section-height-default elementor-section-height-default')
#         # print(section.text)
#         names = section.find('div', class_='elementor-widget-wrap elementor-element-populated')
#         print(names)
#         # data = soup.find('div', class_='elementor elementor-5883 elementor-location-archive')
#         # names = data.find_all('div', class_='elementor-element elementor-element-706f5ba elementor-widget elementor-widget-heading')
#         # print(names)
    
    
#     def run(self) -> None:
#         text = self.load_page()
#         self.parse_page(text)
    

# client = Client()
# client.run()



import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://omsk.yapdomik.ru',
    'Referer': 'https://omsk.yapdomik.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'sentry_key': '3f6061fa6b5e48efa67fece896a5e39f',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.vue/7.37.0',
}

data = '{"sent_at":"2023-08-01T14:00:40.925Z","sdk":{"name":"sentry.javascript.vue","version":"7.37.0"}}\n{"type":"session"}\n{"sid":"d1e139039e0e4f3e9b76c419becd3c9b","init":true,"started":"2023-08-01T14:00:40.924Z","timestamp":"2023-08-01T14:00:40.924Z","status":"ok","errors":0,"attrs":{"release":"15964503f0ae97cb7f51f3ba35637997d3e270ce","user_agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}}'

response = requests.post('https://sentry.sushi-market.dev/api/9/envelope/', params=params, headers=headers, data=data)

for msg in response:
    print(msg)
    
    
# https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python