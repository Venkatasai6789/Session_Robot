import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "24330005").strip()
API_HASH = os.getenv("API_HASH", "f7b37cb26bd04ab9e43f57ac269288e3").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5879426315:AAG9YWXb_3vLNmJQHZWok5cHpr4vULLzmJU").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Sessionbot:session9999@sessionbot.yz6kvyv.mongodb.net/?retryWrites=true&w=majority").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
