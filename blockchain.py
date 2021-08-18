import hashlib
import json
import random

class Wallet:
    
    private_keys = {}
    public_keys = {}
    def create_wallet(self, password):
        self.password = ""
        self.private_keys = private_keys
        self.public_keys = public_keys
        
    def unlock_wallet(self, password):
        
        
    def create_private_key(self, create_wallet.password):
        
        i = 0
        self.private_key = (for i < 127) {
            
            self.private_binary_key += random.randint(0, 1)
            i += 1
            
        })
        private_keys.insert(len(private_keys), self)
        
    def create_public_key(self, chosensecretkey):
        
        if (len(private_keys) < chosensecretkey) {
            
            println("Error, the chosen secret key is not in the private keys !")
            
        } else {
            
            self.public_key = "AB" + hashlib.sha256(private_keys[chosensecretkey[0:512]]).hexdigest()[0:496]
            public_keys.insert(len(public_keys), self)
            
        }

class Blockchain:
    
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
        self.hash = (self.hash + blockchain.difficulty) %36
        blockchain.insert(len(blockchain), self.hash)
        self.prevhash = self.hash, self.txs = {}, self.txsnumber = 0, self.fees = 0, self.hash = "0000000000000000000000000000000000000000000000000000000000000000"
    
blockchain = Blockchain
wallet = wallet
