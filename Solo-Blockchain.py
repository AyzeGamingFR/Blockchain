import hashlib
import random
import string

class Main :
    
    def blockchain() :
        
        chain = {"prevblkhash": "0000000000000000000000000000000000000000000000000000000000000000", "prevtxhash": "0000000000000000000000000000000000000000000000000000000000000000", "reward": 100, "blockchain": []}
        constantsresult = (string.digits("ayzelyc") +string.digits("blockchain") +string.digits("bitcoin") +string.digits("ethereum") +string.digits("marscoin") +string.digits("mooncoin") +string.digits("token") +string.digits("nfc"))
        wallet = {"keys": {}}
        
    def create_block(self, prevblkhash, transactions, blkmessage, blkfees, reward) :
        
        self.prevblkhash = prevblkhash
        self.blktxs = transactions
        self.blkmessage = blkmessage
        self.blkfees = fees
        
    def create_key() :
        
        self.key = random.randint(0, 2304)
        self.key = string.ascii_letters(self.key +blockchain.constantsresult)
        blockchain.wallet["keys"].append(self)
        
    def create_transaction(prevtxhash, txsender, txreceiver, txcoins, txmessage, txfees, key) :
        
        self.prevtxhash = prevtxhash
        self.txsender = txsender
        self.txreceiver = txreceiver
        self.txcoins = txcoins
        self.txmessage = txmessage
        self.txfees = txfees
        self.key = key
        
        self.txdatas = "{ 'prevtxhash': '" +self.prevtxhash +"', 'txsendr': '" +self.txsender +"', 'txrecvr': '" +self.txreceiver +"', 'txcoins': " +self.txcoins +", 'txfees': " +self.txfees +", 'txmsg': '" +self.txmessage +"' }"
        self.txdatas = string.ascii_letters(string.digits(self.txdatas) *string.digits(self.key))
        self.txdatas = hashlib.sha256(self.txdatas).hexdigest()
        blockchain.chain["blockchain"].append(self.txdatas)
        
    def create_wallet(self, password) :
        
        self.constresult = blockchain.constantsresult
        self.password = password
        self.keys = blockchain.wallet["keys"]
        
        self.keys = string.ascii_letters(string.digits(self.keys) *string.digits(self.password) *string.digits(self.constresult))
        return (self.keys)
