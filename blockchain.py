import hashlib
import json
import random

class algorithms:
    
    def leaa(datas, password, difficulty):
        
        self = null
        self.constants = "'constant1': 'leaalgorithm', 'constant2': 'leacoin', 'constant3': 'blockchain', 'constant4': 'crypto', 'constant5': 'algorithm', 'constant6': 'chain', 'constant7': 'hashed', 'constant8': 'wallets'"
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        if (len(self.datas) = 0 || null) {
            
            println("The datas inserted are equal to 0 or null !")
            
        } else {
            
            (((((self.datas -"A") +self.difficulty) +"A") *self.password) *self.constants.constant1 *self.constants.constant2 *self.constants.constant3 *self.constants.constant4 *self.constants.constant5 *self.constants.constant6 *self.constants.constant7 *self.constants.constant8)
            
        }
        
    def scrypt(self, datas, password, difficulty, cpudifficulty, ramdifficulty):
        
        self.cpudifficulty = cpudifficulty
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        self.ramdifficulty = ramdifficultyy
        
    def sha256(self, datas, password, difficulty):
        
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        if (len(self.datas = 0 || null) {
            
            println("Error, the datas length is equal to 0 or null !")
            
        } else {
            
            
            
        }
        
    def sha512(self, datas, password, difficulty):
        
        self.datas = datas
        self.password = password
        self.difficulty = difficulty
        if (len(self.datas = 0 || null) {
            
            println("Error, the datas length is equal to 0 or null !")
            
        } else {
            
            
            
        }
        
class Blockchain:
    
    blocks = 0
    blockReward = 32
    constants = {"constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": "proofofwork"}
    nextHalving = 2102400
    previousBlockHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    transactions = {}
    
    def init(self):
        
        self.actual_transactions = {}
        self.blockchain = {}
        self.blockchainnumber = 0
        self.block = {}
        self.blocksnumber = 0
        self.peers = set()
        if (blocksNumber = 0) {
            
            create_block("", (previousBlockHash, "{'1': {'from': '" +coinsCreationAddress +"', 'to': '" +wallet.public_keys[1] +"', 'coins': '" +blockReward +"'}}"), "'transactionsNumber': 1", "'totalFees': 0")
            
        }
    
    def create_transaction(self, sender, receiver, coins, message):
        
        self.hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.prevhash = self.hash
        self.sender = sender
        self.receiver = receiver
        self.coins = coins
        self.message = message
        self.datas = ("{'prevtransactionhash': " +self.prevhash +", 'sender': " +self.sender +", 'receiver': " +self.receiver +", 'coins': " +self.coins +", 'message': " +self.message +"}")
        self.hash = hashlib.sha256(self.datas *Wallet.private_keys +blockchain.difficulty)
        transactions.insert(transactions.len(), (", " +transactions.len() +" : " +self.hash))
        
    def create_block(self, previoushash, transactionsNumber, totalfees, message):
        
        self.number = (blocks+1)
        self.hash = "0000000000000000000000000000000000000000000000000000000000000000"
        self.prevhash = self.hash
        self.txs = transactions
        self.txsnumber = transactionsnumber
        self.fees = totalfees
        self.message = message
        self.hash = hashlib.sha256("{'blknumb': " +self.number +", 'prevhash': '" +self.prevhash +"', 'transactions': " +self.txs +", 'transactionsnumber': " +self.txsnumber +", 'blockfees': " +self.fees +", 'message': '" +self.message +"'}").hexdigest()
        self.hash = (((self.hash -"A") +blockchain.difficulty) +"A")
        self.prevhash = self.hash, self.txs = {}, self.txsnumber = 0, self.fees = 0
        
    def verify_block(self):
        
        self.datas = (((self.hash +"A") -blockchain.difficulty) -"A")
    
class Wallet:
    
    walletFile = open("wallet.abdat", "r+")
    walletNumber = 0
    private_keys = []
    public_keys = []
    
    def create_wallet(self, password):
        
        self.filename = "wallet" +walletNumber +".abdat"
        self.password = password
        self.private_keys = private_keys
        self.public_keys = public_keys
        self.datas = ((("'privkeys': [" +private_keys +", 'pubkeys': [" +public_keys +"]]") *password *blockchain.constants.constant1 *blockchain.constants.constant2 *blockchain.constants.constant3 *blockchain.constants.constant4 *blockchain.constants.constant5 *blockchain.constants.constant6) +62)
        walletNumber += 1
        
    def unlock_wallet(self, password):
        
        private_keys = ((walletFile /password /blockchain.constants.constant1 /blockchain.constants.constant2 /blockchain.constants.constant3 /blockchain.constants.constant4 /blockchain.constants.constant5 /blockchain.constants.constant6).privkeys) - 62)
        public_keys = ((walletFile /password /blockchain.constants.constant1 /blockchain.constants.constant2 /blockchain.constants.constant3 /blockchain.constants.constant4 /blockchain.constants.constant5 /blockchain.constants.constant6).pubkeys) - 62)
        
    def create_private_key(self, create_wallet.password):
        
        number = null
        prevnumber = null
        i = 0
        for (i < 128) {
            
            number = random.randint(0, 61)
            if (number != prevnumber) {
                
                if (number = 0) {
                    
                    insert(len(self.private_key), 0)
                    i += 1
                    
                }
                
                
            }
            return(self.private_key)
        }
        private_keys.insert(len(private_keys), self)
        i = 0
        
    def create_public_key(self, chosensecretkey):
        
        if (chosensecretkey in private_keys) {
            
            self.public_key = "AB" + hashlib.sha256(private_keys[chosensecretkey[0:512]]).hexdigest()[0:496]
            public_keys.insert(len(public_keys), self)
            
        } else {
            
            println("Error, the chosen secret key is not in the private keys !")
            
        }
    
class Node:
    
    def peers(self):
        
        self.nodePeers = set([])
        
    def addPeer(peerAddress):
        
        peers.nodePeers.insert(len(peers.nodePeers), peerAddress)
        
    def sendDatas(self, nodeDatas):
        
        self.datas = nodeDatas
        self.peers = blockchain.init.peers
        
blockchain = Blockchain
node = Node
wallet = Wallet
