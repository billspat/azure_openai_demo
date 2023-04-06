#!/bin/bash
source .env

# TODO check if $1 is something, and if not, ask for a prompt
if [[ -z "$1" ]];then
  echo "enter the prompt you want to complete, and press enter:"
  read AI_PROMPT
else
  AI_PROMPT=$1
fi

AI_URL="https://${OPENAI_NAME}.openai.azure.com/openai/deployments/${OPENAI_ENGINE}/completions?api-version=2022-12-01/" 
echo $AI_URL

PAYLOAD='{"prompt": "'$AI_PROMPT'","max_tokens": 100,"temperature": 1,"frequency_penalty":0,"presence_penalty": 0,"top_p": 0.5,"stop": null}'
echo $PAYLOAD

curl $AI_URL \
  -H "Content-Type: application/json" \
  -H "api-key: $OPENAI_API_KEY" \
  -d '{"prompt": '"$AI_PROMPT"',"max_tokens": 100,"temperature": 1,"frequency_penalty":0,"presence_penalty": 0,"top_p": 0.5,"stop": null}'
