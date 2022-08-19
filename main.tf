/**
Vartija Terraform configuration
Copyright 2022 Alberto Morón Hernández

■ Table of Contents ■
  SETUP

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
