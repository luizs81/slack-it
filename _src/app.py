# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
import os

import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

danger_msgs = [
    ' but with errors',
    ' to RED',
    'During an aborted deployment',
    'Failed to deploy application',
    'Failed to deploy configuration',
    'has a dependent object',
    'is not authorized to perform',
    'Pending to Degraded',
    'Stack deletion failed',
    'Unsuccessful command execution',
    'You do not have permission',
    'Your quota allows for 0 more running instance',
]

warning_msgs = [
    ' aborted operation.',
    ' to YELLOW',
    'Adding instance ',
    'Degraded to Info',
    'Deleting SNS topic',
    'is currently running under desired capacity',
    'Ok to Info',
    'Ok to Warning',
    'Pending Initialization',
    'Removed instance ',
    'Rollback of environment',
]


def handler(event, context):
    logger.debug('got event: {}'.format(event))
    logger.debug('from SNS: {}'.format(event['Records'][0]['Sns']['Message']))

    subject = event['Records'][0]['Sns']['Subject']
    message = event['Records'][0]['Sns']['Message']
    severity = 'good'

    for m in danger_msgs:
        if m in message:
            severity = 'danger'
            break

    if severity != 'danger':
        for m in warning_msgs:
            if m in message:
                severity = 'warning'
                break

    url = os.environ['webhook_url']
    # for record in event['Records']:
    data = {
        'channel': os.environ['channel'],
        'username': os.environ['username'],
        'icon_emoji': os.environ['icon_emoji'],
        'attachments': [
            {
                'fallback': subject,
                'color': severity,
                'pretext': subject,
                'text': message,
            },
        ],
    }

    r = requests.post(url, json=data)
    logger.debug('Slack response: {}'.format(r.json()))

    return {'status': 'success'}
