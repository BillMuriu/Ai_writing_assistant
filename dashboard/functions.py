import os
import openai
from django.conf import settings

# Load your API key from an environment variable or secret management service
openai.api_key = settings.OPENAI_API_KEYS


def generateBlogTopicIdeas(topic, keywords):
    blog_topics = []
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Generate Blog Topic ideas on the following topic: {}\nKeywords: {} \n *".format(topic, keywords),
      temperature=0.79,
      max_tokens=321,
      top_p=1,
      best_of=2,
      frequency_penalty=0,
      presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            return []
    else:
        return []


    a_list = res.split('*')
    if len(a_list) > 0:
        for blog in a_list:
            blog_topics.append(blog)
    else:
        return []

    return blog_topics



def generateBlogSectionHeadings(topic, keywords):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Generate blog section headings and section titles, based on the following blog section topic.\nTopic: {}\nKeywords: {}\n*".format(topic, keywords),
      temperature=0.79,
      max_tokens=321,
      top_p=1,
      best_of=2,
      frequency_penalty=0,
      presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            res = None
    else:
        res = None

    return res
