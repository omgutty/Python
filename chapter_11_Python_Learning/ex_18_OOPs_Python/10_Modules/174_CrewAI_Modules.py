# 174_CrewAI_Modules.py
# Topic: Modules used by a real AI agent (CrewAI test-analyst agent)
#
# This is a copy of chapter_12_CrewAI/01_test_analyst_Agent.py - the
# first working AI agent in this repo. It is placed here as a MODULES
# study reference: look at WHICH modules/classes it imports and why.
#
# Modules used:
#   from crewai import Agent, Task, Crew  -> CrewAI framework (pip install crewai)
#   from crewai import LLM                 -> the "brain" wrapper (LLM provider)
#   from dotenv import load_dotenv         -> python-dotenv: read .env secrets
#   import os                              -> os.getenv: read env variables
#
# The agent flow (5 steps):
#   1. Set up the Brain   -> LLM (Groq gpt-oss-120b via OpenAI-compatible API)
#   2. Define the Agent   -> role / goal / backstory (identity)
#   3. Give the Task      -> description + expected output
#   4. Build the Crew     -> agents + tasks together
#   5. Kick Off           -> crew.kickoff() runs everything

# Test Ananlyst Agent
# 
# a senior QA with 15 years (JIRA MD)
#  of experience. Based on the feature, 
# it will just analyze the requirement
# and suggest a 5-10 testcases(p0 testcases).

from crewai import Agent,Task, Crew
from crewai import LLM
from dotenv import load_dotenv
import os


# By Default crew AI actually the brain which
# OpenAI - GROQ API Key


# Step 0 - Set up the Brain
# Step 1. - Define the Agent (identity)
# Step 2. - Give the Task to the Agent
# Step 3. Add them to the Crew
# Step 4. Kick Off Agent.

# Prompt vs Skill vs AI Agent

# We need use the GROQ gpt-oss-120b model


# Step 0 - Set up the Brain (Groq LLM)
load_dotenv()  # reads the .env file in this folder

# Groq exposes an OpenAI-compatible API, so we use the "openai/" provider
# prefix with a custom base_url pointing at Groq.
# GROQ_MODEL in .env = openai/gpt-oss-120b (exact ID from groq.com console)
groq_llm = LLM(
    model=f"openai/{os.getenv('GROQ_MODEL')}",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_BASE_URL"),
)

# Step 1. - Define the Agent (identity)
qa_agent = Agent(
    role="QA Enginner",
    goal="Analyse the feature or the requirements, and create 5-10 test cases out of it.",
    backstory="You are a senior QA engineer with 15 years of experience in test planning and testcases creation",
    llm = groq_llm,
    verbose=True
)

# Step 2 - Give the Task to the Agent
test_case_task = Task(
    description="Create 5-10 test cases",
    expected_output="A numbered list of 5-10 test cases with brief descriptions for a app.vwo.com Login page with the username, password and submit button with remember me functionality",
    agent=qa_agent
)

# Step 3. Add them to the Crew
crew = Crew(
    agents=[qa_agent],
    tasks=[test_case_task],
    verbose=True
)

# Step 4. kickOff
if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
