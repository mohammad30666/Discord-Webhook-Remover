b = """                       ___________________________________ 
                      | created by:                       |
                      |    mohammad30666#0719             |
                      |                                   |
                      |                                   |
                      |   my github:                      |
                      | https://github.com/mohammad30666  |
                      |___________________________________|"""
import os
import requests
import time

def clear_console():
    if os.name in ('nt', 'dos'):
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass


def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "Webhook Remover | By mohammad30666"')
        except:
            pass
    else:
            pass


clear_console()
change_title()



def webhooksremover():
    try:
        print (b)
        print("Enter the WebHook you want to delete ")
        webhook = input("WebHook Link: ")
        requests.delete(webhook.rstrip())
        print("Webhook has been deleted")
    except:
        print("Webhook could not be deleted")

          
webhooksremover()

print ("Thanks for using my tool\nDogecoin: 0xc9E9Aa7FF6CAf6eEa784a686e4890cc6D61dd289\nBitcoin: 1DkEjNHhZmiyaaoQP9cxozpS5JwKdPyM4N\nTron: TZ7Dj2ZWaDrDHGTpG1oQvrWBuA5GJFAKMx")
time.sleep (14)
