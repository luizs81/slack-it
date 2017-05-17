# slack-it

AWS Lambda function to push SNS notifications to Slack

## Quick start

1. Clone this repository
2. Create a virtual environment and install the dependencies
3. Copy the `kappa.yml.sample` to `kappa.yml` and fill the correct values
4. `$ cd _src && pip install -r requirements.txt -t /full/path/to/lib/folder`

## References
* [How to set up a Slack channel to be an AWS SNS subscriber](https://medium.com/cohealo-engineering/how-set-up-a-slack-channel-to-be-an-aws-sns-subscriber-63b4d57ad3ea)
* [Slack Incoming Webhooks](https://api.slack.com/incoming-webhooks)
* [Amazon SNS Notification Format](http://docs.aws.amazon.com/sns/latest/dg/json-formats.html#http-notification-json)
