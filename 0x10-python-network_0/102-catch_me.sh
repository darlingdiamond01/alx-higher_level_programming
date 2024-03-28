#!/bin/bash

# Make a request to 0.0.0.0:5000/catch_me with curl, sending POST request with -X flag
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"

