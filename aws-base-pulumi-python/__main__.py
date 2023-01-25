import pulumi
import pulumi_aws as aws
from utils import get_prefixed_value

config=pulumi.Config()

##########################################
# VPC, subnets, routing tables, gateways
##########################################
# virtual public cloud
vpc_name=get_prefixed_value(config.require('vpc-name'))
vpc_cidr_block=config.require('vpc-cidr-block')

vpc=aws.ec2.Vpc(vpc_name,
                cidr_block=vpc_cidr_block,
                tags={'Name':vpc_name})

# public subnet
subnet_public_info=config.require_object('subnet-public-info')
subnet_public_name=get_prefixed_value(subnet_public_info.get('name'))
subnet_public=aws.ec2.Subnet(subnet_public_name,
                             vpc_id=vpc.id,
                             cidr_block=subnet_public_info.get('cidr-block'),
                             map_public_ip_on_launch=True,
                             tags={
	                             'Name':subnet_public_name,
                             })

# private subnet
subnet_private_info=config.require_object('subnet-private-info')
subnet_private_name=get_prefixed_value(subnet_private_info.get('name'))
subnet_private=aws.ec2.Subnet(subnet_private_name,
                              vpc_id=vpc.id,
                              cidr_block=subnet_private_info.get('cidr-block'),
                              map_public_ip_on_launch=False,
                              tags={
	                              'Name':subnet_private_name,
                              })

# internet gateway
igw_name=get_prefixed_value(config.require('igw-name'))
igw=aws.ec2.InternetGateway(igw_name,
                            vpc_id=vpc.id,
                            tags={
	                            'Name':igw_name,
                            })

# routing table for public subnet
rt_public_name=get_prefixed_value(config.require('rt-public-name'))
rt_public=aws.ec2.RouteTable(rt_public_name,
                             vpc_id=vpc.id,
                             routes=[
	                             aws.ec2.RouteTableRouteArgs(
		                             cidr_block="0.0.0.0/0",
		                             gateway_id=igw.id,
	                             )
                             ],
                             tags={
	                             'Name':rt_public_name
                             })
rta_public=aws.ec2.RouteTableAssociation(
	get_prefixed_value(config.get("rta-public-name")),
	route_table_id=rt_public.id,
	subnet_id=subnet_public.id
)

# elastic IP
eip_natgw_name=get_prefixed_value(config.require('eip-natgw-name'))
eip_natgw=aws.ec2.Eip(eip_natgw_name,
                      vpc=True,
                      tags={
	                      'Name':eip_natgw_name
                      })

# NAT gateway
natgw_name=get_prefixed_value(config.require('natgw-name'))
natgw=aws.ec2.NatGateway(natgw_name,
                         allocation_id=eip_natgw.allocation_id,
                         subnet_id=subnet_public.id,
                         tags={
	                         'Name':natgw_name,
                         },
                         opts=pulumi.ResourceOptions(depends_on=[igw]))

# routing table for private subnet
rt_private_name=get_prefixed_value(config.require('rt-private-name'))
rt_private=aws.ec2.RouteTable(rt_private_name,
                              vpc_id=vpc.id,
                              routes=[
	                              aws.ec2.RouteTableRouteArgs(
		                              cidr_block="0.0.0.0/0",
		                              gateway_id=natgw.id,
	                              )
                              ],
                              tags={
	                              'Name':rt_private_name,
                              })
rta_private=aws.ec2.RouteTableAssociation(
	get_prefixed_value(config.get("rta-private-name")),
	route_table_id=rt_private.id,
	subnet_id=subnet_private.id
)

##########################################
# EC2 instances
##########################################

# security groups (for EC2 instances)
sg_name=get_prefixed_value(config.require('sg-name'))
sg=aws.ec2.SecurityGroup(
	sg_name,
	vpc_id=vpc.id,
	description="Allow HTTP traffic to EC2 instance",
	ingress=[
		{
			"protocol":"tcp",
			"from_port":80,
			"to_port":80,
			"cidr_blocks":["0.0.0.0/0"],
		},
		{
			"protocol":"tcp",
			"from_port":443,
			"to_port":443,
			"cidr_blocks":["0.0.0.0/0"],
		},
		{
			"protocol":"tcp",
			"from_port":22,
			"to_port":22,
			"cidr_blocks":["0.0.0.0/0"],
		}
	],
	egress=[
		{
			"protocol":"-1",
			"from_port":0,
			"to_port":0,
			"cidr_blocks":["0.0.0.0/0"],
		}
	],
	tags={
		'Name':sg_name,
	}
)

# key pair for SSH access to public EC2
keypair=aws.ec2.KeyPair("keypair",public_key=config.get("public-SSH-key"))

# EC2 SSH instance
ec2_ssh_name=get_prefixed_value(config.require('ec2-ssh-name'))
ec2_ssh=aws.ec2.Instance(
	ec2_ssh_name,
	instance_type=config.get("ec2-ssh-type"),
	vpc_security_group_ids=[sg.id],
	ami=config.require('ec2-ami-id'),
	key_name=keypair.key_name,
	#	user_data=user_data,
	subnet_id=subnet_public.id,
	associate_public_ip_address=True,
	tags={
		'Name':ec2_ssh_name,
	}
)

user_data="""
#!/bin/bash
echo "Hello from ec2-webserver instance!" > index.html
nohup python -m SimpleHTTPServer 80 &
"""

# EC2 WebServer instance
ec2_webserver_name=get_prefixed_value(config.require('ec2-webserver-name'))
ec2_webserver=aws.ec2.Instance(
	ec2_webserver_name,
	instance_type=config.get("ec2-webserver-type"),
	vpc_security_group_ids=[sg.id],
	ami=config.require('ec2-ami-id'),
	key_name=keypair.key_name,
	user_data=user_data,
	subnet_id=subnet_public.id,
	associate_public_ip_address=True,
	tags={
		'Name':ec2_webserver_name,
	}
)
eip_main_name=get_prefixed_value(config.require('eip-main-name'))
eip_main=aws.ec2.get_elastic_ip(
	tags={
		"Name":eip_main_name,
	})
eip_assoc=aws.ec2.EipAssociation("eipAssoc",
                                 instance_id=ec2_webserver.id,
                                 allocation_id=eip_main.id)

ec2_private_name=get_prefixed_value(config.require('ec2-private-name'))
ec2_private=aws.ec2.Instance(
	ec2_private_name,
	instance_type=config.get("ec2-private-type"),
	vpc_security_group_ids=[sg.id],
	ami=config.require('ec2-ami-id'),
	#	ami=ami.id,
	key_name=keypair.key_name,
	subnet_id=subnet_private.id,
	tags={
		'Name':ec2_private_name,
	}
)

pulumi.export('result',{
	'vpc.name':vpc.tags['Name'],
	'eip_main.public_ip':eip_main.public_ip
})
