import slack
from datetime import datetime
import ssl as ssl_lib
import certifi
import logging
import time
import json

# SLACK_BOT_TOCKEN = 'xoxp-104585340695-232007719184-776157101776-20a2e37ab75cf498ce8dc4b58ec22f31'
SLACK_BOT_TOKEN = 'xoxb-104585340695-1331671864672-UG9n2l0MrGdkddcIwF9YQqaP'


class ReactionType:
    ONLY_MENTIONS = 0
    ONLY_FROM_USER = 1
    ALL = 2
    NONE = 3


class TriggerType:
    MESSAGE = 0
    REACTION = 1


class User:
    def __init__(self, name, id, emoji, aliases=None, reaction_type=ReactionType.ONLY_MENTIONS):
        self.name = name
        self.id = id
        self.emoji = emoji
        self.aliases = aliases if aliases is not None else []
        self.reaction_type = reaction_type


class MessageTrigger:
    def __init__(self, triggers, response, trigger_type=TriggerType.MESSAGE):
        self.triggers = triggers
        self.response = response
        self.trigger_type = trigger_type


users = [
    User('kenza', 'U4W8VP1MK', 'kenza-dab', ['k dawg', 'k-dawg', 'boudad']),
    User('andrew_cox', None, 'andrew-cox-dab', ['andrew', 'cox']),
    User('robert', 'U4N22D1JL', 'bobby-earl-dab', ['bobby earl', 'bobby-earl', 'pritchett']),
    User('brian', 'U4NMUFLF5', 'brian-dab', ['mccarthy']),
    User('emily', 'U4PDMLWAW', 'emily-dab', ['e dawg', 'e-dawg', 'spreen']),
    User('ted', None, 'ted-dab', ['wahl', 'theodore']),
    User('nick', 'U6U07M55E', 'nick-dab', ['lafarge']),
    User('ash', None, 'ash-dab', ['das']),
    User('matt', None, 'matt-dab', ['bollinger']),

    User('juan', 'U6RAXQNSF', 'jor', ['jor', 'ojeda romero'], reaction_type=ReactionType.ALL),
    User('juandab', 'U6RAXQNSF', 'juan-dab', ['juan', 'jor', 'ojeda romero']),
    User('rj', 'U6R3PLNJC', 'power', ['rolfe', 'power']),
]

message_triggers = [
    MessageTrigger(['research group'], ':kenza-dab::andrew-cox-dab::bobby-earl-dab::brian-dab::juan-dab::emily-dab:'
                                       ':ted-dab::nick-dab::ash-dab::matt-dab:'),
    MessageTrigger(['dab'], 'squiddab', trigger_type=TriggerType.REACTION)
]

users_dict = {u.name: u for u in users}

try:
    with open('response_log.json') as json_file:
        responses = json.load(json_file)
except:
    responses = dict()

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
client = slack.WebClient(SLACK_BOT_TOKEN, ssl=ssl_context)
channels = client.conversations_list().data['channels']


def text_in_msg(msg, text):
    if 'text' not in msg:
        return False

    return text.lower() in msg['text'].lower()


def name_or_mention_in_msg(msg, user):
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


def msg_from_user(msg, user):
    if 'user' not in msg:
        return False

    if not user.id:
        return False

    return msg['user'] == user.id


def add_user_reaction(channel, msg, user):
    return add_reaction(channel, msg, user.emoji)


def add_reaction(channel, msg, emoji):
    if 'reactions' in msg:
        existing_reactions = [r for r in msg['reactions'] if r['name'] == user.emoji]
        if existing_reactions:
            return

    client.reactions_add(
        name=emoji,
        channel=channel['id'],
        timestamp=msg['ts']
    )


def send_message(channel, text, trigger_ts):
    # Only respond once
    if trigger_ts in responses.keys():
        return

    response = client.chat_postMessage(
        channel=channel['id'],
        text=text
    )
    responses[trigger_ts] = response.data['message']['ts']
    pass


def clear_channel(channel, messages):
    for msg in messages:
        print(msg)
        client.chat_delete(
            channel=channel['id'],
            ts=msg['ts']
        )
        time.sleep(1)


try:
    get_channel = lambda name: next(i for i in channels if i['name'] == name)
    general = get_channel('general')
    random = get_channel('random')
    outings = get_channel('outings')
    climbing = get_channel('climbing')
    research = get_channel('research')
    test = get_channel('bot-testing')
    # channels_list = [general, random, outings, climbing, test]
    channels_list = [test]

    for c in channels_list:
        history = client.channels_history(channel=c['id']).data

        bot_history = [msg for msg in history['messages'] if 'bot_id' in msg]
        # clear_channel(c, bot_history)
        for msg in [msg for msg in history['messages'] if 'bot_id' not in msg and msg['user'] != 'USLACKBOT']:
            msg_date = datetime.fromtimestamp(float(msg['ts']))

            if msg_date <= datetime(2020, 8, 15):
                continue

            for user in users:
                if user.reaction_type == ReactionType.ALL or user.reaction_type == ReactionType.ONLY_MENTIONS:
                    if name_or_mention_in_msg(msg, user):
                        add_user_reaction(c, msg, user)

                if user.reaction_type == ReactionType.ALL or user.reaction_type == ReactionType.ONLY_FROM_USER:
                    if msg_from_user(msg, user):
                        add_user_reaction(c, msg, user)

            for msg_trigger in message_triggers:
                for trigger in msg_trigger.triggers:
                    if text_in_msg(msg, trigger):
                        if msg_trigger.trigger_type == TriggerType.MESSAGE:
                            send_message(c, msg_trigger.response, trigger_ts=msg['ts'])
                        elif msg_trigger.trigger_type == TriggerType.REACTION:
                            add_reaction(c, msg, msg_trigger.response)

except Exception as e:
    logging.error(e)
    pass

with open('response_log.json', 'w') as outfile:
    json.dump(responses, outfile)
