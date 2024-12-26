# VPC - Virtual private cloud
https://www.youtube.com/watch?v=ZMJV5AIfVBE

What is VPC
What are subnets
What is AWS region and availability zones
What is CIDR Block
What are routing tables
Integrating Internet Gateways (IGW)
What is NAT
What is Security Group
Managing Security Groups
VPC Peering
AWS Client VPN
AWS Direct 
Bastion Host
Real-world examples and usecases


A private, isolated network within the aws cloud where you can launch and manage your resources securely.  

why we need VPC?
to secure isolated and control network environments.

in one region -> multiple Availability zones a1,b1,c1 to prevent failure of one Availability zone


![alt text](VPC/cidr_block.png)

![alt text](VPC/subnet.png)

while creating vpc we were providing CIDR range

CIDR - (classless inter-domain-routing) is a method for allocating IP addresses and routing internal protocol(IP) pocket.

cidr.xyz to understand cidr

10.0.0.0/16 

if ipv4 cidr block 16 - 65536
if 28 - 16

first usable ip - 10.0.0.1
last usable ip - 10.0.255.254


one region -> one VPC -> we can have 16 ip or 65536 inside VPC


Subnet - a subnet is a smaller, segment part of a larger network that isolated and organizes device within a specific IP address range.


public-subnet -front end - 10.0.1.0/24
private-subnet - database - 10.0.2.0/24

each of subnet have 256 ip in which 251 is usable

subnet build on avaliability zones 

in one avaliability zone you can build mutiple subnet or 
one avaliability zone one subnet

![alt text](VPC/subnet1.png)

![alt text](VPC/cidr.png)


![alt text](VPC/subnet2.png)


inside aws--->

vpc setting -> vpc and more 

ipv4cidr block - 10.0.0.0/16

number of avaliability zones - 2,3 - a1,b1,c1

number of private and public subnet

![alt text](VPC/vpc_connectivity.png)


![alt text](VPC/route_table.png)

each subnet inside VPC accociated with a route table,  which controls the routing for the subnet


![alt text](VPC/internet_gateway.png)

Internet gateway -> Internet gateway is a component that allows communication between instances in your VPC and internet.
 (we can see it is conencted with VPC)

Security group -> Network firewall rules that control inbound and outbound traffic for instances.

(Only allow rules)
security group work on instance level

inside VPC -> security group -> open security group -> inbound rule (from internetor browser request will come in ur application- enable HTTP/port 80)



Netwrok ACLs (Access control lists): -> optional layer of your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

Allow or deny rules.

Networks ACL works on Subnet (one or more subnet) - (one subnet can have multiple instance) 


NAT - (Network Address Trnaslation) Gateway: -> Enable instance in private subnet to conenct to the internet or other AWS services, but prevents the internet from initiating connections to those instances.


![alt text](VPC/nat_gateway.png)

![alt text](VPC/vpc_peering.png)

VPC Peering -> a networking connection between two vpc's that enables you to route traffic between them privately.

![alt text](VPC/vpc_endpoints.png)

VPC endpoints -> allow you to privately connect your vpc to supported AWS services and VPC endpoint services powered by aws privatelink.

ex. connection between ec2 instance to s3 

Bastion Host -> A special-purpose instance that provides secure access to your instance in private subnets.

![alt text](VPC/bastion_host.png)

Elastic IP Address -> Static IP addresses designed for dynamic cloud computing.

VPC Flow Logs -> Capture infromation about the IP traffic going and from network interfaces in your VPC.


Direct conenct -> establishes a dedicated netwrok connection from your premises to AWS.
![alt text](VPC/direct_connect.png)


AWS Client VPN -> Managed VPN service that enables secure remote access to AWS resources and on premises netwroks using OpenVPN-based clients.

