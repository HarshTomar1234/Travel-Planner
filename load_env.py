from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Verify the API key is loaded
if not os.getenv("OPENAI_API_KEY"):
    print("WARNING: OPENAI_API_KEY not found in environment!")
else:
    print("✅ OPENAI_API_KEY loaded successfully") 