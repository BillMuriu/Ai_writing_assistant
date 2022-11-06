import os
import openai
from django.conf import settings

# Load your API key from an environment variable or secret management service
openai.api_key = settings.OPENAI_API_KEYS

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generateBlogTopicIdeas(topic, keywords):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Generate Blog Topic ideas on the following topic: {} \n Keywords: {} \n".format(topic, keywords),
      temperature=0.79,
      max_tokens=321,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)

    return response
