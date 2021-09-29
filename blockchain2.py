import hashlib
import keyboard
import PySide6.QtCore
import random
import socket
import threading
import time

class Main :
    
    class mainDatas :
        
        blockchain = {"chainId": 0, "chainName": "", "chainBlocks": [[], [], [], [], []]}
        network = {"peers": [], "datas": []}
        nodeSettings = {"ligthningNetwork": 1, "messageResposter": 1, "blocksUnvalidated": 5}
        walletPrivateKeys = []
        walletPublicKeys = []
        
    class blockchain :
        
        def syncChain() :
            
    class wallet :
        
        keysCharacters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        def createPrivateKey() :
            
            key = ""
            for len(self.privatekey) < 64 :
                
                self.privatekey.append(0[keysCharacters[random.randint(0, 36)])
                
            else :
                
                return (key)
                
        def createPublicKey(privatekey) :
            
            key = ""
            key = chr(ord(privatekey) *(ord(Date.getYear()) +ord(Date.getMonth()) +ord(Date.getDay()) +ord(Date.getMinute()) +ord(Date.getSeconds())))
            return (key)
            
        def createWalletFile() :
            
            fileContent = "{'privkeys': '" +mainDatas.walletPrivateKeys +"', 'pubkeys': '" +mainDatas.walletPublicKeys +"'}"
