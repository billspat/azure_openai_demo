Using Microsoft OpenAI completion 

1. get access to OpenAI.   Only available to select customers for now, 
   provide your subscription ID and company information
1. create an OpenAI resource 
     - see the Azure documentation for details
1. In that resource, open in AI Studio and create a deployment
1. create a configuration file and name it `.env`
    - see the "example_dotenv.txt" file for contents
    - get the values from the Azure port, in the "Azure OpenAI" resource
1. run the completion script from the terminal:
     - `./complete_this.sh
1. create a python virtual environment in this folder.  You must have a version of python installed with virtualenv installed.  This is strongly encourage so that the libraries we install won't conflict with other projects
    1. use command `virtualenv -p 3.10 .venv`
    1. this creates a folder named `.venv`
    1. the name `.venv` is not required but convention
1. activate the virtual environment using the terminal: 
   `source .venv/bin/activate`
1. install the openai library.  
   - `pip install openai`
   - `pip install python-dotenv`
1. run the python script from the command line: 
   `python openai_completion_example.py "A very important question is"`
