#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 443
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "541aa899-3c02-4e7f-bffe-45cfe953f276")
    #CONNECTION_NAME = os.environ.get("ConnectionName", "BotTeamsAuthADv1")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "302d9294f0784ecd801181c868f80c3e")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://centralindia.api.cognitive.microsoft.com/")
