# Caesar Cypher, make use of string method find()
# include uppercase and lower case symbols
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'decrypt', 'e', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "decrypt" or \'e or \'d')

def getMsg():
    print('Enter your message:')
    input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s' % (MAX_KEY_SIZE))
        key = int(input())
        if(key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key #for decrypting, we shift to the left
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol) #returns -1 if symbol not found
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            # add the symbol without any change
            translated += symbol
        else:
            # Encrypt or decrypt