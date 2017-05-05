# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def handler(event, context):
    logger.debug('got event: {}'.format(event))
    logger.debug('from SNS: {}'.format(event['Records'][0]['Sns']['Message']))

    # for record in event['Records']:
    post_data = {
        'channel': os.environ['channel'],
        'username': os.environ['username'],
        'icon_emoji': os.environ['icon_emoji'],
        'text': event['Records'][0]['Sns']['Subject']
    }

    return {'status': 'success'}
