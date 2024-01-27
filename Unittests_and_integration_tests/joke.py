#!/usr/bin/env python3
import requests

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = 'http://api.chucknorris.io/jokes/random'

    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        print(response.status_code)
        joke = 'No jokes'
    
    return joke

if __name__ == '__main__':
    print(get_joke())
