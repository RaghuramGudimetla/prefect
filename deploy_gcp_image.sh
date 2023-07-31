export flow_name=$1
export artifact_registry="australia-southeast1-docker.pkg.dev/raghuram-exec/prefect-repo"

gcloud auth configure-docker australia-southeast1-docker.pkg.dev

# Building the docker image using Dockerfile
docker build -t $flow_name:latest -f gcp-image/Dockerfile --build-arg flow_name=$flow_name .

# Docker push steps
docker tag $flow_name:latest $artifact_registry/$flow_name:latest

# Docker push
docker push $artifact_registry/$flow_name

# Go the flows directory
cd flows/$flow_name

# Run the deployment
python deploy.py