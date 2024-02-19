# # Base container name
# ARG BASE_NAME=python:3.11

# FROM $BASE_NAME as base

# ARG PACKAGE_NAME="lamini_classifier"

# # Install Ubuntu libraries
# RUN apt-get -yq update && apt-get -yqq install libpq-dev psmisc

# # Install python packages
# WORKDIR /app/${PACKAGE_NAME}
# COPY ./requirements.txt /app/${PACKAGE_NAME}/requirements.txt
# RUN pip install -r requirements.txt

# # Copy all files to the container
# COPY . /app/${PACKAGE_NAME}
# WORKDIR /app/${PACKAGE_NAME}

# ENTRYPOINT ["/app/lamini_classifier/scripts/start-classify.sh"]


# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
