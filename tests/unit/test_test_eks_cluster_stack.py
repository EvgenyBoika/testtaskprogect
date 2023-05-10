import aws_cdk as core
import aws_cdk.assertions as assertions

from test_eks_cluster.test_eks_cluster_stack import TestEksClusterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_eks_cluster/test_eks_cluster_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestEksClusterStack(app, "test-eks-cluster")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
