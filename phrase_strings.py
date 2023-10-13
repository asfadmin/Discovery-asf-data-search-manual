# https://github.com/phrase/phrase-python
# Expects an environment variable named PHRASE_DISCOVERY_ACCESS_TOKEN to be set.

from __future__ import print_function

import os
import json
import phrase_api
from phrase_api.rest import ApiException

project_id = '88ffd4d5abd6494131fabb1a271950b8'  # mkDocs

def load_configuration():
    configuration = phrase_api.Configuration()
    configuration.api_key_prefix['Authorization'] = 'token'
    configuration.host = "https://api.us.app.phrase.com/v2/"

    access_token = 'PHRASE_DISCOVERY_ACCESS_TOKEN'
    if access_token in os.environ:
        configuration.api_key['Authorization'] = os.environ[access_token]
    else:
        print(f'{access_token} does not exist')
        exit(1)

    return configuration


def load_locale(locale):

    configuration = load_configuration()

    # Enter a context with an instance of the API client
    with phrase_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = phrase_api.LocalesApi(api_client)
        id = locale
        x_phrase_app_otp = ''
        if_modified_since = ''
        if_none_match = ''
        branch = ''
        file_format = 'json'
        tags = ''
        tag = ''
        include_empty_translations = True
        exclude_empty_zero_forms = True
        include_translated_keys = True
        keep_notranslate_tags = True
        convert_emoji = True
        format_options = None
        encoding = ''
        skip_unverified_translations = False
        include_unverified_translations = True
        use_last_reviewed_version = False
        fallback_locale_id = ''
        source_locale_id = 'en'

        try:
            # Download a locale
            api_response = api_instance.locale_download(project_id, id,
                                                        x_phrase_app_otp=x_phrase_app_otp,
                                                        if_modified_since=if_modified_since,
                                                        if_none_match=if_none_match,
                                                        branch=branch, file_format=file_format,
                                                        tags=tags, tag=tag,
                                                        include_empty_translations=include_empty_translations,
                                                        exclude_empty_zero_forms=exclude_empty_zero_forms,
                                                        include_translated_keys=include_translated_keys,
                                                        keep_notranslate_tags=keep_notranslate_tags,
                                                        convert_emoji=convert_emoji,
                                                        format_options=format_options,
                                                        encoding=encoding,
                                                        skip_unverified_translations=skip_unverified_translations,
                                                        include_unverified_translations=include_unverified_translations,
                                                        use_last_reviewed_version=use_last_reviewed_version,
                                                        fallback_locale_id=fallback_locale_id,
                                                        source_locale_id=source_locale_id)
            f = open(api_response, 'r')
            data = json.load(f)
            return data
        except ApiException as e:
            print("Exception when calling LocalesApi->locale_download: %s\n" % e)

def list_locales():
    configuration = load_configuration()
    # Enter a context with an instance of the API client
    with phrase_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = phrase_api.LocalesApi(api_client)
        # sort_by = 'sort_by_example'  # str | Sort locales. Valid options are \"name_asc\", \"name_desc\", \"default_asc\", \"default_desc\".
        # branch = 'my-feature-branch'  # str | specify the branch to use

        try:
            # List locales
            # api_response = api_instance.locales_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page,
            #                                          per_page=per_page, sort_by=sort_by, branch=branch)
            api_response = api_instance.locales_list(project_id)
        except ApiException as e:
            print("Exception when calling LocalesApi->locales_list: %s\n" % e)

        return api_response

