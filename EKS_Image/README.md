# AWS EKS

eks tutorial - https://www.youtube.com/watch?v=1lZdI8BInWc&list=PLuVrvwRQWy6QQDBe11vKD-haZZr7MLvPB&index=1&pp=iAQB
               https://k21academy.com/docker-kubernetes/amazon-eks-kubernetes-on-aws/

![alt text](EKS_Image/eks_architecutre.png)

![alt text](EKS_Image/eks_overview.png)

![alt text](EKS_Image/eks_document.png)

1. create eks clsuter

2. IAM role(eksClusterRole) - use case - EKS - eks cluster 

3. create EC2 instance

4. create access key

5. ec2 instance connect
      aws --version
      eksctl
      sudo eksctl
      sudo kubectl

      aws configure
         create access key from iam user secret
         AWS Access Key ID [****************O2CP]: 
         AWS Secret Access Key [****************wPOS]: 
         Default region name [us-east-1]: ap-south-1
         Default output format [json]: 


      check status of cluster
      aws eks --region ap-south-1 describe-cluster --name k21eks01 --query cluster.status
      pwd
      ls -a
      cd .aws
      ls
      ls -al
      cat credentails
      cat config
      cd ..
      ls
      cd
      ls
      ls -a
      aws eks --region ap-south-1 update-kubeconfig --name k21eks01
      cd .kube/
      ls
      cat config
      ls
      cd ..
      ls
      ls -a
      kubectl get svc


      install kubectl - https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

      inside [ec2-user@ip ~] curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.2/2024-11-15/bin/linux/amd64/kubectl

      ls -a
      ls -a
      ls -al

      chmod +x ./kubectl
      mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
      ls
      cd bin
      ls -la
      echo $PATH
      kubectl version --short --client
      kubectl version --client

      cd
      ls -a
      ls -a

      <!-- # for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
      ARCH=amd64
      PLATFORM=$(uname -s)_$ARCH

      curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

      # (Optional) Verify checksum
      curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

      tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz -->


      curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
      ls
      cd /tmp/
      ls -ltr
      cd
      sudo mv /tmp/eksctl /usr/local/bin
      echo $PATH
      cd /usr/local/bin/
      ls -al
      cd
      eksctl
      eksctl version
      kubectl get nodes
      kubectl get svc

      
6. Create EKS Cluster Worker Nodes      

go inside cluster -> compute -> node group -> create -> 
   create role (EKSNodeInstanceRole) - use case - ec2 - > amazoneksworkernodepolicy, amazoneks_cni_policy,amazonec2containerregistryreadonly


   then select role in node group
   node group scalig configuraton - 2,2,2

now create node group


now run inside -> [ec2@ip ~] kubectl get nodes --watch
now run inside -> [ec2@ip ~] kubectl get nodes


7. Delete EKS Cluster from Console

cluster -> node group -> delete 

      
delete all EKS roles      






# How to Create EKS Using CLI

create ec2 instance -
      ec2 instance connect - cmd then paste below command inside [ec2@ip ~]

1.    eksctl create cluster \
      --name eks-test-cluster \
      --version 1.24 \
      --region sp-south-1 \
      --nodegroup-name linux-nodes \
      --node-type t2.micro \
      --managed

2.    aws eks --region ap-south-1 describe-cluster --name eks-test-cluster --query cluster.status

3.    mv $HOME/.kube/config/ $HOME/.kube/config.old

cd 
ls
cd .kube/
ls
ls -al
vi config
cd 

inside [ec2-user@ip ~]kubectl get svc

4.    eksctl delete cluster \
      --name eks-test-cluster \
      --region ap-south-1


inside aws cloudformation -> stack details -> check eks cluster building
stop ec2 instance


# AWS EKS Architecture: Clusters, Nodes, and Networks

![alt text](EKS_Image/eks_architecture1.png)
   
![alt text](EKS_Image/vpc_netwrok.png)

![alt text](EKS_Image/load_balancer.png)

![alt text](EKS_Image/aws_file_storage.png)

![alt text](EKS_Image/iam_users.png)

![alt text](EKS_Image/aws_services.png)

VPC - vpc is nothing but a netowrk of continous blocks of ip address of network. example 1-10000 ip address netwrok that netwrok broken down into small network which is called vpc subnet, bigger netwrok breakdown and form subnets - virtual machine like ec2 , linx machine runs worker nodes inside this subnets and get ip address from subnets, ec2 machine got created inside vpc inside subnet and got ip address from subnet and this machine got connected with internet gateway 





Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service that allows users to run Kubernetes on AWS and on-premises: 

Features
EKS automates Kubernetes cluster infrastructure management, including scheduling containers, managing application availability, and scaling resources. 

Integration
EKS integrates with AWS networking, security, and storage services. 

Support for Windows
EKS supports adding Windows nodes as worker nodes and scheduling Windows containers. 

Hybrid deployments
EKS allows users to run nodes on AWS-hosted infrastructure, AWS Outposts, or their own on-premises environments. 

Amazon EKS Anywhere
EKS Anywhere is a Kubernetes management software that runs on infrastructure managed by the user. It's designed for isolated or air-gapped environments.

EKS makes it easier to run Kubernetes without needing to be an expert in managing Kubernetes clusters. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.





------------------------------------------------------

# What is Amazon EKS?


Amazon Elastic Kubernetes Service (Amazon EKS) is a
managed Kubernetes service that makes it easy for you to
run Kubernetes on AWS and on-premises


Kubernetes is an open-source system for automating
deployment, scaling, and management of containerized
applications.

# How to create Kubernetes Cluster & Node Groups in AWS using Managed EKS

1. AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2. Install Kubectl - https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
3. Create access key and secret key for cluster creation user - inside user(adminsitrator policy) details page -> secret credentials -> access key -> aws cli

aws configure

4. Create VPC & 2 public subnets - https://ap-south-1.console.aws.amazon.com/vpcconsole/home?region=ap-south-1#CreateVpc:createMode=vpcWithResources - VPC and more 

5. Create a Key pair - EC2 key pair create
6. Create IAM Role for cluster & attach the permission Policy - role -> use case -> eks cluster -> 
7. Create another IAM Role for Worker node & attach the permission Policy -> role -> use case -> ec2 -> AmazonEKSWorkerNodePolicy, AmazonEc2ContainerRegistryReadOnly, AmazonEKS_CNI_Policy
8. Create Security group -> vpc from point 4 -> inboud -> All traffic 
9. Create the EKS cluster - https://ap-south-1.console.aws.amazon.com/eks/home?region=ap-south-1#/cluster-create -> attach role from point 6 -> select security group -> public

aws eks update-kubeconfig --name cluster_name --region ap-south-1

10. Create the node group and attach to the cluster - IAM from point 7 -> security group select from eks and you created -> key value pair -> enable configure setting -> create -> while creationg if get error (go to inside subnet auto assign ip setting -> enabled) 
11. Connect to AWS EKS cluster using the kubectl



# Kubernetes: How to deploy a Simple Game App into Amazon EKS in 10 minutes

https://www.youtube.com/watch?v=wyad99QMKtc