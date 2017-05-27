import os
import getpass
import shutil

username = getpass.getuser()

def getapp():

    appurl=str(input("What is the URL to the app you want to download? ").lower())
    if not 'http://' in appurl:
        if not 'https://' in appurl:
            appurl="http://"+appurl
    appname=str(input("What do you want to name the app? "))
    
    apppath='/home/'+username+'/webapps/'+appname.lower()+'/'
    appsh='/home/'+username+'/webapps/'+appname+'.sh'
    appshort='/home/'+username+'/Desktop/'+appname+'.desktop'
    
    os.chdir('/home/'+username)
    os.system('nativefier '+appurl+' --name '+appname.lower())
    
    shutil.move('/home/'+username+'/'+appname.lower()+'-linux-x64', apppath)
    
    os.system("echo '#!/usr/bin/env bash'>"+appsh)
    os.system('echo "' +apppath+appname.lower()+'">>'+appsh)
    os.system('chmod +x '+appsh)
    
    
    os.system('echo "[Desktop Entry]">'+appshort)
    os.system('echo "Version=1.0">>'+appshort)
    os.system('echo "Type=Application">>'+appshort)
    os.system('echo "Exec='+appsh+'">>'+appshort)
    os.system('echo "Name='+appname+'">>'+appshort)
    os.system('echo "Icon='+apppath+'/resources/app/icon.png">>'+appshort)
    os.system('chmod +x '+appshort)
    
    
getapp()