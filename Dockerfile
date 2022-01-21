# Inherit from the Python 3.9 image.
FROM python:3.9-slim

# Declare the working directory.
WORKDIR /contextuality

# Update Linux.
RUN apt update

# Install Python packages.
RUN python3 -m pip install --upgrade pip
RUN pip3 install --user --upgrade pip
RUN pip3 install scipy==1.7.1
RUN pip3 install numpy==1.20.3
RUN pip3 install pandas==1.3.4

# Install the package.
COPY setup.py .
COPY contextuality/ contextuality
RUN pip3 install .