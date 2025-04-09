import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from dotenv import load_dotenv
import os

from datetime import datetime

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=OPEN_AI_API_KEY,
)

async def get_time() -> str:
    return f"The time is currently {datetime.now()}."

agent = AssistantAgent(
    name="time_agent",
    model_client=model_client,
    tools=[get_time],
    system_message="You return the current time.",
    reflect_on_tool_use=True,
    model_client_stream=True
)

async def main() -> None:
    await Console(agent.run_stream(task="What time is it?"))
    await model_client.close()

asyncio.run(main())
