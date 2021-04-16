"""
Configuration file loader
"""

import os.path

import yaml


# Get configuration YAML FILE location
__CURRENT_DIR = os.path.dirname(__file__)
__RESOURCE_PATH = os.path.join(__CURRENT_DIR, '..', 'resources')
__CONFIG_FILE = os.path.join(__RESOURCE_PATH, 'config.yaml')

with open(__CONFIG_FILE, 'r') as yml_config_file:
    data = yaml.load(yml_config_file, Loader=yaml.FullLoader)
    if isinstance(data, dict) is False:
        raise TypeError("Configuration file should be dict type")

# Twit API 사용 시 필요한 API KEY
twit_api_key = data.get('twit').get('api_key', '')
twit_api_secret_key = data.get('twit').get('api_secret_key', '')
twit_access_token = data.get('twit').get('access_token', '')
twit_access_token_secret = data.get('twit').get('access_token_secret', '')

# Google PUB/SUB 사용시 필요한 설정값
__google_credential_file = data.get('google').get('credential-file-name', '')
google_credential_file = os.path.join(__RESOURCE_PATH, __google_credential_file)
google_pubsub_topic = data.get('google').get('pubsub_topic', '')
