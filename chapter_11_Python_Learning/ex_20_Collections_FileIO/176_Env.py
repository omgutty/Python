# 176_Env.py
# Topic: Environment variables with dotenv
#
# load_dotenv() reads a .env file into the environment, then
# os.getenv('KEY') reads the value. Secrets (passwords, API keys)
# live in .env - NOT in the code. Needs: pip install python-dotenv,
# and a .env file in the SAME folder you run from.
# (Remember: load_dotenv() uses the current working directory -
# pass the path explicitly if you run from elsewhere.)

from dotenv import load_dotenv
import os
load_dotenv() 

print(os.getenv('DB_PASSWORD'))

if os.getenv('DB_PASSWORD') == "superSecret123!":
    print("Welcome Admin")
else:
    print("Goodbye")