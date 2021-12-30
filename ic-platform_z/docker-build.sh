#!/bin/sh

# usage: docker-build.sh GITHUB_TOKEN_FILE [DOCKER_TAG]
#   GITHUB_TOKEN_FILE should be a file containing a GitHub Access Token

project_root="$(dirname "$0")"
echo $1
DOCKER_BUILDKIT=1 docker build "$project_root" \
    -t ghcr.io/zoetisdenmark/ic-platform:${2:-latest} \
    --secret id=github-token,src="$1"
