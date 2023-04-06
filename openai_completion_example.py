#!/usr/bin/env python

import os, json
import openai

def init_openai(openai_name, api_key):
  openai.api_type = "azure"
  openai.api_base = f"https://{openai_name}.openai.azure.com/"
  openai.api_version = "2022-12-01"
  openai.api_key = api_key


def generate_completion(engine, prompt):
  response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    temperature=1,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)
  return(response)

def load_from_env():
  """ get the specifics for this Azure OpenAI deployment for use with this project
  This reads the keys belows in a file called .env
  """
  from dotenv import load_dotenv
  load_dotenv()
  openai_name = os.getenv("OPENAI_NAME")
  api_key = os.getenv("OPENAI_API_KEY")
  openai_engine = os.getenv("OPENAI_ENGINE")
  if not(openai_name and api_key and openai_engine):
      raise Exception("a required environment setting is missing for openAI")
  return(openai_name,api_key,openai_engine)

  
  
if __name__ == "__main__":
  # read the .env file for configuration
  openai_name,api_key,openai_engine=load_from_env()
  # configure the global module openai
  init_openai(openai_name, api_key)
  
  # get prompt from the command line
  import sys
  prompt = sys.argv[1]
  
  # use global openai module to complete prompt
  openai_response = generate_completion(openai_engine, prompt)
  
  
  # get the first text completion from the openai response object
  response = json.loads(str(openai_response))
  # the response text is in an array called choices
  c = response.get('choices')
  # if there is something, get the first element
  if c:
    completion = c[0].get('text')
  
  print(f"AI completion:  {prompt}...")
  print(completion)

  
  
