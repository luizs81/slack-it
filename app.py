# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)


def handler(event, context):
    assert context
    for record in event['Records']:
        start_time = record['Sns']['Timestamp']
        LOG.info('start_time: %s', start_time)
