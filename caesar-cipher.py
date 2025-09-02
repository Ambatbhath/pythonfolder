
#take 3 arguments: the message, the cipher key and the alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet=alphabet+alphabet
    return doubleAlphabet
    
def getMessage():
    stringToEncrypt=input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage=""
    uppercaseMessage=""
    uppercaseMessage=message.upper()
    print(f'alphabet is: {alphabet}')
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        print(f'current character is: {currentCharacter}')
        print(f'current character position is: {position}')
        newPosition = position + int(cipherKey)
        print(f'New Encrypted Position of the character is: {newPosition}')
        print(f'Encrypted character is: {alphabet[newPosition]}')
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
            print(f'Encrypted Message: {encryptedMessage}')
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    print(f'Decrypted cipherKey: {decryptKey}')
    return encryptMessage(message,decryptKey,alphabet)
    
"""def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage=decryptMessage(myEncryptedMessage,myCipherKey,myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')"""
    
#runCaesarCipherProgram()
message = getMessage()
print(message)
doubleAl = getDoubleAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(doubleAl)
cipherKey = getCipherKey()
print(message)
encryptedMessage=encryptMessage(message,cipherKey,doubleAl)
print(f'Final Encrypted Message is: {encryptedMessage}')
decryptedMessage=decryptMessage(encryptedMessage,cipherKey,doubleAl)
print(f'Final Decrypted Message is: {decryptedMessage}')
