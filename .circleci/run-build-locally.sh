#!/usr/bin/env bash

# script to test my config.yml file
#
# usage:
#   ./run-build-locally <git-hash>
#
# a new job has been created on circleci
#


CIRCLE_TOKEN=$(cat ./token.txt)

curl --user $CIRCLE_TOKEN: \
    --request POST \
    --form revision=$1 \
    --form config=@config.yml \
    --form notify=false \
        https://circleci.com/api/v1.1/project/github/gDelgado14/personal-site/tree/master
