import hashlib
import random
import socket
import time

class Algorithms :
    
    def caesar() :
        
        def encrypt(datas, difficulty) :
            
            encrypted_datas = ""
            if len(datas) == 0 :
                
                print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be encrypted !")
                
            else :
                
                enrypted_datas = ""
                for char in datas :
                    
                    encrypted_datas += chr(ord(char) +difficulty)
                    
                return ("{'datas': '" +encrypted_datas +"'}")
                
        def decrypt(datas, difficulty) :
            
            decrypted_datas = ""
            if len(datas) == 0 :
                
                print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be decrypted !")
                
            else :
                
                encrypted_datas = ""
                for char in datas :
                    
                    encrypted_datas += chr(ord(chr) -difficulty)
                    
                return ("{'datas': '" +encrypted_datas +"'}")
                    
    def leya() :
        
        self.constants = "'constant1': 'leaalgorithm', 'constant2': 'leacoin', 'constant3': 'blockchain', 'constant4': 'crypto', 'constant5': 'algorithm', 'constant6': 'chain', 'constant7': 'hashed', 'constant8': 'wallets'"
        constantsresult = (self.constants["constant1"] *self.constants["constant2"] *self.constants["constant3"] *self.constants[] *self.constants[] *self.constants[] *self.constants[] *self.constants[])
        
        def encrypt(datas, password, difficulty, ramPrice) :
            
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                if len(password) == 0 :
                    
                    if difficulty <= 0 :
                        
                        return ("'datas': '" +chr(ord(datas) *constantsresult) +"'")
                        
                    else :
                        
                        return ("{'datas': '" +chr((ord(datas) +difficulty) *ord(password) *ord(constantsresult)) +"'}")
                        
                else :
                    
                    return ("{'datas': '" +(chr((ord(datas) +difficulty) *ord(password) *ord(constantsresult)) +"'}")
                    
        def decrypt(datas, password, difficulty) :
            
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                constantsresult = (self.constants["constant1"] *self.constants["constant2"] *self.constants["constant3"] *self constants["constant4"] *self constants["constant5"] *self.constants["constant6"] *self.constants["constant7"] *self.constants["constant8"])
                if len(password) == 0 :
                    
                    return ("{'datas': '" +chr(ord(datas) -difficulty) /constantsresult +"'}")
                    
                elif password == "unknown" :
                    
                    bruteForce(datas, difficulty)
                    
                elif len(password) > 0 AND password != "unknown" :
                    
                    return ("{'datas': '" +chr(ord(datas) -difficulty) /constantsresult +"'}")
                    
        def bruteForce(datas, difficulty) :
            
            constantsresult = ()
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                i = 0
                if !datas.startWith("{'datas':") :
                    
                    datas2 = ((datas -chr(i)) /constantsresult)
                    i += 1
                    datas2 = ((datas *constantsresult) +chr(i))
                    
                else :
                    
                    return ("{'datas': '" +datas +"'}")
                    
    def scrypt(datas, password, difficulty, cpudifficulty, ramdifficulty) :
        
        self.cpudifficulty = cpudifficulty
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        self.ramdifficulty = ramdifficulty
        if len(datas) == 0 :
            
            print ("The bits size of the datas is equal to 0 !")
            
        else :
            
            hashlib.scrypt(datas, password, ramdifficulty)
            
    def sha256(datas, password, difficulty) :
        
        if len(datas) == 0 :
            
            println("Error, the datas length is equal to 0 or null !")
            
        else :
            
            if password == 0 or null :
                
                if difficulty <= 0 :
                    
                    return (hashlib.sha256(datas))
                
                else :
                    
                    return (hashlib.sha256(caesar.encrypt(datas, difficulty)))
                    
            else :
                
                if difficulty <= 0 :
                    
                    datas *= password
                    return (hashlib.sha256(datas))
                    
                else :
                    
                    datas *= password
                    return (hashlib.sha256(caesar.encrypt(datas, difficulty )))
                    
    def sha512(datas, password, difficulty) :
        
        if len(datas == 0) :
            
            print("Error, the datas length is equal to 0 or null !")
            
        else:
            
            if password == 0 or null :
                
                if difficulty == 0 or < 0 :
                    
                    return (hashlib.sha512(datas))
                    
                else :
                    
                    return (hashlib.sha512(caesar.encrypt(datas, difficulty)))
                    
            else :
                
                if difficulty == 0 or < 0 :
                    
                    datas *= password
                    return (hashlib.sha512(datas))
                    
                else :
                    
                    datas *= password
                    return (hashlib.sha512(caesar.encrypt(datas, difficulty)))
                    
class Blockchain :
    
    blockChain = {}
    blockReward = 32
    blocks = 0
    blockTime = 60
    constants = {"constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": "proofofwork"}
    minimumTransactionCoins = 0.0000000001
    minimumTransactionFees = 0.0000000001
    nextHalving = 2102400
    previousBlockHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousCoinTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousTokenTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    previousNfcTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
    transactions = {}
    
    def init() :
        
        self.actual_transactions = {}
        self.blockchain = {}
        self.blockchainnumber = 0
        self.block = []
        self.blocksnotvalidated = []
        self.blocksnumber = 0
        syncChain
        
    def create_transaction(transactionType, sender, receiver, coins, fees, message) :
        
        self.hash = ""
        if transactionType = 0 : """ if the transaction is sending some coins """
            
            self.prevhash = previousCoinTransactionHash
            self.sender = sender
            self.receiver = receiver
            if Blockchain.coinsOfAddress(sender) <= coins :
                
                
                
            else :
                
                self.coins = coins
                
            self.message = message
            if fees < minimumTransactionFees :
                
                return()
                
            self.datas = ("{'prevtransactionhash': " +self.prevhash +", 'sender': '" +self.sender +"', 'receiver': '" +self.receiver +"', 'coins': " +self.coins +", 'fees': " +self.fees +"'message': '" +self.message +"'}")
            self.hash = chr(ord(self.datas *Wallet.public_keys[(sender)].privatekey +difficulty))
            return (self.hash)
        
        elif transactionType = 1 : """ if the transaction is sending some tokens """
            
            self.prevhash = previousCoinTransactionHash
            self.sender = sender
            self.receiver = receiver
            self.coins = minTransactionFees
            self.message = ""
            self.datas = ("{'prevtransactionhash': '" +self.prevhash +"', 'sender': '" +self.sender +"', 'receiver': '" +self.receiver +"', 'coins': " +self.coins +", 'message': '" +self.message +"'}")
            self.hash = ord(self.datas *Wallet.public_keys[(sender)].privatekey +difficulty)
            return (self.hash)
            
        elif transactionType = 2 : """ if the transaction is sending an nfc """
            
            self.hash = self.prevhash
            
    def create_block(message) :
        
        self.number = (blocks+1)
        self.prevhash = previousBlockHash
        self.txs = blockTransactions
        self.fees = totalFees
        self.message = message
        self.hash = Algorithms.sha256(Algorithms.caesar.encrypt("{'prevblknumb': " +self.number +", 'prevblkhash': '" +self.prevhash +", 'txs': " +self.txs +", 'blkfees': " +self.fees +", 'blkmsg': '" +self.message +"'}", difficulty))
        internet.issocket.send()
        
    def getBinaryDate() :
        
        binaryDate = (ord() +ord() +ord() +ord() +ord())
        return (binaryDate)
        
    def syncChain() :
        
        i = 0
        sameChainPeers = []
        peersBlocks = []
        peersBlocksVerifiee = {}
        for i < len(Network.peers) :
            
            chainId = Network.send.chainId(Network.peers[i])
            if chainId == walletChainId :
                
                sameChainPeers.insert(len(sameChainPeers), Network.peers[i])
                
            else :
                
                if len(sameChainPeers) == 0 :
                    
                    create_Block()
                    
    def verify_block(datas) :
        
        self.datas = datas
        self.hash = (((self.hash +"A") -blockchain.difficulty) -"A")
    
class Gui :
    
    
    
class Node :
    
    def peers() :
        
        self.nodeConstants = (Blockchain.nodesconstants["constant1"] *Blockchain.nodesConstants["constant2"] *Blockchain.nodesConstants["constant3"] *Blockchain.nodesConstants["constant4"] *Blockchain.nodesConstants["constant5"] *Blockchain.nodesConstants["conqtant6"] *Blockchain.nodesConstants["constant7"] *Blockchain.nodesConstants["constant8"])
        self.nodePeers = set[]
        self.nodePeers = open("peers.abpeers", "r+") /Blockchain.password /self.nodeConstants
        self.bannedPeers = set[]
        self.bannedPeers = open("bannedpeers.abpeers") /Blockchain.password /self.nodeConstants
        
    def addPeer(peerAddress) :
        
        peers.self.nodePeers.insert(len(peers.self.nodePeers), peerAddress)
        
    def banPeer(peerAddress) :
        
        peers.self.nodePeers.remove[peerAddress]
        peers.self.bannedPeers.insert(len(peers.self.bannedPeers), peerAddress)
        
    def chainId(nodes) :
        
        internetClient.send(nodes, "chainId")
        
    def internetServer() :
        
        issocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        issocket.bind("", 8448)
        issocket.listen(64)
        while True :
            
            if issocket.address !is_in peers.self.bannedPeers :
                
                client, address = issocket.accept()
            
            else :
                
                issocket.close()
                
        def send(datas) :
            
            issocket.send(datas)
            
    def internetClient(datas):
        
        icsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        icsocket.connect(peers.self.nodePeers, 8448)
        while True :
            
            icsocket.send()
            
        def send(datas) :
            
            icsocket.send(datas)
            
    def receivedDatas(datas) :
        
        self.datas = Algorithms.leya.decrypt(datas, Blockchain.difficulty)
        return (self.datas)
        
class Wallet :
    
    blockchainConstants = Blockchain.constants["constant1"] *Blockchain.constants["constant2"] *Blockchain.constants["constant3"] *Blockchain.constants["constant4"] *Blockchain.constants["constant5"] *Blockchain.constants["constant6"] *Blockchain.constants["constant7"] *Blockchain.constants["constant8"]
    private_keys = []
    public_keys = []
    walletFile = open("wallet.abdat", "r+")
    walletNumber = 0
    
    def create_wallet(password) :
        
        self.filename = "wallet" +walletNumber +".abdat"
        self.password = password
        self.private_keys = private_keys
        self.public_keys = public_keys
        self.datas = ((("'privkeys': [" +private_keys +", 'pubkeys': [" +public_keys +"]]") *chr(ord(password) *ord(blockchainConstants)) *blockchainConstants) +62)
        walletNumber += 1
        
    def unlock_wallet(self, password) :
        
        private_keys = Algorithms.caesar.decrypt(chr(walletFile /(ord(password) *ord(blockchainConstants)) /ord(blockchainConstants)), 62)[privkeys]
        public_keys =  Algorithms.caesar.decrypt(chr(walletFile /(ord(password) *ord(blockchainConstants)) /ord(blockchainConstants)), 62)[pubkeys]
        if !private_keys.startsWith("{'privkeys': [") :
            
            print("Error during the decryption of the private keys of the wallet !")
            
        if !public_keys.startsWith("{'pubkeys': [") :
            
            print ("Error during the decryption of the public keys of the wallet !")
            
            
    def create_private_key(self, create_wallet.password) :
        
        self.i = 0
        self.private_key = None
        self.private_finished_key = None
        for self.i < 416 :
            
            self.private_key += random.randint(0, 1)
            self.i += 1
            
        for self.i2 < (len(private_key) / 8) :
            
            self.private_finished_key = chr[(i2 *8) : ((i2 *8) +7)]
            self.i2 += 1
            
        self.private_finished_key += yourDate.binaryDate
        return (self.private_finished_key)
        
    def create_public_key(self, chosensecretkey) :
        
        self.public_key = None
        if chosensecretkey in private_keys :
            
            self.public_key = "AB" + hashlib.sha256(private_keys[(chosensecretkey)]).hexdigest()[0 : 498]
            public_keys.insert(len(public_keys), self.public_key)
            
        else :
            
            print("Error, the chosen secret key is not in the private keys !")
            
class yourDate() :
    
    def binaryDate() :
        
        return (time.tm_year +time.tm_month +time.tm_day +time.tm_hour +time.tm_min)
