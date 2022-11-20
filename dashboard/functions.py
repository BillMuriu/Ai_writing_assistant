import os
import openai
from django.conf import settings

# Load your API key from an environment variable or secret management service
openai.api_key = settings.OPENAI_API_KEYS


def generateBlogTopicIdeas(topic, keywords, profile):
    blog_topics = []
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Generate Blog Topic ideas on the given topic. \ntopic: {}\nkeywords: {} \n *".format(topic, keywords),
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



def generateBlogSectionTitles(blogTopicIdea, keywords, profile):
    blog_sections = []
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Generate a blog outline for the following blog topic.\nblogTopicIdea: {}\nkeywords: {}\n*".format(blogTopicIdea, keywords),
      temperature=0.79,
      max_tokens=321,
      top_p=1,
      best_of=2,
      frequency_penalty=0,
      presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
            if not res == '':
                if profile.monthlyCount:
                    oldCount = int(profile.monthlyCount)
                else:
                    oldCount = 0

                oldCount += len(res.split(' '))
                profile.monthlyCount = str(oldCount)
                profile.save()
            else:
                return ''
        else:
            return []
    else:
        return []


    a_list = res.split('*')
    if len(a_list) > 0:
        for blog in a_list:
            blog_sections.append(blog)
    else:
        return []


    return blog_sections






###################FULL BLOG FUNCTION###############




def checkCountAllowance(profile):
    if profile.subscribed:
        type = profile.subscriptionType
        if type == 'free':
            max_limit = 5000
            if profile.monthlyCount:
                if int(profile.monthlyCount) < max_limit:
                    return True
                else:
                    return False
            else:
                return True
        elif type == 'starter':
            max_limit = 40000
            if profile.monthlyCount:
                if int(profile.monthlyCount) < max_limit:
                    return True
                else:
                    return False
            else:
                return True
        elif type == 'advanced':
            return True
        else:
            return False
    else:
        max_limit = 5000
        if profile.monthlyCount:
            if int(profile.monthlyCount) < max_limit:
                return True
            else:
                return False
        else:
            return True
