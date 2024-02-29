import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys
apikey = os.getenv("OPENAI_API")
