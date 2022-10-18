#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import terminal command
import os

os.system("clear")	


#disclaimer
disclaimer = """
			USE AT YOUR
		         OWN RISK
	
	Make sure to run this script as superuser 
	"""

#manifest
manifest = """
		Android Toolkit for MacOS.
	 
			Code by Lorehaze (xda)
	
		It's a simple python script 
		to manipulate your Android.
	
	"""

#menu
menu = """
      #-------------------------------------------#	
      |		Base files			  |
      |						  |
      |	b1. Download ADB & Fastboot		  |
      |						  |
      |		ADB				  |
      |						  |
      |	a1. Start ADB server			  |
      |	a2. Stop ADB server			  |
      |	a3. Restart ADB server			  |
      |	a4. Check device via ADB		  |
      |	a5. Reboot device via ADB		  |
      |	a6. Reboot into Fastboot via ADB	  |
      |	a7. ADB Sideload			  |
      |	a8. Start ADB shell			  |
      |						  |
      |		Fastboot			  |
      | 					  |
      |	f1. Check device via fastboot		  |
      |	f2. Unlock bootloader			  |
      |	f3. Reboot to system via Fastboot	  |
      |	f4. Flash stock ROM			  |
      |	f5. Check Bootloader status 		  |
      |	f6. Flash custom recovery   		  |
      |	f7. Boot custom recovery 		  |
      |						  |
      |		Cleaner				  |
      | 					  |
      |	c1. Remve all the files used by this tool |
      °-------------------------------------------°      
	"""

print ( disclaimer )
print ( manifest)
print ( menu)

select = input(' Select an option [ex. b1]: ')

#b1. Download ADB & Fastboot
if select == "b1":
	playD = input('\nAre you sure you want to download ADB & fastboot?\n\nPress Enter key to continue, or Ctrl+C to stop the script')	
	os.system(" curl https://dl.google.com/android/repository/platform-tools-latest-darwin.zip -O -J -L && unzip -qq platform-tools-latest-darwin.zip && mv platform-tools tools && rm platform-tools-latest-darwin.zip && chmod 777 tools")
	print ('\n\nADB & Fastboot successfully downloaded on your system!')	

#a1. Start ADB server
if select == "a1":
	playAS = input('\nThis will start ADB server. Press Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./adb start-server")

#a2. Stop ADB server
if select == "a2":
	stopAS = input('\nThis will stop ADB server. Press Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./adb kill-server")

#a3. Restart ADB server
if select == "a3":
	restartAS = input('\nThis will restart ADB server. Press Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./adb kill-server && ./adb start-server")

#a4. Check device via ADB
if select == "a4":
	print('\nConnect your device via USB and enable ADB...')
	checkA = input('\nPress Enter to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./adb devices")

#a5. Reboot device via ADB
if select == "a5":
	print('\nConnect your device via USB and enable ADB...')
	reboot = input('\nPress Enter key to continue, or Ctrl+C to stop the script')
	os.system("cd tools && ./adb reboot")
	print('\nReboot successful!')

#a6. Reboot into fastboot via ADB
if select == "a6":
	print('\nConnect your device via USB and enable ADB...')
	rebootAF = input('\nPress Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./adb reboot")

#a7. ADB sideload
if select == "a7":
	print('\nConnect your device via USB and enable ADB...')
	print('\nI just create the sideload directory. \nPlease be sure to place the files you want to sideload into this directory before continuing.')
	sideload = input('\nPress Enter key to continue, or Ctrl+C to stop the script...')
	os.system("mkdir sideload && cp tools/* sideload/ && cd sideload && ./adb sideload *.zip")
	print('\nSuccessful!')

#a8. Start ADB shell
if select == "a8":
	print('\nConnect your device via USB and enable ADB...')
	shell = input('\nPress Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./adb shell")

#f1. Check device via Fastboot
if select == "f1":
	print('\nConnect your device via USB in Fastboot mode...')
	checkF = input('\nPress Enter to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./fastboot devices")

#f2. Unlock Bootloader
if select == "f2":
	print('\nConnect your device via USB in Fastboot mode...')
	print('\n\nUNLOCK YOUR BOOTLOADER MAY VOID YOUR WARRANTY!')
	confirm = input('\nPress Enter key to continue, or Ctrl+C to stop the script')
	os.system("cd tools && ./fastboot oem unlock")

#f3. Reboot to system via fastboot
if select == "f3":	
	print('\nConnect your device via USB in Fastboot mode...')
	freboot = input('\nPress Enter key to continue, or Ctrl+C to stop the script')
	os.system("cd tools && ./fastboot reboot")

#f4. Flash stock ROM
if select == "f4":
	os.system("mkdir os && cp tools/* os/")
	print('\nConnect your device via USB in Fastboot mode...')
	print('\n\nFLASHING PROCESS COULD BRICK YOUR DEVICE!')
	print('\n\nMake sure to copy all the stock rom files + the .sh file containing the flashing commands into the os folder.!')
	flashc = input('\nPress Enter to continue, or Ctrl+C to stop the script...')
	os.system("cd os && mv *.sh flasher.sh && chmod +x flasher.sh && sudo bash flasher.sh")

#f5. Check bootloader status
if select == "f5":
	print('\nConnect your device via USB in Fastboot mode...')
	checker = input('\nPress Enter to continue, or Ctrl+C to stop the script...')
	os.system("cd tools && ./fastboot oem device-info")

#c1. Clean all
if select == "c1":
	print('\nThis will remove all the files and directory used by this script...')
	question = input('\nPress Enter key to continue, or Ctrl+C to stop the script...')
	os.system("rm -rf tools os sideload recovery")
	print('\n\nClean success!\nFiles: ')
	os.system("ls")

#f6. Flash custom recovery
if select == "f6":
	print('\nThis will flash a custom recovery on your device. Any flashing process could cause a brick.')
	os.system("mkdir recovery && cp tools/* recovery/")
	print('\nBe sure to put your recovery.img into the recovery folder that was just created.\nMake sure that your .img is the only recovery file in the directory.')
	flashCR = input('\nPress Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cp -r tools/* recovery/ && cd recovery && ./fastboot flash *.img")

#f7. Boot custom recovery
if select == "f7":
	os.system("mkdir recovery")
	print('recovery folder just created!')
	print('\nBe sure to put your recovery.img into the recovery folder that was just created.\nMake sure that your .img is the only recovery file in the directory.')
	bootCR = input('\nPress Enter key to continue, or Ctrl+C to stop the script...')
	os.system("cp -r tools/* recovery/ && cd recovery && ./fastboot boot *.img")

