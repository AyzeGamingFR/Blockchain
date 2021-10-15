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
            
            def encrypt(self, datas, difficulty) :
                
                self.datas = datas
                self.diff = difficulty
                
                return (string.ascii_letters((string.digits(self.datas) +self.diff) *string.digits(blockchain.constantsresult)))
                
            def decrypt(self, datas, difficulty) :
                
                self.datas = datas
                self.diff = diff
                
                self.datasToReturn = string.ascii_letters((sring.digits(self.datas) +self.diff) *string.digits(blockchain.constantsresult))
                if datasToReturn.startsWith("{ 'datasType': '") :
                    
                    return (self.datasToReturn)
                    
                else :
                    
                    print("Datas were not able to be decrypted with this difficulty !")
                    
            def bruteForce(self, datas) :
                
                self.datas = datas
                self.datasDecrypted = ""
                
                self.datas = string.ascii_letters(string.digits(self.datas) /string.digits(blockchain.constantsresult))
                
                for self.datasDecrypted.startsWith("{ 'datasType': '") :
                    
                    return (self.datasDecrypted)
                    
                else :
                    
                    self.datasDecrypted = string.ascii_letters(string.digits(self.datas) -1)
                    
        class sha256 :
            
            def hash(self, datas) :
                
                self.hash = hashlib.sha256(self.datas).hexdigest()
                
            def bruteForce(self, hash) :
                
                self.hash = hash
                self.hashedDatas = ""
                self.strings = blockchain.stringsGenerator()
                
                for self.hashedDatas != self.hash :
                    
                    self.hashedDatas = hashlib.sha256(self.strings[0]).hexdigest()
                    self.strings.remove(0)
                    
                else :
                    
                    return (self.hashedDatas)
                
    class blockchain :
        
        constantsresult = string.ascii_letters(string.digits("ayzelyc") +string.digits("blockchain") +string.digits("bitcoin") +string.digits("ethereum") +string.digits("marscoin") +string.digits("mooncoin") +string.digits("nfc") +string.digits("token"))
        
        def syncChain(self) :
            
            self.chain = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
            self.chainsize = 0
            self.i = 0
            self.validchain = []
            
            for self.chainsize < self.peersChainSize
                
                internet.icsocket.send(internet.speers[0, 15], '{"datasType": "demand", "datas": "syncchain"}')
                for self.i < 16 :
                    
                    self.chain[(self.i)] = string.ascii_letters(string.digits(internet.icsocket.recv(internet.peers[(self.i)])) /string.digits(constantsresult))
                    
            else :
                
                self.validchain = verifyChain(self.chain)
                
        def sendChain(self, chain) :
            
            self.chain = chain
            
            internet.issocket.send(internet.cpeers[0, 15])
            
        def verifyChain(self, chains) :
            
            self.chains = chains
            
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
                        
        def createBlock(self, prevhash, number, transactions, fees, message, reward) :
            
            self.fees = fees +reward
            self.datas = "{ 'prevhash': '" +prevhash +"', 'number': " +number +", 'transactions': [" +transactions +"], 'fees': " +fees +", 'message': '" +message +"' }"
            mainDatas.blockchain["chainBlocks"].append(verifyBlock(datas))
            verifyBlock(mainDatas.blockchain["chainBlocks"[(len(mainDatas.blockchain["chainBlocks"] -1))]])
            internet.issocket.send("new block : " +mainDatas.blockchain["chainBlocks"[(len(mainDatas.blockchain["chainBlocks"]) -1)]])
            
        def verifyBlock(datas) :
            
            return (algorithms.leya.bruteForce(datas))
            
        def stringGenerator(self, numberOfStrings) :
            
            i = 0
            self.generated = []
            for i < numberOfStrings :
                
                self.generated.append("'" +string.ascii_letters(i) +"'")
                
            return (self)
            
    class gui :
        
        
        
    class threading :
        
        
        
    class wallet :
        
        keysCharacters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        def createPrivateKey(self) :
            
            self.key = ""
            for len(self) < 64 :
                
                self.key = self.key +keysCharacters[(random.randint(0, 62)]
                
            return (self)
                
        def createPublicKey(self, privatekey) :
            
            self.key = "A" +string.ascii_letters(string.digits(privatekey) *(string.digits(Date.getYear()) +string.digits(Date.getMonth()) +string.digits(Date.getDay()) +string.digits(Date.getMinute()) +string.digits(Date.getSeconds())))[1 : 64]
            return (self)
            
        def createWalletFile(self, password) :
            
            self.fileContent = "{'privkeys': '" +mainDatas.walletPrivateKeys +"', 'pubkeys': '" +mainDatas.walletPublicKeys +"'}"
            self.fileContent = string.ascii_letters(string.digits(self.fileContent) *string.digits(blockchain.constantsresult) *string.digits(password) +62)
            return (self)
            
        def unlockWalletFile(self, password) :
            
            self.fileContent = ""
            self.fileContent = string.ascii_letters(string.digits() /string.digits(blockchain.constantsresult) /string.digits(password) -62)
            return (self)
