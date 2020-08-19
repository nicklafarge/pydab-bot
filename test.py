import requests

url = 'http://127.0.0.1:5000/dabbot/'

challenge_test = {
    "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
    "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
    "type": "url_verification"
}

dab_reaction_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF', 'api_app_id': 'ANU4DL7EC',
                     'event': {'client_msg_id': '9f024765-091c-4c69-9221-9f92437a6364', 'type': 'message',
                               'text': 'cmon dab me fam', 'user': 'U6U07M55E', 'ts': '1597844798.032400',
                               'team': 'T32H7A0LF', 'blocks': [{'type': 'rich_text', 'block_id': 'gHn', 'elements': [
                             {'type': 'rich_text_section',
                              'elements': [{'type': 'text', 'text': 'cmon dab me fam'}]}]}], 'channel': 'C019MGFAXS4',
                               'event_ts': '1597844798.032400', 'channel_type': 'channel'}, 'type': 'event_callback',
                     'event_id': 'Ev019ABH4XCL', 'event_time': 1597844798, 'authed_users': ['U019RKRREKS']}

many_reaction_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF', 'api_app_id': 'ANU4DL7EC',
                      'event': {'client_msg_id': '19db0039-2264-417f-b2f0-c634d181941e', 'type': 'message',
                                'text': 'emily kenza dab', 'user': 'U6U07M55E', 'ts': '1597843940.030700',
                                'team': 'T32H7A0LF', 'blocks': [{'type': 'rich_text', 'block_id': 'nJ88k', 'elements': [
                              {'type': 'rich_text_section',
                               'elements': [{'type': 'text', 'text': 'emily kenza dab'}]}]}], 'channel': 'C019MGFAXS4',
                                'event_ts': '1597843940.030700', 'channel_type': 'channel'}, 'type': 'event_callback',
                      'event_id': 'Ev019U081X96', 'event_time': 1597843940, 'authed_users': ['U019RKRREKS']}

reaction_added_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF', 'api_app_id': 'ANU4DL7EC',
                       'event': {'type': 'reaction_added', 'user': 'U6U07M55E',
                                 'item': {'type': 'message', 'channel': 'C019MGFAXS4', 'ts': '1597844226.031200'},
                                 'reaction': 'brian-dab', 'item_user': 'U6U07M55E', 'event_ts': '1597844233.031300'},
                       'type': 'event_callback', 'event_id': 'Ev01945ANCM8', 'event_time': 1597844233,
                       'authed_users': ['U019RKRREKS']}

name_reaction_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF', 'api_app_id': 'ANU4DL7EC',
                      'event': {'client_msg_id': 'eb9ca07f-321e-4967-bc8d-1539807dfcc2', 'type': 'message',
                                'text': 'shit no dag for k dawg', 'user': 'U6U07M55E', 'ts': '1597845654.035000',
                                'team': 'T32H7A0LF', 'blocks': [{'type': 'rich_text', 'block_id': 'mFG', 'elements': [
                              {'type': 'rich_text_section',
                               'elements': [{'type': 'text', 'text': 'shit no dag for k dawg'}]}]}],
                                'channel': 'C019MGFAXS4', 'event_ts': '1597845654.035000', 'channel_type': 'channel'},
                      'type': 'event_callback', 'event_id': 'Ev0192RQFLKF', 'event_time': 1597845654,
                      'authed_users': ['U019RKRREKS']}

# payload = dab_reaction_test
# payload = reaction_added_test
payload = name_reaction_test

response = requests.post(url, json=payload)
