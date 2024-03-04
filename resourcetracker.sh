#!/bin/bash

####################################
#Author: Mohammed Asif Raza
#Date: 03/03/2024

#Version: 1

# This Script will report the AWS resource usage

######################################

# AWS S3
# AWS EC2
# AWS LAMBDA
# AWS IAM USERS
chmod 777 awsscript.sh

set -x # Debug mode

# List S3 buckets
echo "Print list of S3"
aws s3 ls >> awsresourceTracker


# List EC2 Instances
echo "Print EC2 lists"
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Instance:InstanceId}'>> awsresourceTracker

# List Lambda Functions
echo "Print lambda functions"
aws lambda list-functions>> awsresourceTracker

# list IAM Users
echo "Print Iam Users"
aws iam list-users>> awsresourceTracker


