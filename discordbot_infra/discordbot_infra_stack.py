from aws_cdk import core as cdk
from aws_cdk import aws_ecs as ecs


class DiscordbotInfraStack(cdk.Stack):

  def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # The code that defines your stack goes here
    # Create an ECS cluster
    cluster = ecs.Cluster(self, "Cluster")
