from constructs import Construct
from aws_cdk import App, Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_eks as eks
from aws_cdk import lambda_layer_kubectl


class TestEksClusterStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "Vpc",
            max_azs=3,
            nat_gateways=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="EksPublicSubnet", subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="EksPrivateSubnet", subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT)
            ]
        )

        # Create an EKS cluster
        cluster = eks.Cluster(self, "Cluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_24,
            kubectl_layer=lambda_layer_kubectl.KubectlLayer(self, "KubectlLayer"),
            default_capacity=0
        )

        # Add a managed node group with on-demand instances
        on_demand_node_group_props = {
            'instance_types': [ec2.InstanceType('t3.small')],
            'min_size': 1,
            'max_size': 1,
            'desired_size': 1,
            'labels': {"workload": "on-demand"}
        }
        cluster.add_nodegroup_capacity("OnDemandNodeGroup", **on_demand_node_group_props)

        # Add a managed node group with spot instances
        spot_node_group_props = {
            'instance_types': [ec2.InstanceType('t3.small')],
            'min_size': 2,
            'max_size': 2,
            'desired_size': 2,
            'labels': {"workload": "spot"},
            'capacity_type': eks.CapacityType.SPOT
        }
        cluster.add_nodegroup_capacity("SpotNodeGroup", **spot_node_group_props)

# Initialize the CDK app
app = App()
# Create the EKS cluster stack
TestEksClusterStack(app, "TestEksClusterStack")
# Generate CloudFormation templates and assets
app.synth()