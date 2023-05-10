
# Deploying an EKS Cluster using AWS CDK
This application deploys an Amazon EKS Cluster using the AWS Cloud Development Kit (CDK). It creates a VPC with public and private subnets, an EKS cluster, and two managed node groups with on-demand and spot instances.


Prerequisites
1. Install the AWS CLI. https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

2. Configure the AWS CLI with your AWS credentials and region where you will deploy

```
aws configure
```
3. Install Python 3.7 or later

```
sudo apt update
sudo apt install python3
```

4. Install pip3.

```
sudo apt install python3-pip
```
5. Install nodejs:

```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```
6. Install the AWS CDK.

```
npm install -g aws-cdk
```
Deployment Steps

1.Clone the repository and navigate to the project directory:

```
git clone https://github.com/EvgenyBoika/testtaskprogect.git

```
2. Go to cdkcode:

```
cd cdkcode
```
3. Create a new CDK project using Python:
```
cdk init app --language python
```

Deploy the application using the AWS CDK:

```
cdk synth
cdk deploy

```

Clean Up
To delete the resources created by this application, run:

```
cdk destroy

```

Deploying Hello Kubernetes on an Amazon EKS Cluster using Helm
This guide will walk you through deploying the Hello Kubernetes container on an Amazon EKS cluster using Helm and expose it to the public internet.

Prerequisites
A running Amazon EKS cluster.
kubectl installed and configured to work with your EKS cluster.
Helm installed and configured to work with your EKS cluster.
Deployment Steps
1. Clone the Hello Kubernetes repository:
```
git clone https://github.com/paulbouwer/hello-kubernetes.git
cd hello-kubernetes/deploy/helm

```
2. Deploy it using command:

```
helm install --create-namespace --namespace hello-kubernetes hello-world ./hello-kubernetes --set service.type=LoadBalancer

```
To access the application use this command (this is ip adress in your browser):
```
kubectl get svc -n hello-kubernetes hello-kubernetes-hello-world -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

```
Building the Flink WordCount Example
This guide will walk you through building the WordCount example from the Apache Flink project.

Prerequisites
1. Install the Java Development Kit (JDK) version 8 or later.

```
sudo apt update
sudo apt install openjdk-11-jdk

```

2. Install Maven.

```
sudo apt update
sudo apt install maven

```

Building the WordCount Example
1. Clone the Apache Flink repository:

```
git clone https://github.com/apache/flink.git
cd flink

```

2. Navigate to the Flink streaming examples directory:

```
cd flink-examples/flink-examples-streaming

```

3. Build the Flink streaming examples with Maven:

```
mvn clean install -DskipTests

```
4. Go to target directory 

```
cd target

```
5. Here is WordCount.jar


Deploying Flink on Amazon EKS HA
This guide will walk you through deploying a Flink cluster in High Availability (HA) cluster on an Amazon EKS cluster using your custom Helm chart.

Prerequisites
A running Amazon EKS cluster.
kubectl installed and configured to work with your EKS cluster.
Helm installed and configured to work with your EKS cluster.

1. Go to flinkchart directory

```
cd flinkk8s

```
2. helm install:

```
helm install flink8schart-test flink8schart
```
3. Get external ip of flink

```
kubectl get svc flink-jobmanager-rest -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

```
4. Run this EXTERNAL-IP:8081

5. Using web ui Add your WordCount.jar in flink
