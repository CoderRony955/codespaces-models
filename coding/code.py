import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "Meta-Llama-3.1-8B-Instruct"
token = 'GITHUB-TOKEN'

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

prompt = """"
Create a cool and fully functional gaming website landing page using HTML, TAILWIND CSS and JAVASCRIPT. Firstly add fully responsive sticky navigation bar with the tabs 'Home', 'Explore', 'About', 'Contact' and in mobile and tablet view add hameburger at the right side of the corner of the navbar and when we click on it then navbar open with smooth animation effect, Now after this add hero section with background image and write on the hero section 'Welcome to gaming planet' and add button bottom of this heading for 'Explore' and after hero section add cards with different games with their names desccription and button and in the last add cool footer with company logo and all social media logos"""


response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

with open('index.html', 'w') as file:
    file.write(response.choices[0].message.content)