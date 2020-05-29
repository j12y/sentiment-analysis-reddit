#!/bin/bash

# Environment variables are a convenient way to keep
# secrets out of your code.  I recommend copying this
# file to my-env.sh and then using it to populate these
# variables.  If you use a shell other than bash you
# may need to adjust your configuration.

# For read access
export REDDIT_USERNAME="your-reddit-username"
export REDDIT_CLIENT_ID="your-reddit-client-id"
export REDDIT_CLIENT_SECRET="your-reddit-client-secret"
export REDDIT_USER_AGENT="web:sentiment-analysis:v0.0.1 (by $REDDIT_USERNAME)"

# To gain write access
export REDDIT_PASSWORD="your-reddit-password"
