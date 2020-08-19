from app.utils.response_types import User, MessageTrigger, ReactionType, TriggerType
from datetime import datetime
from app.utils.slackhelper import SlackHelper

users = [
    User('kenza', 'U4W8VP1MK', 'kenza-dab', ['k dawg', 'k-dawg', 'boudad', 'kempa', 'kenga']),
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
sh = SlackHelper()


def dab_message_response(request):
    channel = request['channel']

    for user in users:
        if user.reaction_type == ReactionType.ALL or user.reaction_type == ReactionType.ONLY_MENTIONS:
            if sh.name_or_mention_in_msg(request, user):
                sh.add_user_reaction(channel, request['ts'], user)

        if user.reaction_type == ReactionType.ALL or user.reaction_type == ReactionType.ONLY_FROM_USER:
            if sh.msg_from_user(request, user):
                sh.add_user_reaction(channel, request['ts'], user)

    for msg_trigger in message_triggers:
        for trigger in msg_trigger.triggers:
            if sh.text_in_msg(request, trigger):
                if msg_trigger.trigger_type == TriggerType.MESSAGE:
                    sh.send_message(channel, msg_trigger.response)
                elif msg_trigger.trigger_type == TriggerType.REACTION:
                    sh.add_reaction(channel, request['ts'], msg_trigger.response)


def dab_add_to_emoji(request):
    emoji_reaction = request['reaction']
    if 'dab' in emoji_reaction:
        sh.add_reaction(request['item']['channel'], request['item']['ts'], emoji_reaction)


def dab(request):
    if 'bot_id' in request:
        return

    print(f"Request type: {request['type']}")
    if request['type'] == 'message':
        dab_message_response(request)
    elif request['type'] == 'reaction_added':
        dab_add_to_emoji(request)
