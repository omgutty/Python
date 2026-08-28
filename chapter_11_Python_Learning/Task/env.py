from dotenv import load_dotenv
import os
load_dotenv()

print(os.getenv('VWO_USERNAME'))

if os.getenv('VWO_USERNAME')=='om.gutty@gmail.com':
    print('Welcome')
else:
    print('goodbye')