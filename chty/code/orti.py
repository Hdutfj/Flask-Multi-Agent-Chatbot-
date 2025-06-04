from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, InputGuardrail, GuardrailFunctionOutput, set_tracing_disabled, function_tool
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import asyncio
from pydantic import BaseModel

class TechnologyOutput(BaseModel):
    is_technology:bool
    reasoning:str
    
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

guardrail_agent= Agent(
    name="Guardrail agent",
    instructions="You should check that input is of the right type if not block that",
    output_type=TechnologyOutput,
    model=OpenAIChatCompletionsModel(model="gemini-1.5-flash",openai_client=provider)
)

async def Technologybrand(ctx, agent, input_data):
    result= await Runner.run(guardrail_agent, input_data, context=ctx)
    final_output=result.final_output_as(TechnologyOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=False
    )


robotic_agent = Agent(
    name="Robot Agent",
    handoff_description="Specialized about robotic technology",
    instructions="You should answer all questions  related to robots, their working advantages and all about them",
    model=OpenAIChatCompletionsModel(model="gemini-1.5-flash",openai_client=provider)
)

ConstructionTech_Agent = Agent(
    name="Robot Agent",
    handoff_description="Specialized about construction technology",
    instructions="You should answer all questions  related to construction including advanced buildings, advanced towers etc all about that",
    model=OpenAIChatCompletionsModel(model="gemini-1.5-flash",openai_client=provider)
)

GunsandPlanes_Agent = Agent(
    name="GunsandPlanes Agent",
    handoff_description="Specialized about guns and planes technology",
    instructions="You should answer all questions  related to guns, planes including advanced artilliary, advanced machinery etc all about that",
    model=OpenAIChatCompletionsModel(model="gemini-1.5-flash",openai_client=provider)
)

triage_agent= Agent(
    name="Select Agent",
    instructions="You should select which agent to call on the basis of input",
    handoffs=[ConstructionTech_Agent,GunsandPlanes_Agent,robotic_agent],
    model=OpenAIChatCompletionsModel(model="gemini-1.5-flash",openai_client=provider),
    input_guardrails=[InputGuardrail(guardrail_function=Technologybrand)]
)

async def get_chatbot_reply(user_input: str, category="auto") -> str:
    category = category.lower()

    if category == "robotics":
        result = await Runner.run(robotic_agent, input=user_input)
    elif category == "construction":
        result = await Runner.run(ConstructionTech_Agent, input=user_input)
    elif category == "guns_planes":
        result = await Runner.run(GunsandPlanes_Agent, input=user_input)
    elif category == "auto":
        result = await Runner.run(triage_agent, input=user_input)
    else:
        return "Sorry, I don't know anything about this topic."
    return str(result.final_output)
     