#!/bin/sh

IMAGE_NAME=contextuality

# Format the code as per PEP8.
{
echo "Cleaning up the code with autopep8..."
autopep8 --in-place --aggressive --aggressive ./*.py
} ||
{
echo "WARNING: pip3 install autopep8 if you would like to format your code."
}

# Create a Docker image.
docker build --tag=$IMAGE_NAME .
