
import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

# Temp hack-up of bot's dialog
with open('chat_bot.json')as f:
    bot_dict = json.load(f)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log('Recieved {}'.format(data))
    # We don't want to reply to ourselves!
    if data['name'] != 'dev_bot':
        #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        # send_message(msg)
        if data['text'][0] == '!':
            value = data['text'].replace('!', '').lower()
            if value in bot_dict:
                if len(value) > 4:
                    msg = print_player_stats(value)
                    send_message(msg)
                else:
                    msg = pretty_print_all(value)
                    send_message(msg)
    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# helpers

def print_player_stats(msg):
    if len(msg) > 4:
        user_name = bot_dict[msg]['userName']
        fav_pve = bot_dict[msg]['favoriteWeaponPve']
        joined = bot_dict[msg]['dateJoined']
        time_played = bot_dict[msg]['durationPlayedPve']
        fav_pvp = bot_dict[msg]['favoriteWeaponPvp']
        raid_clears = bot_dict[msg]['raidClears']
        kill_death = bot_dict[msg]['kdPvp']
        msg_out = '\t{}\n'\
            'Date Joined Clan: {}\n'\
            'Time Played: {}\n'\
            'Favorite PVE Weapon: {}\n'\
            'Raid Clears: {}\n'\
            'Favorite PVP Weapon: {}\n'\
            'Kill/Death ratio: {}'.format(user_name, joined, time_played,
                                          fav_pve, raid_clears, fav_pvp, kill_death)
        return msg_out

def pretty_print_all(msg):
    return bot_dict[msg]

def log(msg):
    print(str(msg))
    sys.stdout.flush()
