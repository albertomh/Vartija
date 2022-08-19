/**
Vartija Terraform template
Copyright 2022 Alberto Morón Hernández

■ Table of Contents ■
  SETUP
  ECR

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
