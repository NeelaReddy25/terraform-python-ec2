terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "5.59.0"
    }
  }
  backend "aws" {
    bucket = "neelareddy.stores"
    key = "terraform-python-ec2"
    region = "us-region-1"
    dynamodb_table = "neelareddy-dev"
  }
}

# Provide authentication here
provider "aws" {
  region = "ys-east-1"
}