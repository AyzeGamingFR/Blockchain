import json

class Wallet:
    
    def create_wallet(self, password):
        self.password = ""
        self.private_keys = {}
        self.public_keys = {}
        self.private_keys = self.private_keys + () 

class Blockchain:
    
    def init(self):
        self.actual_transactions = {}
        self.blockchain = {}
        self.blockchainnumber = 0
        self.block = {}
        self.blocksnumber = 0
        self.nodes = set()
    
    def create_transaction(self, sender, receiver, coins, message):
        self.previoushash = self.previoushash
        self.sender = sender
        self.receiver = receiver
        self.coins = coins
        self.message = message
        self = self ^ privateKey + difficulty
        
    def create_block(self, previoushash, transactions, transactionsnumber, totalfees):
        self.prevhash = previoushash
        self.txs = transactions
        self.txsnumber = transactionsnumber
        self.fees = totalfees
    
blockchain = Blockchain
