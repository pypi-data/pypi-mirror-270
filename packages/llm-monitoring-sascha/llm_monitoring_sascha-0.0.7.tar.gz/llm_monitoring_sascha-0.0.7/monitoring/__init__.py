from .client import MonitoringClient, CloudProvider, Identifier

client = None
from enum import Enum

def initialize(cloud_provider, topic_name, **kwargs):
    global client
    client = MonitoringClient(cloud_provider, topic_name, **kwargs)

def monitor(func):
    print(func)
    
    for attribute in dir(func):
        # Filter out private and special methods
        if not attribute.startswith('__'):
            try:
                #value = getattr(func, attribute)
                #print(f"{attribute}: {value}")
                print(f"{attribute}")
            except AttributeError as e:
                print(f"{attribute}: Could not access value")
                
    #print("Model name", func._model_name) #gemini
    #print("Model ID:", func._model_id)
    #print("Model ressoure name:", func._model_resource_name)
    #print("endpoint:", func._endpoint)  
    #print("endpoint_name:", func._endpoint_name)    

    
    if client is None:
        raise Exception("SDK not initialized. Call initialize() first.")

    print(client.cloud_provider)
    
    #if client.cloud_provider == CloudProvider.Google and hasattr(func, 'generate_content'):
    if hasattr(func, 'generate_content'):
        #TODO figure out if there is a more generic way to get the model name
        #test how that works with openai and PaLM models
        model_name = getattr(func, "_model_name")
        func.generate_content = client.monitor(func.generate_content, client, model_name, Identifier.GEMINI)
    
    #TODO this is PaLM test again
    #if client.cloud_provider == CloudProvider.Google and hasattr(func, 'predict'):
    if hasattr(func, 'predict'):
        model_name = getattr(func, "_model_resource_name")
        func.predict = client.monitor(func.predict, client, model_name, Identifier.PALM)

    if client.cloud_provider == CloudProvider.OpenAI and hasattr(func.chat.completions, 'create'):
        func.chat.completions.create = client.monitor(func.chat.completions.create, client)
    
    # we are only interested in the actual calls made to the LLM
    # all others can be ignored
    return func

