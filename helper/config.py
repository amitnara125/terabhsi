#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID", cast="7774029")
    API_HASH = config("API_HASH",="531dbf42d387514dc43da07db9f2dc8f")
    BOT_TOKEN = config("BOT_TOKEN",="5987535163:AAHGC-Aii_e3hXiNnkuK2JVOXTyYAj0wC_c")
    OWNER = config("OWNER_ID", default=1322549723, cast=1654867043)
    LOG = config("LOG_CHANNEL", cast="VCAMCHANEL")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
