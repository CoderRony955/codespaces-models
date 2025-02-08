from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from rich.console import Console

console = Console()

endpoint = "https://models.inference.ai.azure.com"
model_name = "Phi-3.5-MoE-instruct"
token = 'GITHUB_MODEL'

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

while True:
    user = input("What's your query? Enter here: ")
    if user == 'exit':
        break
    else:
        response = client.complete(
            messages=[
                SystemMessage(content="You are a helpful assistant."),
                UserMessage(content=user),
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model_name
        )

        console.print(response.choices[0].message.content, style='italic')
