import hashlib
import json
import random

class Wallet:
    
    walletFile = open("wallet.abdat", "r+")
    private_keys = {}
    public_keys = {}
    
    def create_wallet(self, password):
        
        self.password = ""
        self.private_keys = private_keys
        self.public_keys = public_keys
        
    def lock_wallet(self, password):
        
        walletFile = (((json.stringify('privkeys: ' +private_keys +", 'pubkeys': " + public_keys) *password *blockchain.constants.constant1 *blockchain.constants.constant2 *blockchain.constants.constant3 *blockchain.constants.constant4 *blockchain.constants.constant5 *blockchain.constants.constant6) + 52)
        
    def unlock_wallet(self, password):
        
        private_keys = ((walletFile /password /blockchain.constants.constant1 /blockchain.constants.constant2 /blockchain.constants.constant3 /blockchain.constants.constant4 /blockchain.constants.constant5 /blockchain.constants.constant6).privkeys) - 62)
        public_keys = ((walletFile /password /blockchain.constants.constant1 /blockchain.constants.constant2 /blockchain.constants.constant3 /blockchain.constants.constant4 /blockchain.constants.constant5 /blockchain.constants.constant6).pubkeys) - 62)
        
    def create_private_key(self, create_wallet.password):
        
        number = null
        prevnumber = null
        i = 0
        for (i < 128) {
            
            random.randint(0, 61)
            if (number != prevnumber) {
                
                self.private_key += key
                i += 1
                
            }
            
        }
        private_keys.insert(len(private_keys), self)
        i = 0
        
    def create_public_key(self, chosensecretkey):
        
        if (len(private_keys) < chosensecretkey) {
            
            println("Error, the chosen secret key is not in the private keys !")
            
        } else {
            
            self.public_key = "AB" + hashlib.sha256(private_keys[chosensecretkey[0:512]]).hexdigest()[0:496]
            public_keys.insert(len(public_keys), self)
            
        }

class Blockchain:
    
    constants = {"constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": ""}
    
    def init(self):
        
        self.actual_transactions = {}
        self.blockchain = {}
        self.blockchainnumber = 0
        self.block = {}
        self.blocksnumber = 0
        self.nodes = set()
    
    def create_transaction(self, sender, receiver, coins, message):
        
        self.hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.prevhash = self.hash
        self.sender = sender
        self.receiver = receiver
        self.coins = coins
        self.message = message
        self.datas = (self.prevhash + self.sender + self.receiver + self.coins + self.message)
        self.hash = (self.datas ^ Wallet.private_keys + blockchain.difficulty) %36
        
    def create_block(self, previoushash, transactions, transactionsnumber, totalfees):
        
        self.hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.prevhash = self.hash
        self.txs = transactions
        self.txsnumber = transactionsnumber
        self.fees = totalfees
        self.hash = hashlib.sha256(self.prevhash, self.txs, self.txsnumber, self.fees).hexdigest()
        self.hash = (((self.hash -"A") + blockchain.difficulty) +"A") %36
        blockchain.insert(len(blockchain), self.hash)
        self.prevhash = self.hash, self.txs = {}, self.txsnumber = 0, self.fees = 0
        
    def verify_block(self):
        
        self.hash = ((())) 
    
class node:
    
    def addPeer(self):
        
        
        
blockchain = Blockchain
wallet = wallet
