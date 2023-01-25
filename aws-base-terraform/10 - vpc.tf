resource "aws_vpc" "my-vpc" {
	cidr_block = var.vpc_cidr_block
	tags       = {
		Name = "${var.env_prefix}-my-vpc"
	}
}

resource "aws_subnet" "my-subnet-public" {
	vpc_id            = aws_vpc.my-vpc.id
	cidr_block        = var.subnet_cidr_block_public
	availability_zone = var.availability_zone
	tags              = {
		Name : "${var.env_prefix}-my-subnet-public"
	}
}

#resource "aws_subnet" "my-subnet-private" {
#	vpc_id            = aws_vpc.my-vpc.id
#	cidr_block        = var.subnet_cidr_block_private
#	availability_zone = var.availability_zone
#	tags              = {
#		Name : "${var.env_prefix}-my-subnet-private"
#	}
#}

resource "aws_route_table" "my-rt" {
	vpc_id = aws_vpc.my-vpc.id
	route {
		cidr_block = "0.0.0.0/0"
		gateway_id = aws_internet_gateway.my-igw.id
	}
	tags = {
		Name : "${var.env_prefix}-my-rt"
	}
}

resource "aws_route_table_association" "my-subnet-public-rta" {
	subnet_id      = aws_subnet.my-subnet-public.id
	route_table_id = aws_route_table.my-rt.id
}

#resource "aws_route_table_association" "my-subnet-private-rta" {
#	subnet_id      = aws_subnet.my-subnet-private.id
#	route_table_id = aws_route_table.my-rt.id
#}
