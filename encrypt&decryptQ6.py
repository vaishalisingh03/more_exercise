def encrypt():
  message = input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt")
  ascii_message = [ord(char) for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = True
while flag == True:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice =='e':
        encrypt()
        play_again=input('do you want to try again:"Y/N')
        if play_again=="Y":
            continue
        else:
            break
    elif choice=='d':
        decrypt()
        play_again=input('do you want to play again:(Y/N)')
        if play_again=="Y":
            continue
        else:
            break
    else:
        break

    