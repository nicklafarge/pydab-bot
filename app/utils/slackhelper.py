import slack
from slack.errors import SlackApiError
from config import get_env
import ssl as ssl_lib
import certifi


class SlackHelper:
    def __init__(self):
        self.slack_token = get_env('SLACK_TOKEN')
        ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
        self.client = slack.WebClient(self.slack_token, ssl=ssl_context)

        all_channels = self.client.conversations_list(types='public_channel, private_channel').data['channels']
