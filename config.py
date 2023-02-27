import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18302370")

API_HASH = os.environ.get("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6103102860:AAGN0Gm7MWOvyDzKtgBHaBoTlk-ealdooFY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","My")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Mst:Mst@cluster0.g3uxpl0.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1957296068').split()]

PORT = os.environ.get('PORT', '8080')
