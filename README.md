#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )

Are you mad that your discord account is always getting fucked after 1 week of using Pysilon ?
If that's the case, you're on the right place.
Every file have been changed in order to be very discrete while using pysilon.
Please note that command have also changed.

Advanced Modded RAT malware written in Python, fully controllable through Discord with dedicated GUI builder to make preparation easier.

.s - take screenshot at any time
.scrnrc - record the screen for 15 seconds
.crtclb - elevates the process to critical status (.critical-disable to undo)
.dspl-grphc - manipulate low-level graphics by displaying pixels prepared in DrawlingStudio
.dspla-gltch <name> - display specified screen glitch
.mntrsff - turn off all monitors (.monitors-on to turn back on)
.wbsteblck <website> - block specified website from being accessed from any browser (.website-unblock <website> to unblock it)
.shw <what-to-show> - get list of running processes or available commands
.kll <process-name-or-id> - kill any running process
.blcklst <process-name> - adds specified process to the blacklist (victim won't be able to run it)
.witellt <process-name> - removes specified process from the blacklist (victim will be able to run it)
.frgrnd - get active window process name
.msg title="<title>" text="<text>" style=<style> - send a message to victim and get the response
.tts <message> - plays a Text-to-Speech message on victim's PC
.wbcm <action> - use connected webcam (currently supports photos shooting)
.blck-nput - block the mouse and keyboard(.unblock-input to unblock it)
.grb <what-to-grb> - grb for example saved passwords in web browsers ( tkn , pswrds , cokies )
.vlme <value> - change the audio output volume on victim's PC
.ply [<file>] - play any .mp3 file on the victim's PC (existing one or sent in the next message if no filename was provided)
.join - join voice-channel and stream live microphone input
.pwd - show working directory
.ls - list content of working directory
.tree - show tree of working directory
.cd <directory> - change working directory
.upld <type> [<name>] - upload any file or zipped directory (also greater than 8MB ones) onto target PC
.downld <file-or-directory> - download any file or zipped directory (also greater than 8MB ones) from target PC
.rmv <file-or-directory> - remove file or directory on target PC
.xcte <file> - run any file on target PC
.strt-clpper - start crypto-clipper (swap crypto currency wallet addresses to your ones)(.stop-clipper to stop it)
.jmpscr [<preset>] - play very loud and rapidly flashing video or other graphics
.bsd - trigger Blue Screen of Death
.frkbmb - execute fork bomb
.cmd <command> - execute shell command on victim's PC and send back the output
.implde - remove PySilon from target PC and clean the "evidence"
.clr - clear messages from file-related channel



List of features that should appear in following releases:

 webhook connection in case of unexpected circumstances (like BOT-Token banned by Discord)
 overall system info grabber with cool Discord Embeds
 traditional reverse shell creator
 grab credit cards information
 optional crypto mining (for example, when victim is idle)
 grab sessions from popular applications (Steam/Minecraft/Metamask/Exodus/Roblox)
