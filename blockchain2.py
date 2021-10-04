import hashlib
import keyboard
import PySide6.QtCore
import random
import socket
import string
import threading
import time

class Main :
    
    class mainDatas :
        
        blockchain = {"chainId": 0, "chainName": "", "chainBlocks": [], "chainDiff": 1}
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
                if datasDecrypted.startsWith("{ 'datasType': '") :
                    
                    return (datasDecrypted)
                    
                else :
                    
                    datasDecrypted = string.ascii_letters(string.digits(datas) -1)
                    
        class sha256 :
            
            def hash(datas) :
                
                hashlib.sha256(string.ascii_letters(string.ascii_digits(datas) +random.randint(mainDatas.blockchain["chainDiff"], random.randint(mainDatas.blockchain["chainDiff" +100])))).hexdigest()
                
            def bruteForce(hash) :
                
                strings = blockchain.stringsGenerator()
                hashedDatas = ""
                
                for hashedDatas is not hash :
                    
                    hashedDatas = hashlib.sha256(strings[0]).hexdigest()
                    strings.remove(0)
                    
                return (hashedDatas)
                
    class blockchain :
        
        constantsresult = string.ascii_letters(string.digits("ayzelyc") +string.digits("blockchain") +string.digits("bitcoin") +string.digits("ethereum") +string.digits("marscoin") +string.digits("mooncoin") +string.digits("nfc") +string.digits("token"))
        
        def syncChain() :
            
            
            
        def verifyChain() :
            
            
            
        def createTransaction(txnumber, prevhash, sender, receiver, coins, fees, message, privkey) :
            
            tx = "{'txnumber': " +txnumber +", 'prevhash': '" +prevhash +"', 'sender': '+"sender +"', 'receiver': '"+ +receiver +"', 'coins': " +coins ", 'fees': " +fees"}"
            tx = string.ascii_letters(string.digits(tx) *string.digits(privkey))
            return (tx)
            
        def verifyTransaction(datas) :
            
            tx = datas
            generatedStrings = stringsGenerator()
            i = 0
            for tx.startsWith("{ 'prevhash': '") :
                
                
                
            else :
                
                if i == 0 :
                    
                    tx /= generatedStrings[0]
                    generatedStrings.remove(0)
                    
                else :
                    
                    if len(generatedStrings) == 0 :
                        
                        i += 1
                        
                    else :
                        
                        i += 1
                        
        def createBlock(prevhash, number, transactions, fees, message, reward) :
            
            fees += reward
            datas = "{ 'prevhash': '" +prevhash +"', 'number': " +number +", 'transactions': [" +transactions +"], 'fees': " +fees +", 'message': '" +message +"' }"
            mainDatas.blockchain["chainBlocks"].append(verifyBlock(datas))
            internet.issocket.send("new block : " +mainDatas.blockchain["chainBlocks"[(len(mainDatas.blockchain["chainBlocks"]) -1)]])
            
        def verifyBlock(datas) :
            
            return (algorithms.leya.bruteForce(datas))
            
        def stringGenerator(numberOfStrings) :
            
            i = 0
            generated = []
            for i < numberOfStrings :
                
                generated.append("'" +string.ascii_letters(i) +"'")
                
            return (generated)
            
    class threading :
        
        
        
    class wallet :
        
        keysCharacters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        def createPrivateKey() :
            
            key = ""
            for len(self.privatekey) < 64 :
                
                self.privatekey.append(0[keysCharacters[random.randint(0, 36)])
                
            else :
                
                return (key)
                
        def createPublicKey(privatekey) :
            
            key = "A" +string.ascii_letters(string.digits(privatekey) *(string.digits(Date.getYear()) +string.digits(Date.getMonth()) +string.digits(Date.getDay()) +string.digits(Date.getMinute()) +string.digits(Date.getSeconds())))[0 : 62]
            return (key)
            
        def createWalletFile(password) :
            
            fileContent = "{'privkeys': '" +string.ascii_letters(string.digits(mainDatas.walletPrivateKeys) *string.digits(blockchain.constantsresult) *string.digits(password)) +"', 'pubkeys': '" +string.ascii_letters(string.digits(mainDatas.walletPublicKeys) *string.digits(blockchain.constantsresult) *string.digits(password)) +"'}"
