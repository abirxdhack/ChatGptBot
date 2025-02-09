import aiohttp
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from config import API_TOKEN, GPT_API_KEY, API_ID, API_HASH

async def fetch_gpt_response(prompt, model):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GPT_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
            "n": 1,
            "stop": None,
            "temperature": 0.5
        }
        
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                json_response = await response.json()
                return json_response['choices'][0]['message']['content']
            else:
                error_message = await response.text()
                print(f"Error {response.status}: {error_message}")
                return None

def setup_gpt_handlers(app: Client):
    @app.on_message(filters.command(["gpt4"], prefixes=["/", "."]) & (filters.private | filters.group))
    async def gpt4_handler(client, message):
        await message.reply_text("**GPT-4 Gate Off 🔕**", parse_mode=ParseMode.MARKDOWN)

    @app.on_message(filters.command(["gpt"], prefixes=["/", "."]) & (filters.private | filters.group))
    async def gpt_handler(client, message):
        try:
            # Check if a prompt is provided
            if len(message.command) <= 1:
                await message.reply_text("**❌Please provide a prompt for GPT response**", parse_mode=ParseMode.MARKDOWN)
                return

            prompt = " ".join(message.command[1:])
            # Send a temporary message indicating the bot is generating a response
            loading_message = await message.reply_text("**⚡️Generating GPT Response Please Wait....⌛️**", parse_mode=ParseMode.MARKDOWN)
            # Fetch response from the API
            response_text = await fetch_gpt_response(prompt, "gpt-4o-mini")
            
            # Delete the loading message
            await loading_message.delete()
            
            if response_text:
                # Send the response text to the user
                await message.reply_text(response_text, parse_mode=ParseMode.MARKDOWN)
            else:
                await message.reply_text("**Error Generating Response...**", parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            print(f"Exception: {e}")
            await message.reply_text("**Error Generating Response...**", parse_mode=ParseMode.MARKDOWN)

app = Client("gpt_bot", api_id=API_ID, api_hash=API_HASH, bot_token=API_TOKEN)
setup_gpt_handlers(app)

if __name__ == "__main__":
    app.run()