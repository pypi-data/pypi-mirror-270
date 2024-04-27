import functools
from enum import Enum
from google.cloud import pubsub_v1
import json
import time
from concurrent import futures

import logging
logger = logging.getLogger(__name__)

#TODO we should be able to detect the provider automatically and for now we could focus on Google
class CloudProvider(Enum):
    Google = 1
    OpenAI = 2
    # Other cloud providers...
    
class Identifier(Enum):
    PALM = 1
    GEMINI = 2

class MonitoringClient:
    def __init__(self, cloud_provider,topic_name, **kwargs):
        print("init")
        self.project = kwargs.get('project')
        self.cloud_provider = cloud_provider
        self.topic_name = f"projects/{self.project}/topics/{topic_name}"
        self.monitored_attributes = {}
        # Other initialization logic
        self.publisher = pubsub_v1.PublisherClient()
        #self.topic_name = 
        self.publish_futures = []

    def measure_response_time(self, func, *args, **kwargs):
        import time
        start_time = time.time()  # Start timing
        response = func(*args, **kwargs)  # Execute the function and capture the response
        end_time = time.time()  # End timing
        response_time_ms = (end_time - start_time) * 1000  # Calculate response time in ms
        return response_time_ms, response

    def get_attribute(self, attribute_name):
        return self.monitored_attributes.get(attribute_name, None)
    
    def publish_message(self):
        message = b"Hello, Pub/Sub!"
        future = self.publisher.publish(self.topic_name, data=message)
        print(f"Published message: {message}")
        return future.result()

    def monitor(self, func, client, model_name, identifier):
       
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            
            #print("args")
            #print(args)
            #print(args[0][0])
            #print("response")
            #print(response)
            #print("kwargs")
            #print(kwargs)
            #attrs = {attr: getattr(client, attr) for attr in dir(client)
            #         if not callable(getattr(client, attr)) and not attr.startswith("_")}
            #print("Attributes of the model before execution:", attrs)
           
            #response_time, response = self.measure_response_time(func(*args, **kwargs))
            response_time, response = self.measure_response_time(func, *args, **kwargs)

            response = func(*args, **kwargs)
            #print("RESPONSE")
            #print(response)
            #print(response_time)
            
            
            #new_attrs = {attr: getattr(client, attr) for attr in dir(client)
            #             if not callable(getattr(client, attr)) and not attr.startswith("_")}
            #print("Attributes of the model after execution:", new_attrs)
           
            # Here, you can add the actual monitoring logic
            # For now, it just calls the function
            
            temperature = None
            top_p = None
            prompt = None
            generation = None
            input_token_count = None
            output_token_count = None
            total_token_count = None
            
            if identifier == Identifier.PALM:
                temperature = kwargs["temperature"]
                top_p = kwargs["top_p"]
                prompt = ""
                generation = response.text
                
            if identifier == Identifier.GEMINI:
                temperature = kwargs['generation_config']['temperature']
                top_p = kwargs['generation_config']['top_p']
                prompt = args[0][0]
                # TODO never encountered multiple parts but apparently it is possible
                # TODO check that again as this is a potential bug cause
                generation = response.candidates[0].content.parts[0].text 
                input_token_count = response._raw_response.usage_metadata.prompt_token_count
                output_token_count = response._raw_response.usage_metadata.candidates_token_count
                total_token_count = response._raw_response.usage_metadata.total_token_count
            
            message = json.dumps({
                "model_name": model_name.split('/')[-1],
                "response_time": response_time,
                "temperature": temperature,
                "top_p": top_p,
                "prompt": prompt,
                "generation": generation,
                "input_token_count": input_token_count,
                "output_token_count": output_token_count,
                "total_token_count": total_token_count
            }).encode('utf-8')
            
            #todo use the API to get the billable characters since this a dedicated API that takes time 
            # we do this as a workflow service step
            
            #print(response._raw_response.usage_metadata)
            
            start_time = time.time()
            future = self.publisher.publish(self.topic_name, data=message)
            future.result()  # Block until the message has been confirmed as published
            end_time = time.time()
            duration = (end_time - start_time) * 1000
    
            print(f"Time taken to publish the message: {duration} ms")
            logger.error(f"Time taken to publish the message: {duration} ms")
           
            return response
        
        return wrapper


    
