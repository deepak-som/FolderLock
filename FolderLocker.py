import base64
import os
import time
import sys


pw = "password".encode()      	 #default password is password feel free to change it here.
encode = base64.b64encode(pw)

locker_path = r" "  		 #Provide the path where you want to have a locker.



def goto(linenum):
    global line
    line = linenum


line = 1

while True:
    pw = str(input("Enter password:--> ")).encode()
    if pw == base64.b64decode(encode):
        os.chdir(locker_path)

        if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locker")

            else:
                os.popen(
                    'attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename(
                    "Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                sys.exit()

        else:
            os.rename(
                "Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen(
                'attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            sys.exit()

    else:
        print("Sorry! its Wrong one")
        time.sleep(5)
        goto(1)
