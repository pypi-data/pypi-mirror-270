# -*- coding: utf-8 -*-

from typing import Dict

from ....framework.plugin.manager import BasicPluginManager


def constructor(config: Dict):
    return BasicPluginManager(config)


__all__=[
    'constructor'
]
