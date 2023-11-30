## Using Microsoft OpenAI ChatGPT from Python

This is simple example code for working with OpenAI via Microsoft Azure.  While Azure provides an web 'playground' to explore it's AI services, you may want to automate working with "AI" services ( such as large language models like ChatGPT) for research, and this program is a complete example of that. 

This is intermediate exercise that assumes you know how to use the Azure command line or can use the portal, use python and install python libraries in a virtual environment. 

Do not use this program as part of a public web application or expose your secret keys and account names in anyway, ever.  You may be charged for each invocation in your Azure account.    Do not put the account keys directly in the code, and if you use the '.env' method to load secrets like keys, do not put .env into github. 


### Creating a 'model' to work with.  

To use this code, you must first create an OpenAI account in Azure in your resource group, and then create
a 'model' (which is also called a 'deployment') inside your account.    You can have multiple models in an account, and those models can use different back-end AI services.    You could for example create a model of ChatGPT version 3.5 and version 4.0, write a program to send the same prompt to both services, and use natural language processing (NLP) to analyze the differences.   

How to create an AI 'account' using the Portal or the command line:

https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=cli

If you have an existing resoure group, you create an account and then a model in two steps using the command line.  YOu need to install the Azure CLI, or just use the cloud shell https://portal.azure.com/#cloudshell/   The text in brackets `<example>` needs to be replaced with your values 

You must fist log-in and get your subscription ID: 

`az login`

A convenient way to show all of your subscriptions is in table format: 

`az account list -o table`

If you have multiple subscriptions you must select one. The the subscription ID number from the table above.  Save this number, you'll need it again 

`az account set -s <subscriptionID>`

Note for the commands below I'm just using the `eastus` location for convenience, but change this to any other location code that supports Cognitive services.  Not all of them do. 

In the subscription in your resource group, create an AI account. the 'myCognitiveServicesAccountName' can be anything with letters, numbers and hyphens.  I suggest using your organization ID (NetID for us), the project you are working in, and 'AI'   For the MSU Cloud Computing Fellowship, I used `billspat-ccf23-ai` for `<myCognitiveServicesAccountName>`

```
az cognitiveservices account create \
--name <myCognitiveServicesAccountName> \
--resource-group <myResourceGroupName> \
--location eastus \
--kind OpenAI \
--sku s0 \
--subscription <subscriptionID>
```

Now create a 'deployment' in that account where you select an AI model/service to work with.  the example python program  here has been tested with ChatGPT 3.5
You can set `myModelName` to anything but make sure to indicate what the model is for so  you an keep track.  You need this to work with the program below.  `model-name` below is one of the choices from Azure, not the name you pick.  A description of the options for `model-name` are here: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models, but it can be hard to find the actual 'name' you can put in the command. 

Get a list of current model names you can use this command which uses the query option to filter out just the Azure names and the Azure model version numbers available in tabular format: 

`az cognitiveservices model list --location eastus --query "[].model.[name, version]" -o table`

This doesn't list any of the capabilities/limitations, so be sure to look that up on the Azure documentation linked above.   Note as of today all the models listed have format 'OpenAI' , sku-capacity 1 and sku-name "Standard" but that could change at any time.   

the comand below creates the model you can use.   Select the model/version, your resource group from above, your myCognitiveServicesAccountName from above.  You can use the deployment name in the code.  

```
az cognitiveservices account deployment create \
--name <myCognitiveServicesAccountName> \
--resource-group  <myResourceGroupName> \
--deployment-name <MyDeploymentName> \
--model-name <AzureModelName> \
--model-version <AzureModelVersion>  \
--model-format OpenAI \
--sku-capacity "1" \
--sku-name "Standard"
```

Now from that model you need to get a 'key' to be able to use the program below.   There are two keys associated with any Azure CognitiveServices account (the same keys for all deployments in that account).   You can show those in the portal, or using 

`az cognitiveservices account keys list --resource-group <myResourceGroupName>--name <myCognitiveServicesAccountName>`

There are two keys and either will work.  If you have given out keys and want to revoke access to those who have them, you can regenerate the keys and you'll have to replace the keys in your configuration file with the new ones. 

`az cognitiveservices account keys regenerate --name myresource --resource-group cognitive-services-resource-group --key-name key1`

This allows you to revoke access from any app that relies on one of your keys. 

In the configuration for the python script below, you'll need one of these keys (stored as OPENAI_API_KEY), the account name, and the model deployment name you created above.  ( the script looks for variables OPENAI_API_KEY, OPENAI_NAME, and OPENAI_DEPLOYMENT)

### Sample Python Code

This very small sample code demonstrates how to call an existing model

1. You may need to first get access to OpenAI.   Only available to select customers for now, 
   provide your subscription ID and company information
1. create an OpenAI resource 
     - see the Azure documentation for details
1. In that resource, open in AI Studio and create a deployment
1. create a configuration file and name it `.env`
    - see the "example_dotenv.txt" file for contents
    - get the values as described above using the Azure CLI, or from the Azure portal.  
1. create a python virtual environment in this folder.  You must have a version of python installed with virtualenv installed.  This is strongly encourage so that the libraries we install for this example won't conflict with other projects.   There are many instructions on line for this. 
    - use command `virtualenv -p 3.10 .venv` \
    this creates a folder named `.venv` \ 
    the name `.venv` is not required but convention
1. activate the virtual environment using the terminal: 
   `source .venv/bin/activate`
1. install the openai library.  
   - `pip install openai`
   - `pip install python-dotenv`
1. run the python script from the command line (in two ways): 
   - with a single prompt: `python openai_completion_example.py "Is AI useful for anything?"`
   - start a chat session: `python openai_completion_example.py chat` \
     enter prompts that are related.  The program sends previous prompts to try to make it more conversation like. 

### Sample Shell Script

There is an example that uses the REST api and the shell.  No python is needed.  


1. create a file `.env` as described above following the example file `example_dotenv.txt`

2. From the terminal, Azure cloud shell,  or Linux shell in windows), run the command `./complete_this.sh 
   

