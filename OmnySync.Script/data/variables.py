# -*- coding: utf-8 -*-

"""
Файл с данными для скрипта
"""
from notion.collection import Collection
from notion.client import NotionClient

INSTALL_PATH = '/opt/sync_notion'

_AUTH_TOKEN = 'bd4d288d2278c964c49c72b0cac90f78aef2fbedb00f030665b7e2f4746279c00d2f5f385bb37e67ad36e5445f749c66a227e082eb6743eaecf90a92c5eeecee288b2d4bd442ebbb35ee178e79f1'

_PAGE_URL = 'https://www.notion.so/vmylife/Test-93c78278d51949f1b0dd8c80660f6abe'

_TASKS_URL = 'https://www.notion.so/vmylife/654216a578e749cbb42d659a18c2a11e?v=6c91a28ee1d746d4b20a4b9481781c74'

_PERSONS_URL = 'https://www.notion.so/vmylife/156e29110e9143139e34d20b756a078f?v=bb3d1d8058414b09836ebb5b417b8109'

_client = NotionClient(token_v2=_AUTH_TOKEN)

notionData = {
    'client': _client,
    'page': _client.get_block(_PAGE_URL),
    'tasks_database': _client.get_collection_view(_TASKS_URL),
}

users = {}

_users_database = _client.get_collection_view(_PERSONS_URL)

for row in _users_database.collection.get_rows():
    users[row.OmniPlanName] = row.PersonLink
