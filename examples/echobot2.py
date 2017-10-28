
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import CallbackQueryHandler, Updater, CommandHandler, MessageHandler, Filters
import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import subprocess
#admin = ['raldokusuma','adadeeeh','udinIMM','fathoniadi','syukronrm']

f = open("admin.txt", "r")
listAdmin = []
for line in f:
   listAdmin.append(line)
listAdmin = [w.replace("\n","") for w in listAdmin]

#print listAdmin
#Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def admin(bot,update):
    file = open('admin.txt','r')
    file2 = file.read()
    if update.message.chat.username in file2:
    	 filew = open("admin.txt","a")
    	 temp = update.message.text
    	 temp2 = temp.split(" ")
    	 newadmin = temp2[1]
    	 filew.write(newadmin+"\n")
    	 update.message.reply_text("username "+newadmin+" telah ditambahkan")
    else :
         update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')
    file.close()

def start(bot, update):
    update.message.reply_text('Hi!')

def help(bot, update):
    update.message.reply_text(
		'Selamat Datang di SmartHousseAJK\n\nPanduan Penggunaan :\n\n'
		'/bukagarasi \n   --> Membuka Garasi \n\n'
		'/tutupgarasi \n   --> Menutup Garasi\n\n'
		'/nyalakanlampugarasi \n   --> Menyalakan lampu Garasi\n\n'
		'/matikanlampugarasi \n   --> Mematikan Lampu Garasi\n\n'
		'/nyalakanlampurumah \n   --> Menyalakan Lampu Rumah\n\n'
		'/matikanlampurumah \n   --> Mematikan Lampu Rumah\n\n'
		'/nyalakanlampudepan \n   --> Menyalakan Lampu Depan\n\n'
		'/matikanlampudepan \n   --> Mematikan Lampu Depan\n\n'
		'/status \n   --> Melihat status\n\n'
		'/start \n   --> Mulai\n\n'
		'/help \n   --> Bantuan Pengguna\n\n'
		'/tambahadmin (username)\n   --> untuk menambah admin\n\n')


def buka(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
	f = open('garasi.log', 'r')
        g = f.read().split(" ")
	if "buka\n" in g:
           update.message.reply_text("Garasi sudah buka")
        else :
           os.system('python ./servobuka.py')
           update.message.reply_text("Membuka garasi")
    else :
        update.message.reply_text("Maaf "+update.message.chat.username+" bukan admin")


def tutup(bot, update):
     file = open("admin.txt","r")
     file2 = file.read()
     if update.message.chat.username in file2:
        f = open('garasi.log', 'r')
        g = f.read().split(" ")
        if "tutup\n" in g:
           update.message.reply_text("Garasi sudah tutup")
        else :
           os.system('python ./servotutup.py')
           update.message.reply_text("Menutup garasi")
     else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def nyala1(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        f = open('lampu1.log', 'r')
        g = f.read().split(" ")
        if "nyala\n" in g:
           update.message.reply_text("Lampu garasi sudah nyala")
        else :
           os.system('python ./lampu1nyala.py')
           update.message.reply_text("Menghidupkan lampu garasi ")
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def mati1(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        f = open('lampu1.log', 'r')
        g = f.read().split(" ")
        if "mati\n" in g:
           update.message.reply_text("Lampu garasi sudah mati")
        else :
           os.system('python ./lampu1mati.py')
           update.message.reply_text("Mematikan lampu garasi")
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def nyala2(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        f = open('lampu2.log', 'r')
        g = f.read().split(" ")
        if "nyala\n" in g:
           update.message.reply_text("Lampu rumah sudah nyala")
        else :
           os.system('python ./lampu2nyala.py')
           update.message.reply_text("Menghidupkan lampu rumah")
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def mati2(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        f = open('lampu2.log', 'r')
        g = f.read().split(" ")
        if "mati\n" in g:
           update.message.reply_text("Lampu rumah sudah mati")
        else :
           os.system('python ./lampu2mati.py')
           update.message.reply_text("Mematikan lampu rumah")
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def nyala3(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        f = open('lampu3.log', 'r')
        g = f.read().split(" ")
        if "nyala\n" in g:
           update.message.reply_text("Lampu depan sudah nyala")
        else :
           os.system('python ./lampu3nyala.py')
           update.message.reply_text("Menghidupkan lampu depan")
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def mati3(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        f = open('lampu3.log', 'r')
        g = f.read().split(" ")
        if "mati\n" in g:
           update.message.reply_text("Lampu depan sudah mati")
        else :
           os.system('python ./lampu3mati.py')
           update.message.reply_text("Mematikan lampu 3")
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')


def status(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username in file2:
        servo  = subprocess.check_output(['cat','./garasi.log'])
	lampu1 = subprocess.check_output(['cat','./lampu1.log'])
        lampu2 = subprocess.check_output(['cat','./lampu2.log'])
        lampu3 = subprocess.check_output(['cat','./lampu3.log'])

	update.message.reply_text(servo+"\n"+lampu1+"\n"+lampu2+"\n"+lampu3+"\n");
    else :
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def echo(bot, update):
    file = open("admin.txt","r")
    file2 = file.read()
    if update.message.chat.username not in file2:
        update.message.reply_text('Maaf '+update.message.chat.username+' bukan admin')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("458534210:AAHOeYPZamMU9bqH-MV36tOBnKj4FhWuvoo")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    #one = os.system('python ./servo.py')
    # on different commands - answer in Telegram
    #updater.message.reply_text('Selamat Datang di SmartHouseAJK\n\n/help\n   --> Melihat Panduan Penggunaan')
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bukagarasi", buka))
    dp.add_handler(CommandHandler("tutupgarasi", tutup))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("matikanlampu1", mati1)) #matikanlampugarasi
    dp.add_handler(CommandHandler("nyalakanlampu1", nyala1)) #nyalakanlampugarasi
    dp.add_handler(CommandHandler("matikanlampu2", mati2)) #matikanlampurumah
    dp.add_handler(CommandHandler("nyalakanlampu2", nyala2)) #nyalakanrampurumah
    dp.add_handler(CommandHandler("matikanlampu3", mati3)) #matikanlampudepan
    dp.add_handler(CommandHandler("nyalakanlampu3", nyala3)) #nyalakanlampudepan
    dp.add_handler(CommandHandler("tambahadmin", admin))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text , echo))

    #log all errors
    dp.add_error_handler(error)

    #Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
