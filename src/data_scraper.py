from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import pandas as pd

# Your API credentials
api_id = "24031714"  # Replace with your API ID
api_hash = "56d77abec2efd7a4f9efe977c9aae914"  # Replace with your API Hash
phone_number = "+91 9880167017"  # Replace with your phone number

# Connect to Telegram
client = TelegramClient('my_telegram_session', api_id, api_hash)

async def scrape_messages():
    # Define the channel you want to scrape
    target_channel = 'Zero_to_hero_sr_stocks_nifty_507'

    messages = []
    async with client:
        # Scraping messages from the target channel
        async for message in client.iter_messages(target_channel, limit=500):  # Adjust limit as needed
            if message.text:  # Filter out non-text messages
                messages.append({"date": message.date, "text": message.text})
    return messages

client.start(phone=phone_number)
messages = client.loop.run_until_complete(scrape_messages())

# Save the messages to a DataFrame
df = pd.DataFrame(messages)

# Save the DataFrame to a CSV file
df.to_csv('data/raw_data.csv', index=False)

print("Data scraped and saved to 'raw_data.csv'!")

