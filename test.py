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

edited_message_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF', 'api_app_id': 'ANU4DL7EC',
                       'event': {'type': 'message', 'subtype': 'message_changed', 'hidden': True,
                                 'message': {'client_msg_id': '8721e910-0e42-41ac-9da1-cd75b3fbefe1', 'type': 'message',
                                             'text': 'research group', 'user': 'U6U07M55E', 'team': 'T32H7A0LF',
                                             'edited': {'user': 'U6U07M55E', 'ts': '1597845926.000000'}, 'blocks': [
                                         {'type': 'rich_text', 'block_id': 'UqSo', 'elements': [
                                             {'type': 'rich_text_section',
                                              'elements': [{'type': 'text', 'text': 'research group'}]}]}],
                                             'ts': '1597845919.036900', 'source_team': 'T32H7A0LF',
                                             'user_team': 'T32H7A0LF'}, 'channel': 'C019MGFAXS4',
                                 'previous_message': {'client_msg_id': '8721e910-0e42-41ac-9da1-cd75b3fbefe1',
                                                      'type': 'message', 'text': 'research grou', 'user': 'U6U07M55E',
                                                      'ts': '1597845919.036900', 'team': 'T32H7A0LF', 'blocks': [
                                         {'type': 'rich_text', 'block_id': 'sHUJ', 'elements': [
                                             {'type': 'rich_text_section',
                                              'elements': [{'type': 'text', 'text': 'research group'}]}]}]},
                                 'event_ts': '1597845926.037100', 'ts': '1597845926.037100', 'channel_type': 'channel'},
                       'type': 'event_callback', 'event_id': 'Ev019GS1SQSD', 'event_time': 1597845926,
                       'authed_users': ['U019RKRREKS']}

research_group_in_comment_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF',
                                  'api_app_id': 'ANU4DL7EC',
                                  'event': {'client_msg_id': '4233c6e4-6494-49bb-a9b6-3d63e1ff97fe', 'type': 'message',
                                            'text': 'research group', 'user': 'U6U07M55E', 'ts': '1598290457.000100',
                                            'team': 'T32H7A0LF', 'blocks': [{'type': 'rich_text', 'block_id': 'TPS',
                                                                             'elements': [{'type': 'rich_text_section',
                                                                                           'elements': [{'type': 'text',
                                                                                                         'text': 'research group'}]}]}],
                                            'thread_ts': '1597925377.000300', 'parent_user_id': 'U6U07M55E',
                                            'channel': 'C019MGFAXS4', 'event_ts': '1598290457.000100',
                                            'channel_type': 'channel'}, 'type': 'event_callback',
                                  'event_id': 'Ev0196RX6R7Y', 'event_time': 1598290457, 'authed_users': ['U019RKRREKS']}

jp_test = {'token': 'gm6yRCbGgSePVPtZBErknAQh', 'team_id': 'T32H7A0LF', 'api_app_id': 'ANU4DL7EC',
           'event': {'client_msg_id': '01ca412f-e30f-4865-877c-8bd4114c0b8d', 'type': 'message',
                     'text': 'juan-pablo test', 'user': 'U6U07M55E', 'ts': '1598395906.006000', 'team': 'T32H7A0LF',
                     'blocks': [{'type': 'rich_text', 'block_id': 'x7j', 'elements': [
                         {'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'juan-pablo test'}]}]}],
                     'channel': 'C019MGFAXS4', 'event_ts': '1598395906.006000', 'channel_type': 'channel'},
           'type': 'event_callback', 'event_id': 'Ev019ABK9FKQ', 'event_time': 1598395906,
           'authed_users': ['U019RKRREKS']}

# payload = dab_reaction_test
# payload = reaction_added_test
# payload = name_reaction_test
# payload = research_group_in_comment_test
payload = jp_test

response = requests.post(url, json=payload)
