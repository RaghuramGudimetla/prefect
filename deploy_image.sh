export flow_name=$1
export AWS_ACCESS_KEY_ID=$2
export AWS_SECRET_ACCESS_KEY=$3

# Create a repository
aws ecr describe-repositories --repository-names $1 || aws ecr create-repository --repository-name $1 --image-tag-mutability MUTABLE

# Building the docker image using Dockerfile
docker build -t $1:latest --build-arg flow_name=$1 .

# Docker push steps
docker tag $1:latest 886192468297.dkr.ecr.ap-southeast-2.amazonaws.com/$1

# ECR Login
aws ecr get-login-password | docker login --username AWS --password-stdin 886192468297.dkr.ecr.ap-southeast-2.amazonaws.com

# Docker push
docker push 886192468297.dkr.ecr.ap-southeast-2.amazonaws.com/$1

# Go the flows directory
cd flows/$flow_name

# Run the deployment
python deploy.py