import asyncio
import aiohttp
from datetime import datetime
import json


class AsynChuck:
    def __init__(self, number_of_jokes: int):
        self.base_api_url = "http://api.icndb.com/jokes/random"
        self.number_of_jokes = number_of_jokes

    @staticmethod
    def convert_to_json(response):
        jsonified = json.loads(response)
        return jsonified

    async def fetch(self, session:object):
        async with session.get(self.base_api_url) as response:
            return await response.text()

    async def get_em(self):
        async with aiohttp.ClientSession() as session:
            joke_number = 0
            while joke_number <= self.number_of_jokes:
                joke_number += 1
                print(f"Working on Chuck Norris joke number {joke_number}")
                html = await self.fetch(session)
                json_response = self.convert_to_json(html)
                if json_response["type"] == 'success':
                    print(json_response)



def main():
    t1 = datetime.now()
    MrNorris = AsynChuck(number_of_jokes=200)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(MrNorris.get_em())
    responses = loop.run_until_complete(future)
    t2 = datetime.now()
    timer = t2 - t1
    print(f'Process took {timer} seconds')


if __name__ == '__main__':
    main()
