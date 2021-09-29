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
        
        
    class algorithms :
        
        class leya :
            
            def encrypt(datas, difficulty) :
                
                return (chr((ord(datas) +difficulty) *ord(constantsresult)))
                
            def decrypt(datas, difficulty) :
                
                datasToReturn = chr((ord(datas) +difficulty) *ord(constantsresult))
                if datasToReturn.startsWith("{ 'datasType': '") :
                    
                    return (datasToReturn)
                    
                else :
                    
                    print("Datas were not able to be decrypted with this difficulty, starting a bruteforce against the datas !")
                    return (bruteForce(datas))
                    
            def bruteForce(datas) :
                
                datasDecrypted = ""
                difficulty = 1
                if datasDecrypted.startsWith("{ 'datasType': '") :
                    
                    return (datasDecrypted)
                    
                else :
                    
                    datasDecrypted = chr((ord(datas) -difficulty) /ord(constantsresult))
                    difficulty += 1
                    
    class blockchain :
        
        def syncChain() :
            
            
            
        def verifyChain() :
            
            
            
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
