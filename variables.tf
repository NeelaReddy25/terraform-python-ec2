variable "ami_id" {
  type    = string
  default = "ami-041e2ea9402c46c32"
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "cidr_blocks" {
  type = list
  default = ["0.0.0.0/0"]
}