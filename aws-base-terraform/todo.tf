#resource "aws_instance" "myapp_server" {
#	ami             = data.aws_ami.latest-amazon-linux-image.id
#	instance_type   = "t2.micro"
#	security_groups = [aws_security_group.my_security_group.name]
#	user_data       = file("server-script.sh")
#	tags            = {
#		Name : "web-server"
#	}

#=====================


#
#resource "aws_route_table_association" "demo-rta-public" {
#	subnet_id      = aws_subnet.demo-subnet-1a-public.id
#	route_table_id = aws_route_table.demo-route-table-public.id
#}
#
#
#resource "aws_route" "demo-route-public-igw" {
#	route_table_id         = aws_route_table.demo-route-table-public.id
#	destination_cidr_block = "0.0.0.0/0"
#	gateway_id             = aws_internet_gateway.demo-igw.id
#}

#resource "aws_route_table_association" "demo-rta-public-igw" {
#	#	subnet_id      = aws_subnet.demo-subnet-1a-public.id
#	route_table_id = aws_route_table.demo-route-table-public.id
#	gateway_id     = aws_internet_gateway.demo-igw.id
#}


######################################

#resource "aws_s3_bucket" "tf_course" {
#	bucket = "tf-course-9348509384590"
#	acl    = "private"
#}


# # elastic IP
# resource "aws_eip" "my_eip" {
#   instance = aws_instance.web-server.id
#   tags     = {
# 	Name : "my-eip"
#   }
# }
#
#
# variable "ingress" {
#   type    = list(string)
#   default = ["80", "443"]
# }
#
# variable "egress" {
#   type    = list(string)
#   default = ["80", "443"]
# }
#
#
#
# output "PrivateIP" {
#   value = aws_instance.web-server.private_ip
# }
#
# output "PublicIP" {
#   value = aws_eip.my_eip.public_ip
# }


#

#resource "aws_route_table_association" "a-rtb-subnet" {
#  subnet_id      = aws_subnet.myapp-vpc-subnet-1.id
#  route_table_id = aws_route_table.myapp-route-table.id
#}
