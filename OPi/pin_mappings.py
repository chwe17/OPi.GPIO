# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

import functools
from OPi.constants import BOARD, BCM, SUNXI


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
		#frist row
        3: 12,
        5: 11,
        7: 203,
        11: 15,
        13: 16,
        15: 14,
		#second row
        8: 199,
        10: 198,
        12: 363,
        16: 13,
    },

    # BCM pin to actual GPIO pin
    BCM: {
		#first row
        2: 12,
        3: 11,
		4: 203,
        17: 15,
        27: 16,
        22: 14,
		#second row
        14: 199,
        15: 198,
        18: 363,
		23: 13,
    },

    SUNXI: _sunXi()
}


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
