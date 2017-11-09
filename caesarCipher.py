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