# from aws_cdk import core as cdk
from constructs import Construct
from aws_cdk import App, Stack                    # core constructs
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_secretsmanager as secretsmanager
# from aws_cdk import aws_

class DiscordbotInfraStack(Construct):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Importing existing resources to CDK
    DiscordAuthTokenSecretArn = "arn:aws:secretsmanager:ap-southeast-2:811385878444:secret:/DiscordBot/Discord/AuthToken"
    DiscordAuthTokenSecret = secretsmanager.Secret.from_secret_partial_arn(self, "DiscordBotTokenSecret", DiscordAuthTokenSecretArn)

    # Lambda function to respond to Discord's API calls
    # DiscordBotResponderLambda = 

    # ECS cluster to run server traffic
    cluster = ecs.Cluster(self, "Cluster")
