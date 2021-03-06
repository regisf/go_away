# -*- coding: utf-8 -*-

"""
    main
"""

import time
import utils
import config


while True:
    try:
        time.sleep(config.REFRESH)
        print(50 * "\n")
        url = config.URL
        samples = utils.parserHtml(utils.getInfo(url))
        for tram in samples:
            print(utils.clean(tram.text))
        print(1 * "\n")
    except ConnectionError:
        print(50 * "\n")
        print("Tram doesn´t exist anymore!")
        print(1 * "\n")
