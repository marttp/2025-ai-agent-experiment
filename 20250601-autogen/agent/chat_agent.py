import os
import asyncio
from autogen_ext.models.openai import (
    OpenAIChatCompletionClient,
    AzureOpenAIChatCompletionClient,
)
from autogen_core.models import (
    ModelInfo,
    ModelFamily,
    SystemMessage,
    UserMessage,
    AssistantMessage,
)
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
import json
# from autogen_ext.models.cache import CHAT_CACHE_VALUE_TYPE
# from autogen_ext.cache_store.redis import RedisStore
# import redis


async def main():
    model_client_ollama = OpenAIChatCompletionClient(
        model="qwen3:8b",
        base_url=os.environ["OLLAMA_BASE_URL"],
        api_key="ollama",
        model_info=ModelInfo(
            vision=False,
            function_calling=False,
            json_output=False,
            family=ModelFamily.UNKNOWN,
            structured_output=True,
        ),
    )

    assistant_agent = AssistantAgent(
        name="assistant",
        model_client=model_client_ollama,
        system_message="You're a helpful personal assistant.",
    )

    while True:
        user_message = input("User: ")
        if user_message == "exit":
            break

        cancellation_token = CancellationToken()
        message = TextMessage(content=user_message, source="user")
        response = await assistant_agent.on_messages(
            messages=[message],
            cancellation_token=cancellation_token,
        )
        print(f"{response.chat_message.content}\n{response.chat_message.models_usage}")


asyncio.run(main())
