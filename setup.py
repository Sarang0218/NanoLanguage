from tqdm import tqdm
from time import sleep
import basic
import os

def y_for_ui():
    for i in tqdm(range(0, 1000), desc ="Loading Modules... (1/3)"):
        sleep(0.01)

    ui = input("Would you like to install UI functions? (about 1 KB) (Y/N)")


    for i in tqdm(range(0, 50), desc ="Loading Modules.... (2/3)"):
        sleep(0.04)

    for i in tqdm(range(0, 1), desc ="Loading Modules... (3/3)"):
        if ui == "Y":
            with open("setup_cache_with_ui.py") as bear:
                content = bear.read()
            with open("basic.py", "a") as file:
                file.write(content)
            sleep(2)

        elif ui == "N" :
            with open("setup_cache.py") as bear:
                content = bear.read()
            with open("basic.py", "a") as file:
                file.write(content)
            sleep(2)

        else:
            with open("setup_cache_with_ui.py") as bear:
                content = bear.read()
            with open("basic.py", "a") as file:
                file.write(content)







    y_for_text_editor()

    if os.path.exists("setup_cache_with_ui.py"):
        os.remove("setup_cache_with_ui.py")
    else:
        print("The file does not exist")

    if os.path.exists("setup_cache.py"):
        os.remove("setup_cache.py")
    else:
        print("The file does not exist")

    if os.path.exists("setup_cache_with_text_editor.py"):
        os.remove("setup_cache_with_text_editor.py")
    else:
        print("The file does not exist")

    


    for i in tqdm(range(0, 900), desc ="Final Tasks"):
        sleep(0.01)



    print("Set-up complete. Use basic.py")




def y_for_text_editor():
    textEditor = input("Would you like a simple text editor? 1 KB")
    if textEditor == "Y":

        with open("setup_cache_with_text_editor.py") as bear:
            content = bear.read()
        with open("run.py", "a") as file:
            file.write(content)


    elif textEditor == "N" :
        print("Set-up done!")

    else:
        print("Set-up done!")

for i in tqdm(range(0, 100), desc ="Setting Up..."):
    sleep(0.1)

setup = input("Would you like to install basic modules? This will take about 57 KB. (Y/N) ")



if setup == "Y" :
    y_for_ui()

if setup == "N" :
    print("No module installed. basic.py is empty.")
    sleep(0.8)
    print("Error: No module installed: Can't run basic.py . Uninstall and retry.")

if setup == "y" :
    y_for_ui()

if setup == "n" :
    print("No module installed. basic.py is empty.")
    sleep(0.8)
    print("Error: No module installed: Can't run basic.py . Uninstall and retry.")

if setup == "yes" :
    y_for_ui()


    print("Set-up complete. Use basic.py")

if setup == "no" :
    print("No module installed. basic.py is empty.")
    sleep(0.8)
    print("Error: No module installed: Can't run basic.py . Uninstall and retry.")


if setup == "Yes" :
    y_for_ui()

if setup == "No" :
    print("No module installed. basic.py is empty.")
    sleep(0.8)
    print("Error: No module installed: Can't run basic.py . Uninstall and retry.")
