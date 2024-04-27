import logging
from typing import Dict, Optional

import google.generativeai as genai
from google.generativeai.generative_models import GenerativeModel

from ...exceptions import RetryableError
from ...objects import Response
from ...utilities import JsonUtility
from ..provider import Provider as BaseProvider


class Provider(BaseProvider):
    _required_attributes = {
        'api_key': None,
        'model': 'gemini-1.5-pro-latest',
    }

    def __init__(self,
                 logger: Optional[logging.Logger] = None,
                 attributes: Optional[Dict] = None):
        super().__init__(logger=logger, attributes=attributes)
        self._client = self.get_client()

    def get_client(self) -> GenerativeModel:
        genai.configure(
            api_key=self.get_attribute('api_key', default_value=None))
        model = genai.GenerativeModel(
            model_name=self.get_attribute('model', default_value=None))
        return model

    async def generate(self,
                       prompt: str,
                       function: Response,
                       language: str = "en",
                       act_as: Optional[str] = None) -> Optional[Dict]:

        generated_prompt = self.generate_prompt(
            prompt=prompt,
            function=function,
            language=language,
            act_as=act_as,
        )

        try:
            response = self._client.generate_content(generated_prompt)
        except Exception as e:
            print(e)
            raise RetryableError(f"Google API exception: {e}")

        result = JsonUtility.extract_json_block(text=response.text)
        if not isinstance(result, dict):
            raise RetryableError('Failed to extract json block')

        return result
