#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]
then
    echo "Please provide a URL as an argument."
    exit 1
fi

# Send a GET request to the URL using curl and save the response to a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check the status code of the response
if [ "$response" == "200" ]
then
    # Send a GET request to the URL using curl and save the response body to a variable
    body=$(curl -s "$1")
    # Display the response body
    echo "$body"
else
    echo "$response"
fi

