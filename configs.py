# Don't Forget That I Made This! 
 # So Give Credits! 
  
  
import os 
  
class Config(object): 
         BOT_TOKEN = os.environ.get("BOT_TOKEN","6586439577:AAERjnKohzK6QBOs01WbVcSUjiY0sUwvsVk") 
         API_ID = int(os.environ.get("API_ID", "16621664")) 
         API_HASH = os.environ.get("API_HASH","8b283f2943729318995738b5963f0bcc") 
         STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed") 
         STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed") 
         LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001976098815")) 
         UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None) 
         DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads") 
         PRESET = os.environ.get("PRESET", "ultrafast") 
         OWNER_ID = int(os.environ.get("OWNER_ID", "6561715152")) 
         CAPTION = "By @Srikanth18" 
         BOT_USERNAME = os.environ.get("BOT_USERNAME", "VideoWatermarkme_Bot") 
         DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Shashanklsss:shashank.ls1324@cluster0.rpvm8q5.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp") 
         BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) 
         ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
         USAGE_WATERMARK_ADDER = """ 
 Hi, I am Video Watermark Adder Bot! 
  
 **How to Added Watermark to a Video?** 
 **Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video. 
  
 __Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/Dads_links_repo).__ 
  
 Desgined by @Dads_links 
 """ 
         PROGRESS = """<b>\n  
  ╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣  
  ┣⪼ 📊 Percentage: {0}%  
  ┣⪼ ✅ Dᴏɴᴇ : {1}  
  ┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s  
  ┣⪼ ⏰️ Eᴛᴀ: {4}  
  ╰━━━━━━━━━━━━━━━➣ </b>"""