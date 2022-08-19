/**
Vartija Terraform template
Copyright 2022 Alberto Morón Hernández

■ Table of Contents ■
  SETUP
  ECR
  IAM

═════════════════════════════════════════════════════════════════════════════ */

//  SETUP ──────────────────────────────────────────────────────────────────────

variable region {
  default = "eu-west-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.17.1"
    }
  }
}

provider aws {
  profile = "default"
  region  = var.region
}

data aws_caller_identity current {}

locals {
  account_id          = data.aws_caller_identity.current.account_id
  ecr_repository_name = "vartija"
  ecr_image_tag       = "latest"
}

//  ECR ────────────────────────────────────────────────────────────────────────

resource aws_ecr_repository repo {
  name = local.ecr_repository_name
}

resource null_resource ecr_image {
  triggers = {
    python_file = md5(file("${path.module}/vartija/main.py"))
    docker_file = md5(file("${path.module}/_docker/dev/Dockerfile.vartija.dev"))
  }

  provisioner "local-exec" {
  command = <<EOF
  aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${local.account_id}.dkr.ecr.${var.region}.amazonaws.com
  cd ${path.module}/_docker/dev/
  docker build -t ${aws_ecr_repository.repo.repository_url}:${local.ecr_image_tag} -f Dockerfile.vartija.dev ../..
  docker push ${aws_ecr_repository.repo.repository_url}:${local.ecr_image_tag}
EOF
  }
}

data aws_ecr_image lambda_image {
  depends_on = [
    null_resource.ecr_image
  ]
  repository_name = local.ecr_repository_name
  image_tag       = local.ecr_image_tag
}

//  IAM ────────────────────────────────────────────────────────────────────────

resource aws_iam_role lambda {
  name = "vartija-lambda-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}