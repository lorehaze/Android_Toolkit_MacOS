# Android_Toolkit_MacOS
A small python application to gain full control over your Android device. It will do his best on MacOS, but it also works on *unix systems.

HOW TO USE:

first, start a terminal and gain superuser powers by typing "sudo -s", then run the script with "./atkit.py" or "python atkit.py" or also "sudo python atkit.py".

Once the script starts, you can select an option among:

#-------------------------------------------#	
|		Base files			        |
|						        |
|	b1. Download ADB & Fastboot		  |
|						        |
|		ADB	                          |
|						        |
|	a1. Start ADB server	              |
|	a2. Stop ADB server                   |
|	a3. Restart ADB server	              |
|	a4. Check device via ADB              |
|	a5. Reboot device via ADB             |
|	a6. Reboot into Fastboot via ADB      |
|	a7. ADB Sideload	                    |
|	a8. Start ADB shell.                  |
|		                                |
|		Fastboot			        |
| 			                          |
|	f1. Check device via fastboot		  |
|	f2. Unlock bootloader	              |
|	f3. Reboot to system via Fastboot	  |
|	f4. Flash stock ROM	              |
|	f5. Check Bootloader status           |
|	f6. Flash custom recovery             |
|	f7. Boot custom recovery              |
|		                                |
|		Cleaner				  |
| 					              |
| c1. Remve all the files used by this tool |
°-------------------------------------------°
      
      
Since this tool is designed to be used from any workstation, please make sure the first option you select is 
"a1", because the script will create a directory called "tools" in wich will be stored the newest and always updated version of adb and fastboot for *unix systems.



HOW TO USE THE "f4. Flash stock rom":
To use this, you will need a .sh script containing all the commands your device need to be flashed. In this repository,
I created a directory named "Scripts" in wich I commited OnePlus_One_64GB.sh, but i will release any other scripts requested.

To flash, simply download the script (or you can just write your own) and place in the "os" directory wich will be created when you select "f4" option. Make sure the .sh file and all the stock rom files are in the "os" directory.



NOTES:
I'll add more options and commands, also i'll scripts flashers for many other Android device. Feel free to contact me for any question/request.
