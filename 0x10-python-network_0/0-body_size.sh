#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]
then
    echo "Please provide a URL as an argument."
    exit 1
fi

# Send a request to the URL using curl and save the response to a variable
response=$(curl -s "$1")

# Get the size of the response body in bytes
size=$(echo "$response" | wc -c)

# Display the size of the response body in bytes
echo "$size"

