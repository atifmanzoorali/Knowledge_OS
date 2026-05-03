import os
from pathlib import Path
from dotenv import load_dotenv

SEARCH_DIR = Path(__file__).parent
ROOT_DIR = SEARCH_DIR.parent

env_path = ROOT_DIR / ".env"
load_dotenv(env_path, override=True)

API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_NAME = "deepseek-chat"
MAX_TOKENS = 1500
TEMPERATURE = 0.7
N_RESULTS = 5

CHROMA_DB_PATH = SEARCH_DIR / "knowledge_db"
MODEL_NAME_EMBED = "all-MiniLM-L6-v2"
KNOWLEDGE_OS_ROOT = ROOT_DIR