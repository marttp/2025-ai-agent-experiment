import os
import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo, ModelFamily
from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.messages import MultiModalMessage
from autogen_core import Image
# from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
# from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

async def get_weather(city: str) -> str:
    return f"อุณหภูมิที่{city} คือ 35 องศา"

async def main():
    model_client_ollama = OpenAIChatCompletionClient(
        model="qwen3:8b",
        base_url=os.environ["OLLAMA_BASE_URL"],
        api_key="ollama",
        model_info=ModelInfo(
            vision=False,
            function_calling=True,
            json_output=True,
            family=ModelFamily.UNKNOWN,
            structured_output=True,
        ),
    )

    weather_agent = AssistantAgent(
        name="weather",
        model_client=model_client_ollama,
        system_message="คุณคือนักพยากรณ์อากาศ จงนำขัอมูลที่ได้มาสรุป และตอบกลับ",
        tools=[get_weather],
        reflect_on_tool_use=True, # ให้ Agent ดูแบบภาษามนุษย์ โดยให้ LLM ไป reflect คิดอีกทีนึง
    )

    stream = weather_agent.run_stream(task="ขอข้อมูลสภาพอากาศที่จังหวัดเชียงใหม่")
    await Console(stream)

async def vision():
    model_client_ollama = OpenAIChatCompletionClient(
        model="gemma3:12b",
        base_url=os.environ["OLLAMA_BASE_URL"],
        api_key="ollama",
        model_info=ModelInfo(
            vision=True,
            function_calling=True,
            json_output=False,
            family=ModelFamily.UNKNOWN,
            structured_output=True,
        )
    )

    vision_agent = AssistantAgent(
        name="vision",
        model_client=model_client_ollama,
        system_message="คุณคือนักวิเคราะห์รูปภาพ",
    )
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "present-image.png")

    message = MultiModalMessage(
        content=[
            "describe this image",
            Image.from_file(image_path),
        ],
        source="vision",
    )

    stream = vision_agent.run_stream(task=message)
    await Console(stream)

# async def code_executor():
#     local_code_executor = LocalCommandLineCodeExecutor(work_dir="coding")
#     docker_code_executor = DockerCommandLineCodeExecutor(work_dir="coding")
#     await docker_code_executor.start()

#     code_executor_agent = CodeExecutorAgent(
#         name="code_executor",
#         code_executor=docker_code_executor,
#     )

#     stream = code_executor_agent.run_stream(task="""
# ```python
# print("Hello World")
# ``` 
# """)
    
#     await Console(stream)
#     await docker_code_executor.stop()

# asyncio.run(main())
asyncio.run(vision())