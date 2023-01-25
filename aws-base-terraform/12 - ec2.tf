resource "aws_instance" "ec2" {
	ami                    = "ami-0747bdcabd34c712a"
	instance_type          = "t2.micro"
	subnet_id              = aws_subnet.my-subnet-public.id
#	vpc_security_group_ids = [aws_security_group.ec2-sg.id]
	security_groups = [aws_security_group.ec2-sg.id]
#	user_data = file("server-script.sh")
}

#resource "aws_eip" "eip" {
#	instance = aws_instance.ec2.id
#	tags     = {
#		Name : "${var.env_prefix}-eip"
#	}
#}
#
#output "eip" {
#	value = aws_eip.eip.public_ip
#}

resource "aws_security_group" "ec2-sg" {
	name        = "${var.env_prefix}-ec2-sg"
	description = "control SSH / HTTPS traffic to/from the EC2 instance"
	vpc_id      = aws_vpc.my-vpc.id

	ingress {
		from_port   = 22
		to_port     = 22
		protocol    = "tcp"
		cidr_blocks = [var.homepc_ip_cidr]
	}

	ingress {
		from_port   = 443
		to_port     = 443
		protocol    = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}

	egress {
		from_port       = 0
		to_port         = 0
		protocol        = "-1"
		cidr_blocks     = ["0.0.0.0/0"]
		prefix_list_ids = []
	}

	tags = {
		Name : "${var.env_prefix}-ec2-sg"
	}
}

#data "aws_ami" "my-ami" {
#	most_recent = true
#	owners      = ["amazon"]
#	filter {
#		name   = "architecture"
#		values = ["x86_64"]
#	}
#	filter {
#		name   = "virtualization-type"
#		values = ["hvm"]
#	}
#	filter {
#		name   = "name"
#		values = ["amzn2-ami—kernel—5*"]
#	}
#	filter {
#		name   = "root-device-type"
#		values = ["ebs"]
#	}
#}
