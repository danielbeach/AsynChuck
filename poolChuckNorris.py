from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import requests
import json
from datetime import datetime


BASE_URL = "http://api.icndb.com/jokes/random"


def break_into_chunks():
    listy = range(1,201)
    chuck_number = len(listy)
    final = [listy[i * chuck_number:(i + 1) * chuck_number] for i in range((len(listy) + chuck_number - 1) // chuck_number)]
    return final


def convert_to_json(response):
    jsonified = json.loads(response)
    return jsonified


def chucks_backup(joke_number):
    print(f"Working on Chuck Norris joke number {joke_number}")
    html = requests.get(BASE_URL)
    json_response = convert_to_json(html.content)
    if json_response["type"] == 'success':
        print(json_response)


def chuck_em(joke_numbers):
    with ThreadPoolExecutor(max_workers=6) as Backup:
        Backup.map(chucks_backup, joke_numbers)


def main():
    t1 = datetime.now()
    joke_chunks = break_into_chunks()
    with ProcessPoolExecutor(max_workers=6) as PoolParty:
        PoolParty.map(chuck_em, joke_chunks)
    t2 = datetime.now()
    timer = t2 - t1
    print(f'Process took {timer} seconds')


if __name__ == '__main__':
    main()