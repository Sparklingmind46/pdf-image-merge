import os
import telebot
from telebot import types
from PyPDF2 import PdfMerger
from PIL import Image
from io import BytesIO
import time 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, ReplyKeyboardMarkup, KeyboardButton

# Initialize bot with token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Temporary storage for user files (dictionary to store file paths by user)
user_files = {}
user_images = {}
user_message_ids = {}

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Send a sticker first
    sticker_id = 'CAACAgUAAxkBAAECEpdnLcqQbmvQfCMf5E3rBK2dkgzqiAACJBMAAts8yFf1hVr67KQJnh4E'
    sent_sticker = bot.send_sticker(message.chat.id, sticker_id)
    sticker_message_id = sent_sticker.message_id
    time.sleep(2)
    bot.delete_message(message.chat.id, sticker_message_id)
    
    # Define the inline keyboard with buttons
    markup = InlineKeyboardMarkup()
    # First row: Help and About buttons
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("«ʜᴇʟᴘ» 🕵️", callback_data="help"),
        InlineKeyboardButton("«ᴀʙᴏᴜᴛ» 📄", callback_data="about")
    )
    # Second row: Developer button
    markup.add(InlineKeyboardButton("•Dᴇᴠᴇʟᴏᴘᴇʀ• ☘", url="https://t.me/Ur_amit_01"))
    
    # Send the photo with the caption and inline keyboard
    image_url = 'https://graph.org/file/0f1d046b4b3899e1812bf-0e63e80abb1bef1a8b.jpg'
    bot.send_photo(
        message.chat.id, 
        image_url, 
        caption="Aʜ, ᴀ ɴᴇᴡ ᴛʀᴀᴠᴇʟᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ... Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴍᴀɢɪᴄᴀʟ ʀᴇᴀʟᴍ !🧞‍♂️✨\n\n• I ᴀᴍ PDF ɢᴇɴɪᴇ, ɪ ᴡɪʟʟ ɢʀᴀɴᴛ ʏᴏᴜʀ ᴘᴅғ ᴡɪsʜᴇs! 📑🪄",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data in ["help", "about", "back"])
def callback_handler(call):
    # Define media and caption based on the button clicked
    if call.data == "help":
        new_image_url = 'https://graph.org/file/0f1d046b4b3899e1812bf-0e63e80abb1bef1a8b.jpg'
        new_caption = "Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.:\n1. Send PDF files.\n2. Use /merge when you're ready to combine them.\n3. Max size = 20MB per file.\n\n• Note: My developer is constantly adding new features in my program , if you found any bug or error please report at @Ur_Amit_01"
        # Add a "Back" button
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Back", callback_data="back"))
    elif call.data == "about":
    # Get the bot's username dynamically
        new_image_url = 'https://graph.org/file/0f1d046b4b3899e1812bf-0e63e80abb1bef1a8b.jpg'
        new_caption = ABOUT_TXT
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Back", callback_data="back"))
    elif call.data == "back":
        # Go back to the start message
        new_image_url = 'https://graph.org/file/0f1d046b4b3899e1812bf-0e63e80abb1bef1a8b.jpg'
        new_caption = "Aʜ, ᴀ ɴᴇᴡ ᴛʀᴀᴠᴇʟᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ... Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴍᴀɢɪᴄᴀʟ ʀᴇᴀʟᴍ !🧞‍♂️✨\n\n• I ᴀᴍ PDF ɢᴇɴɪᴇ, ɪ ᴡɪʟʟ ɢʀᴀɴᴛ ʏᴏᴜʀ ᴘᴅғ ᴡɪsʜᴇs! 📑🪄"
        # Restore original keyboard with Help, About, and Developer buttons
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("Help 🕵️", callback_data="help"),
            InlineKeyboardButton("About 📄", callback_data="about")
        )
        markup.add(InlineKeyboardButton("Developer ☘", url="https://t.me/Ur_Amit_01"))
    
    # Create media object with the new image and caption
    media = InputMediaPhoto(media=new_image_url, caption=new_caption, parse_mode="HTML")
    
    # Edit the original message with the new image and caption
    bot.edit_message_media(
        media=media,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup  # Updated inline keyboard
    )

ABOUT_TXT = """<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/PDF_Genie_Robot'>PDF Genie</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Ur_amit_01'>ꫝᴍɪᴛ ꢺɪɴɢʜ ⚝</a> 
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

# Help command handler
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "1. Send me PDF files you want to merge.\n"
    help_text += "2. Use /merge to combine the files into one PDF.\n"
    help_text += "3. Use /clear to reset the list of files."
    bot.reply_to(message, help_text)

# Helper to update progress
def update_progress(chat_id, message_id, progress_text):
    bot.edit_message_text(
        text=progress_text,
        chat_id=chat_id,
        message_id=message_id
    )

# Merge command handler
@bot.message_handler(commands=['merge'])
def merge_pdfs(message):
    user_id = message.from_user.id
    
    # Check if there are files to merge
    if user_id not in user_files or len(user_files[user_id]) < 2:
        bot.reply_to(message, "You need to send at least two PDF files before merging.")
        return
    
    # Ask for the filename
    bot.reply_to(message, "Please provide a filename for the merged PDF (without the .pdf extension).")
    bot.register_next_step_handler(message, handle_filename_input)

# Handler for receiving the filename
def handle_filename_input(message):
    user_id = message.from_user.id
    filename = message.text.strip()
    
    if filename:
        # Ensure the filename ends with .pdf
        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"
        
        # Proceed to merge the PDFs with the given filename
        merge_pdfs_with_filename(user_id, message.chat.id, filename)
    else:
        bot.reply_to(message, "Please provide a valid filename.")
        bot.register_next_step_handler(message, handle_filename_input)

def merge_pdfs_with_filename(user_id, chat_id, filename):
    # Create a PdfMerger object
    merger = PdfMerger()
    progress_text = "Merging PDFs: 0%"

    # Send initial progress message
    progress_message = bot.send_message(chat_id, progress_text)

    try:
        # Append each PDF file for merging
        total_files = len(user_files[user_id])
        for i, pdf_file in enumerate(user_files[user_id]):
            merger.append(pdf_file)
            # Update progress (simple percentage)
            progress_text = f"Merging PDFs: {int((i+1) / total_files * 100)}%"
            update_progress(chat_id, progress_message.message_id, progress_text)
            time.sleep(1)  # Simulate time for merging each file

        # Output merged file with the user-provided filename
        with open(filename, "wb") as merged_file:
            merger.write(merged_file)
        
        # Simulate upload progress (not real-time, but you can show it)
        progress_text = "Uploading merged file..."
        update_progress(chat_id, progress_message.message_id, progress_text)

        # Send the merged PDF back to the user
        with open(filename, "rb") as merged_file:
            bot.send_document(chat_id, merged_file)
        
        # After sending the file, delete the progress message
        bot.delete_message(chat_id, progress_message.message_id)

        bot.send_message(chat_id, f"*Here is your merged PDF!📕😎*",parse_mode="Markdown")

    finally:
        # Clean up each user's files after merging
        for pdf_file in user_files[user_id]:
            os.remove(pdf_file)
        user_files[user_id] = []

         
# Handler for received documents (PDFs)
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB in bytes

@bot.message_handler(content_types=['document'])
def handle_document(message):
    # Check if the file is a PDF
    if message.document.mime_type == 'application/pdf':
        file_size = message.document.file_size
        
        # Check if the file exceeds the size limit
        if file_size > MAX_FILE_SIZE:
            bot.reply_to(message, "Sorry, the file is too large. Please upload a PDF smaller than 20 MB.")
            return
        
        # Ensure directory for each user
        user_id = message.from_user.id
        if user_id not in user_files:
            user_files[user_id] = []
        
        # Get the file info and download it in one go
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Save the file with a unique name
        file_name = f"{message.document.file_name}"
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        # Store file path in user's file list
        user_files[user_id].append(file_name)
        bot.reply_to(message, f"Added {file_name} to the list for merging.")
    else:
        bot.reply_to(message, "Please send only PDF files.")


# Clear command to reset files
@bot.message_handler(commands=['clear'])
def clear_files(message):
    user_id = message.from_user.id
    if user_id in user_files:
        for pdf_file in user_files[user_id]:
            os.remove(pdf_file)
        user_files[user_id] = []
    bot.reply_to(message, "Your file list has been cleared.")



@bot.message_handler(commands=['convert_images'])
def convert_images_to_pdf(message):
    user_id = message.from_user.id
    
    # Check if there are images to convert
    if user_id not in user_images or len(user_images[user_id]) == 0:
        bot.reply_to(message, "Please upload some images first to convert into a PDF.")
        return
    
    bot.reply_to(message, "Please provide a filename for the PDF (without .pdf extension).")
    bot.register_next_step_handler(message, handle_image_pdf_filename)

# Handle filename input for image PDF
def handle_image_pdf_filename(message):
    user_id = message.from_user.id
    filename = message.text.strip()
    
    if filename:
        # Ensure filename ends with .pdf
        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"
        
        # Convert images to PDF with the given filename
        convert_images_with_filename(user_id, message.chat.id, filename)
    else:
        bot.reply_to(message, "Please provide a valid filename.")
        bot.register_next_step_handler(message, handle_image_pdf_filename)

def convert_images_with_filename(user_id, chat_id, filename):
    try:
        # Use BytesIO to avoid saving the PDF file on disk
        pdf_buffer = BytesIO()

        # Sort images by message_id to maintain order and open images in RGB mode
        sorted_images = sorted(user_images[user_id], key=lambda x: x[0])
        image_list = [Image.open(img_data).convert("RGB") for _, img_data in sorted_images]
        
        # Save all images to a single PDF file in memory without resizing
        image_list[0].save(pdf_buffer, format="PDF", save_all=True, append_images=image_list[1:])
        pdf_buffer.seek(0)  # Reset buffer position to the beginning

        # Send the PDF file back to the user from memory
        bot.send_document(chat_id, pdf_buffer, visible_file_name=filename)
        bot.send_message(chat_id, "Here is your merged PDF, Master! 🧞‍♂️🪄")

        # After sending the PDF, delete the "please wait" message if it exists
        if user_id in user_message_ids:
            bot.delete_message(chat_id, user_message_ids[user_id])

    finally:
        # Clean up user images after conversion
        for _, img_data in user_images[user_id]:
            img_data.close()  # Close BytesIO streams
        user_images[user_id] = []

# Handle received images
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    user_id = message.from_user.id
    
    # Ensure directory for each user's images
    if user_id not in user_images:
        user_images[user_id] = []
    
    # Get file info and download the image
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    # Save the file as a BytesIO stream (in memory) with its message_id to preserve order
    image_stream = BytesIO(downloaded_file)
    user_images[user_id].append((message.message_id, image_stream))
    
    # Get the current count of images for the process
    image_count = len(user_images[user_id])

    # Prepare the buttons for merging and clearing
    markup = types.InlineKeyboardMarkup()
    merge_button = types.InlineKeyboardButton("Merge Images 📃", callback_data="merge_images")
    clear_button = types.InlineKeyboardButton("Clear Images 🗑️", callback_data="clear_images")
    markup.add(merge_button, clear_button)

    # Delete the previous update message, if any
    if user_id in user_message_ids:
        bot.delete_message(message.chat.id, user_message_ids[user_id])

    # Update the message with the current image count and button
    user_message = bot.send_message(message.chat.id, f"• Number of images {image_count} 🖼️\n\n• Send more or click Merge images📄", reply_markup=markup)
    user_message_ids[user_id] = user_message.message_id  # Store the message ID for future deletion

# Callback for Inline Buttons
@bot.callback_query_handler(func=lambda call: call.data == 'merge_images')
def merge_images_callback(call):
    user_id = call.from_user.id
    
    # Show a message saying we are processing the images
    bot.answer_callback_query(call.id, "Merging images...")
    bot.send_message(call.message.chat.id, "Your document is being created master, please wait a moment 🧞‍♂️✨")

    # Check if there are images to merge
    if user_id not in user_images or len(user_images[user_id]) == 0:
        bot.send_message(call.message.chat.id, "No images to merge.")
        return
    
    # Proceed to handle the merging
    bot.send_message(call.message.chat.id, "Please provide a filename for the PDF (without .pdf extension).")
    bot.register_next_step_handler(call.message, handle_image_pdf_filename)

@bot.callback_query_handler(func=lambda call: call.data == 'clear_images')
def clear_images_callback(call):
    user_id = call.from_user.id
    if user_id in user_images:
        for _, img_data in user_images[user_id]:
            img_data.close()  # Close each BytesIO stream
        user_images[user_id] = []
    bot.answer_callback_query(call.id, "Images cleared.")
    bot.send_message(call.message.chat.id, "Your image list has been cleared.")

# Run the bot
bot.polling()
