import os

def install_deps():
    global service
    os.system("yes | sudo apt-get install lm-sensors")
    os.system("yes | sudo sensors-detect")
    os.system("sudo cp -r /home/hive-install-gpugod/modules /etc/")                               
if __name__ == '__main__':   
    install_deps()
