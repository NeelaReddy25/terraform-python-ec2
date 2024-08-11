terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "5.59.0"
    }
  }
  backend "s3" {
    bucket = "neelareddy.stores"
    key = "terraform-python-ec2"
    region = "us-east-1"
    dynamodb_table = "neelareddy-dev"
  }
}

# Provide authentication here
provider "aws" {
  region = "us-east-1"
}