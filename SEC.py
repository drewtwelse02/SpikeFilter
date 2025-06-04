from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import asyncio
import aiohttp
from datetime import datetime
import pytz
import lxml

url :str = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=&company=&dateb=&owner=include&start=0&count=40&output=atom'
url_8k : str = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=8-K&company=&dateb=&owner=include&start=0&count=40&output=atom'
url_doj : str = 'https://www.justice.gov/news/rss?type=press_release&m=1'
user_A = UserAgent()

print('<< SCRAPING SEC 8K >>')
old_headlines = []

async def GetData(session, url):
    async with session.get(url) as response:
        return await response.text()

def GetTime():
    current_time = datetime.now(pytz.timezone("America/New_York"))
    now = current_time.strftime("%H:%M:%S")
    return now

async def Scrape():
    while True:
        headers = {'User-Agent': 'VNK Capital kesney@vnkcapital.com'}
        async with aiohttp.ClientSession(headers=headers) as session:
            webpage = await GetData(session, url_8k)

            soup = BeautifulSoup(webpage, "xml")
            print(soup.text)
            # headline = soup.channel.item.title.string.strip()

            # if headline not in old_headlines:
            #     print(GetTime(), headline)
            #     old_headlines.append(headline)

            # title = soup.entry.title.string.strip()
            # summary = soup.entry.summary.get_text().strip()
            # time = soup.entry.updated.string.strip()

            # if title not in old_headlines:
            #     print(title)
            #     print(summary)
            #     print(time)
            #     print()

            #     old_headlines.append(title)

            await asyncio.sleep(5)


asyncio.run(Scrape()) 