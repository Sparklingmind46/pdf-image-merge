# bot/broadcast.py
from telebot import TeleBot
from pymongo import MongoClient
import time

# Initialize the bot
bot = TeleBot("YOUR_BOT_TOKEN")  # Replace with your bot token

# MongoDB setup
MONGO_URI = "mongodb+srv://uramit0001:EZ1u5bfKYZ52XeGT@cluster0.qnbzn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI
client = MongoClient(MONGO_URI)
db = client["bot_database"]
users_collection = db["users"]

# Add a new user if not already in the database
def add_user(user_id):
    if users_collection.find_one({"user_id": user_id}) is None:
        users_collection.insert_one({"user_id": user_id})

# Command to start the bot
@bot.message_handler(commands=["start"])
def start(message):
    add_user(message.from_user.id)

# Command to get user count
@bot.message_handler(commands=["usercount"])
def user_count(message):
    if message.from_user.id == 2031106491:  # Replace with admin's user ID
        count = users_collection.count_documents({})
        bot.reply_to(message, f"There are {count} users in the database.")

# Broadcast function
def broadcast_message(text):
    successful_count = 0
    failed_count = 0
    for user in users_collection.find():
        try:
            bot.send_message(user["user_id"], text)
            successful_count += 1
        except Exception as e:
            print(f"Error sending message to {user['user_id']}: {e}")
            failed_count += 1
    return successful_count, failed_count

# Command to broadcast a message (only for admins)
@bot.message_handler(commands=["broadcast"])
def broadcast(message):
    if message.from_user.id == 2031106491:  # Replace with admin's user ID
        try:
            text_to_broadcast = message.text.split(" ", 1)[1]
            successful_count, failed_count = broadcast_message(text_to_broadcast)
            bot.reply_to(
                message,
                f"Broadcast completed!\nSent to {successful_count} users.\nFailed for {failed_count} users."
            )
        except IndexError:
            bot.reply_to(message, "Please provide a message to broadcast.")

# Broadcast a message on bot startup
def on_bot_startup():
    # You can customize this message as per your need
    startup_message = "Bot has restarted! ⚡."
    successful_count, failed_count = broadcast_message(startup_message)
    print(f"Broadcast on startup completed! Sent to {successful_count} users. Failed for {failed_count} users.")

# Ensure the startup message is broadcasted
on_bot_startup()

# Run the bot
if __name__ == "__main__":
    bot.polling()
