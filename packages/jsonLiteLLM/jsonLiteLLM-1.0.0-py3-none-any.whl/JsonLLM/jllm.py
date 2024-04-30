from litellm import acompletion
import asyncio
import json
import regex
from jsonschema import validate, ValidationError
import time
import requests



class NoJson(Exception):...

class MaxRetriesExceeded(Exception):...

class JsonLLM:
    def __init__(self, schema=None, endpoint='http://localhost:11434', model='ollama/llama3', api_key=None, retries=3, backoff_factor=2):
        self.api_key = api_key
        self.endpoint = endpoint
        self.model = model
        self.schema = schema
        self.retries = retries
        self.backoff_factor = backoff_factor
        self.SYSTEM_PROMPT = f"""Instructions:
You are JSON LLM model your output is only JSON format
{f'Your output follows the folowing schema: {schema}' if schema else ''}
"""
        self.DEFAULT_SCHEMA = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
            },
            "required": [],
            "additionalProperties": True
        }
        if not self.schema:
            self.schema = self.DEFAULT_SCHEMA 

    def _send_request(self, json_prompt):
        """
        Send a request to the LLM API and return the response. using LiteLLm
        """

        response = asyncio.run(acompletion(
            model=self.model,
            messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": json_prompt},
                ],
                api_base=self.endpoint
            )
        )

        response = response.choices[0].message.content
        
        return response

    @staticmethod
    def extract_json(text):
        # This regex pattern is designed to match a JSON object using recursive patterns
        pattern = r'\{(?:[^{}]|(?R))*\}'
        match = regex.search(pattern, text)
        if match:
            return match.group()
        else:
            raise NoJson('No json found')
    
    def clean_raw_response(self, raw_response):
        """
        1- Extract json from text
        """
        json_response_str = self.extract_json(raw_response)
        return json_response_str

    def send_request(self, json_prompt):
        raw_response = self._send_request(json_prompt)
        response = self.clean_raw_response(raw_response)
        return response

    def validate_response(self, response):
        """
        Validate the response against the predefined schema.
        """
        json_response = json.loads(response)
        validate(instance=json_response, schema=self.schema)

    def query_model(self, json_prompt):
        """
        Send a JSON prompt to the LLM, validate the response, and handle retries.
        """
        attempts = 0
        while attempts < self.retries:
            try:
                response = self.send_request(json_prompt)
                self.validate_response(response)
                return response
            except (requests.HTTPError, ValidationError, json.decoder.JSONDecodeError) as e:
                print(f"Attempt {attempts + 1} failed: {e}")
                attempts += 1
                time.sleep(self.backoff_factor ** attempts)
        raise MaxRetriesExceeded("Maximum retries exceeded with no valid response.")

