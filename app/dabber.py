from app.utils.response_types import User, MessageTrigger, ReactionType, TriggerType
from datetime import datetime
from app.utils.slackhelper import SlackHelper

users = [
    User('kenza', 'U4W8VP1MK', 'kenza-dab',
         ['k dawg', 'k-dawg', 'boudad', 'kempa', 'kenga', 'kemba', 'kenda', 'kenba', 'kemda']),
    User('andrew_cox', None, 'andrew-cox-dab', ['andrew the elder', 'cox']),
    User('robert', None, 'bobby-earl-dab', ['bobby earl', 'bobby-earl', 'pritchett', 'flannel']),
    User('brian', 'U4NMUFLF5', 'brian-dab', ['mccarthy']),
    User('emily', 'U4PDMLWAW', 'emily-dab', ['e dawg', 'e-dawg', 'spreen']),
    User(' ted', None, 'ted-dab', ['wahl', 'theodore']),
    User('nick', 'U6U07M55E', 'nick-dab', ['lafarge']),
    User('ash', None, 'ash-dab', ['das'], exclusions=['trash']),
    User('matt', None, 'matt-dab', ['bollinger']),
    User('juan', 'U6RAXQNSF', 'jor', ['jor', 'ojeda romero'], reaction_type=ReactionType.ALL,
         exclusions=['Juan Pablo', 'Juan-Pablo']),
    User('juandab', 'U6RAXQNSF', 'juan-dab', ['juan', 'jor', 'ojeda romero'], exclusions=['Juan Pablo', 'Juan-Pablo']),
    User('rj', 'U6R3PLNJC', 'power', ['rolfe', 'power']),
    User('beom', 'UHLTCF8J3', 'beom-dab', ['park'])
]

message_triggers = [
    MessageTrigger(['research group'],
                   ':kenza-dab::andrew-cox-dab::bobby-earl-dab::brian-dab::beom-dab::juan-dab::emily-dab:'
                   ':ted-dab::nick-dab::ash-dab::matt-dab:',
                   trigger_type=TriggerType.MESSAGE),
    MessageTrigger(['dab', '@u019rkrreks'], 'squiddab', trigger_type=TriggerType.REACTION),
    MessageTrigger(['graduation', 'defense', 'defend'], 'magi-kenza-dab', trigger_type=TriggerType.REACTION),
    MessageTrigger(['graduation', 'defense', 'defend'], 'magi-brian-dab', trigger_type=TriggerType.REACTION),
    MessageTrigger(['joey'], 'joey', trigger_type=TriggerType.REACTION),
    MessageTrigger(['charlie', 'wagon'], 'chuckwagon', trigger_type=TriggerType.REACTION),
    MessageTrigger(['roxy', 'roxstar'], 'roxstar', trigger_type=TriggerType.REACTION),
    MessageTrigger(['sherpa'], 'sherpa', trigger_type=TriggerType.REACTION),
    MessageTrigger(['bean', 'coffee', 'latte', '3bs'], 'thosbeans', trigger_type=TriggerType.REACTION),
    MessageTrigger(['lucy'], 'lucy', trigger_type=TriggerType.REACTION),
    MessageTrigger(['mischief'], 'lucyintheskywithdiamonds', trigger_type=TriggerType.REACTION),
    MessageTrigger([':f:'], 'f', trigger_type=TriggerType.REACTION),
]

users_dict = {u.name: u for u in users}
sh = SlackHelper()


def dab_message_response(request):
    channel = request['channel']

    kwargs = dict()
    if 'thread_ts' in request:
        kwargs['thread_ts'] = request['thread_ts']

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
                    sh.send_message(channel, msg_trigger.response, **kwargs)
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
