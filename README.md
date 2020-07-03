# groupme_chatbot

Chatbot for use in the PW3 group chat. It will be twitch style where user will enter a string in the chat like '!Fuck'. The chatbot will return 'Fuck Frost' and keep track of how many times we've said it. Some other features will include:
- Get xur data
    - action --> !xur
- Get reset data
    - action --> !reset
- Mention @Frost and tell him 'fuck you' or 'fuck off
    - Keep track of number of times we tell Frost fuck you
    - action --> !fuck
- Greet new members
    - action --> !welcome <new_member>
	- !welcome frost

__TODO:__

- Create BOT using the form https://dev.groupme.com/bots/new
- Make bungie app to get
	- clan info
	- player stats
		- pvp
			- kd
			- w/l
		- pve
			- raid stuff


## Run server
I use heroku to host the server. Heroku uses 'git' style stuff to run. To deploy server do the following:
```sh
git push heroku master
```

## Requirements:
- python3.6
- requests
- heroku
- bungie api

## Server:
- Callback URL --> https://dmonton-testbot.herokuapp.com/

## Enviornmental Variables heroku
- heroku config:set GROUPME_BOT_ID=a390e53b51a05e53b9551dedeb

## Example usage to post message
### bash/curl
```sh
curl -d '{"text" : "Your message here", "bot_id" : "a390e53b51a05e53b9551dedeb"}' https://api.groupme.com/v3/bots/post
```

### python3

```py
import requests

url = 'https://api.groupme.com/v3/bots/post'
text = 'Test bot stuff'
bot_id = 'a390e53b51a05e53b9551dedeb'
payload = {'text': text, 'bot_id': bot_id}

requests.post(url, payload)
```
