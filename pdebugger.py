


import argparse
import requests
import zipfile
import os
import config
import shutil
import subprocess
parser = argparse.ArgumentParser(description='PaxoDebugger')

parser.add_argument('--run', metavar='path_app', type=str, help='App to copy to emulator')

args = parser.parse_args()


import shutil

def launchemu(apppath): # << Merci GPT pour m'avoir aider sur la copie des fichiers !
    if os.path.exists("emulator/storage/apps/lua/debugapp") :
        os.removedirs("emulator/storage/apps/lua/debugapp")
    destination_folder = "storage/apps/lua/"
    print("[+] Copying app path folder")
    destination_folder = f"{destination_folder}/debugapp"
    try:

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

    
        for item in os.listdir(apppath):
            s = os.path.join(apppath, item)
            d = os.path.join(destination_folder, item)


            if os.path.isfile(s):
                shutil.copy2(s, d)

        print("[+] Done copying")
        print("[+] Launching emulator !")
        subprocess.run("emulator/PaxOS8.exe")
    except Exception as e:
        print(f"[-] Error copying app path folder: {e}")



if args.run:
    if os.path.exists("emulator"):
        print("[+] Launching")
        launchemu(args.run)
    else:
        print(args.run)
        response = requests.get(config.WINDOWS_EMULATOR_ZIP)
        if response.status_code == 200:
            print("[+] Downloading emulator...")
            with open("emulator.zip", 'wb') as f:
                f.write(response.content)

            with zipfile.ZipFile("emulator.zip", 'r') as zip_ref:
                zip_ref.extractall("emulator")
      

            print("[+] Done")
    if os.path.exists("storage"):
        print("[+]")
    else:
        print("[+] Downloading emulator storage...")
        print(args.run)
        response = requests.get(config.STORAGE_ZIP)
        if response.status_code == 200:
            print("[+] Downloading ...")
            with open("storage.zip", 'wb') as f:
                f.write(response.content)

            with zipfile.ZipFile("storage.zip", 'r') as zip_ref:
                zip_ref.extractall("storage")

            print("[+] Done")
            launchemu(args.run)
        else:
            print("[+] Error in downloading zip...")
else:
    print("[+]")
