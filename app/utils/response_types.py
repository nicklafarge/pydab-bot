class ReactionType:
    ONLY_MENTIONS = 0
    ONLY_FROM_USER = 1
    ALL = 2
    NONE = 3


class TriggerType:
    MESSAGE = 0
    REACTION = 1


class User:
    def __init__(self, name, user_id, emoji, aliases=None, reaction_type=ReactionType.ONLY_MENTIONS):
        self.name = name
        self.id = user_id
        self.emoji = emoji
        self.aliases = aliases if aliases is not None else []
        self.reaction_type = reaction_type


class MessageTrigger:
    def __init__(self, triggers, response, trigger_type=TriggerType.MESSAGE):
        self.triggers = triggers
        self.response = response
        self.trigger_type = trigger_type
