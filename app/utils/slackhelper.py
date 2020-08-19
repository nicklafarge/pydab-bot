import slack
from slack.errors import SlackApiError
from config import get_env
import ssl as ssl_lib
import certifi
import time


class SlackHelper:
    def __init__(self):
        self.slack_token = get_env('API_TOKEN')
        ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
        self.client = slack.WebClient(self.slack_token, ssl=ssl_context)

        # all_channels = self.client.conversations_list(types='public_channel, private_channel').data['channels']

    def text_in_msg(self, msg, text):
        if 'text' not in msg:
            return False
        print(f"Parsing message: {msg['text'].lower()}")
        return text.lower() in msg['text'].lower()

    def name_or_mention_in_msg(self, msg, user):
        # not just an emoji or picture
        if 'text' not in msg:
            return False

        msg_text = msg['text'].lower()

        # Does the text contain the user's name or alias?
        if user.name in msg_text or any([a in msg_text for a in user.aliases]):
            return True

        # Does the text contain the user's id?
        if user.id and user.id.lower() in msg_text:
            return True

        # If we get here, then its not mentioned...
        return False

    def msg_from_user(self, msg, user):
        if 'user' not in msg:
            return False

        if not user.id:
            return False

        return msg['user'] == user.id

    def add_user_reaction(self, channel, timestamp, user):
        return self.add_reaction(channel, timestamp, user.emoji)

    def add_reaction(self, channel, timestamp, emoji):
        try:
            self.client.reactions_add(
                name=emoji,
                channel=channel,
                timestamp=timestamp
            )
        except SlackApiError as sae:
            print("SLACK API ERROR")
            print(sae)
            pass

    def send_message(self, channel, text):
        return self.client.chat_postMessage(
            channel=channel,
            text=text
        )
