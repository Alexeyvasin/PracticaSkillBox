#TOKEN = '6578730555:AAGMDCL2tDtMuN50WGwpCeMBY3z1waiOj7U'
import os
from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()
BOT_TOKEN = os.getenv("6578730555:AAGMDCL2tDtMuN50WGwpCeMBY3z1waiOj7U")
API_KEY = os.getenv("API_KEY")