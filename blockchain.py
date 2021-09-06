import hashlib
import keyboard
import PySide6.QtCore
import random
import socket
import threading
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
                    
                return (encrypted_datas)
                
        def decrypt(datas, difficulty) :
            
            decrypted_datas = ""
            if len(datas) == 0 :
                
                print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be decrypted !")
                
            else :
                
                encrypted_datas = ""
                for char in datas :
                    
                    encrypted_datas += chr(ord(chr) -difficulty)
                    
                return (encrypted_datas)
                    
    def leya() :
        
        self.constants = "'constant1': 'leaalgorithm', 'constant2': 'leacoin', 'constant3': 'blockchain', 'constant4': 'crypto', 'constant5': 'algorithm', 'constant6': 'chain', 'constant7': 'hashed', 'constant8': 'wallets'"
        constantsresult = (self.constants["constant1"] *self.constants["constant2"] *self.constants["constant3"] *self.constants[] *self.constants[] *self.constants[] *self.constants[] *self.constants[])
        
        def encrypt(datas, difficulty) :
            
            if len(datas) == 0 :
                
                print ("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                if difficulty <= 0 :
                    
                    return (chr(ord(datas) *ord(constantsresult)))
                    
                elif difficulty >= 1 :
                    
                    return (chr((ord(datas) +difficulty) *ord(difficulty) *ord(constantsresult)))
                    
        def decrypt(datas, difficulty) :
            
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                constantsresult = (self.constants["constant1"] *self.constants["constant2"] *self.constants["constant3"] *self constants["constant4"] *self constants["constant5"] *self.constants["constant6"] *self.constants["constant7"] *self.constants["constant8"])
                if difficulty <= 0 :
                    
                    return (chr(ord(datas) /ord(constantsresult)))
                    
                elif difficulty >= 1 :
                    
                    return (chr(ord(datas) /ord(constantsresult) /difficulty -difficulty))
                    
        def bruteForce(datas, difficulty) :
            
            constantsresult = ()
            if len(datas) == 0 :
                
                print("The bit size of the datas inserted is equal to 0 !")
                
            else :
                
                i = 0
                if !datas.startWith("{'datas':") :
                    
                    datas2 = chr(ord(datas) /ord(constantsresult) /i -i)
                    i += 1
                    datas2 = chr((ord(datas) +i) *i *ord(constantsresult))
                    
                else :
                    
                    return (datas)
                    
    def leya2() :
        
        def encrypt(datas, difficulty, password) :
            
            return (chr((ord(datas) *ord(password)) +difficulty))
            
        def decrypt(datas, difficulty, password) :
            
            return (chr((ord(datas) -difficulty) /ord(password)))
            
    def scrypt(datas, password, difficulty, ramdifficulty) :
        
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        self.ramdifficulty = ramdifficulty
        if len(datas) == 0 :
            
            print ("The bits size of the datas is equal to 0 !")
            
        else :
            
            return (hashlib.scrypt(datas, password, ramdifficulty).hexdigest())
            
    def sha256() :
        
        def encrypt(datas, password, difficulty) :
            
            if len(datas) == 0 :
                
                print ("Error, the datas length is equal to 0 or null !")
                
            else :
                
                if password == 0 or null :
                    
                    if difficulty <= 0 :
                        
                        return (hashlib.sha256(datas).hexdigest())
                        
                    else :
                        
                        return (hashlib.sha256(caesar.encrypt(datas, difficulty)).hexdigest())
                        
                else :
                    
                    if difficulty <= 0 :
                        
                        datas *= password
                        return (hashlib.sha256(datas).hexdigest())
                        
                    else :
                        
                        datas *= password
                        return (hashlib.sha256(caesar.encrypt(datas, difficulty )).hexdigest())
                        
        def bruteForce(hash) :
            
            self.hash = hash
            i = 0
            datas = ""
            hashedDatas = ""
            if hashedDatas != self.hash :
                
                datas = chr(i)
                hashedDatas = hashlib.sha256(datas).hexdigest()
                i += 1
                
            else :
                
                return (datas)
                
    def sha512(datas, password, difficulty) :
        
        if len(datas == 0) :
            
            print ("Error, the datas length is equal to 0 or null !")
            
        else:
            
            if password == 0 or null and difficulty <= 0 :
                
                return (hashlib.sha512(datas).hexdigest())
            elif password == 0 or null and difficulty >= 1 :
                
                return (hashlib.sha512(caesar.encrypt(datas, difficulty)).hexdigest())
                
            elif password != 0 and null and difficulty <= 0 :
                
                return (hashlib.sha512(chr(ord(datas) *ord(password))).hexdigest())
                
            elif password != 0 and null and difficulty >= 1 :
                
                return (hashlib.sha512(chr(ord(caesar.encrypt(datas, difficulty)) *ord(password))).hexdigest())
                
        def bruteForce(hash) :
            
            self.hash = hash
            datas = ""
            hashedDatas = ""
            if hashedDatas != self.hash :
                
                datas = chr(i)
                hashedDatas = hashliv.sha512(datas).hexdigest()
                i += 1
                
            else :
                
                return ("{'datas': '" +datas +"', 'difficulty': " +datas['difficulty'] +", 'password': '" +chr(i) +"'")
                
class Blockchain :
    
    def blockchainDatas :
        
        blockChain = set([])
        blockChainId = 0
        blockTime = 60
        blocksNumber = 0
        blockChainPeers = set([])
        blocksReward = 32
        constants = {"constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": "proofofwork"}
        minimumTransactionCoins = 0.0000000001
        minimumTransactionFees = 0.0000000001
        nextHalving = 2102400
        nodeDatas = {"name": "ABlockchain v1.0", "version": 1.0, "address": "127.0.0.1", "port": 8448, "maxcons": 32}
        previousBlockHash = "0000000000000000000000000000000000000000000000000000000000000000"
        previousCoinTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
        previousTokenTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
        previousNfcTransactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
        waitingTransactions = set({})
    
    def init() :
        
        self.actual_transactions = set({})
        self.blockchain = set({})
        self.chainId = 0
        self.block = set({})
        self.blocksNotValidated = set([])
        self.blocksNumber = 0
        Node.internetServer.start(blockchainDatas.nodeDatas{"maxcons"}, blockchainDatas.nodeDatas{"address"}, blockchainDatas.nodeDatas{"port"})
        if len(blockchainDatas.blockChainPeers) == 0 :
            
            print ("There are not peers ")
            
        else :
            
            Node.internetClient.connect(blockchainDatas.blockchainPeers[0 : 15])
            
    def create_transaction(transactionType, sender, receiver, number, fees, message) :
        
        self.hash = ""
        self.fees = fees
        if transactionType == 0 : """ if the transaction is sending some coins """
            
            if Blockchain.coinsOfAddress(sender) <= (coins +self.fees) :
                
                print ("Error during the usage of the create_transaction function, you don't have enough coins to send the transaction !")
                
            else :
                
                if len(receiver) != (blockchainDatas.pubKeysBytesSize *8) :
                    
                    
                    
                else :
                    
                    self.sender = sender
                    self.receiver = receiver
                    self.coins = number
                    self.message = message
                    
                    self.datas = "{'prevtxhash': '" +blockchainDatas.previousCoinTransactionHash +"', 'sender': '" +self.sender +"', 'receiver': '" +self.receiver +"', 'coins': " +self.coins +", 'message': '" +self.message +"'}")
                    self.hash = Algorithms.leya.encode(chr(ord(self.datas) *ord(Wallet.public_keys[(sender)["privatekey"]])), difficulty)
                    return (self.hash)
                    
        elif transactionType == 1 : """ if the transaction is sending some tokens """
            
            self.prevhash = blockchainDatas.previousCoinTransactionHash
            self.sender = sender
            self.receiver = receiver
            self.coins = number
            self.message = message
            self.datas = ("{'prevtransactionhash': '" +self.prevhash +"', 'sender': '" +self.sender +"', 'receiver': '" +self.receiver +"', 'coins': " +self.coins +", 'message': '" +self.message +"'}")
            self.hash = ord(self.datas *Wallet.public_keys[(sender)].privatekey +difficulty)
            return (self.hash)
            
        elif transactionType == 2 : """ if the transaction is sending an nfc """
            
            self.hash = self.prevhash
            
    def create_block(message) :
        
        self.number = (blocks+1)
        self.prevhash = previousBlockHash
        self.txs = blockTransactions
        self.fees = totalFees
        self.message = message
        self.hash = Algorithms.leya.encrypt("{'prevblknumb': " +self.number +", 'prevblkhash': '" +self.prevhash +", 'txs': " +self.txs +", 'blkfees': " +self.fees +", 'blkmsg': '" +self.message +"'}", difficulty))
        blockChain.append(self.hash)
        node.internet.issocket.send(self.hash)
        
    def getBinaryDate() :
        
        binaryDate = (ord(time.tm_year) +ord(time.tm_month) +ord(time.tm_day) +ord(time.tm_hour) +ord(time.tm_minute))
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
                    
    def verify_block(hash, diff) :
        
        if hash["blknumb"] == blockchainSize +1 :
            
            self.hash = hash
            self.datas = Algorithms.leya.decode(Algorithms.caesar.decrypt(self.hash, blockchainDatas.blockchainDifficulty), blockchainDatas.blockchainDifficulty)
            
        else :
            
            self.hash = hash
            self.datas = Algorithms.leya.decode(Algorithms.caesar.decrypt(self.hash, diff), diff)
            
class Gui :
    
    def guiDatas() :
        
        guiButtons = { "buttons": { "home": { "xSize": 100, "ySize": 100, "image": "" }, "addresses": { "xSize": 50, "ySize": 50, "image": "" }, "discord": { "xSize": 50, "ySize": 50, "image": "" }, "instagram": { "xSize": 50, "ySize": 50, "image": "" }, "twitter": { "xSize": 50, "ySize": 50, "image": "" } } }
        guiTexts = { "texts": { "de": { "home": "" }, "en": { "home": "Home" }, "fr": { "home": "Menu" }, "it": { "home": "" }, "sp": { "home": "" } } }
        guiWindow = { "title": "AyzeLYC Blockchain Wallet", "xSize": 1920, "ySize": 1080 }
        
    backgroundImage = QPushImage("./images/background.jpg")
    backgroundImage.enabled = False
    loadingImage = QPushImage("./images/loading.jpg")
    loadingImage.enabled = True
    
    homeButton = QPushButton("Home")
    homeButton.enabled = False
    addressesButton = QPushButton("Addresses")
    addressesButton.enabled = False
    filesButton = QPushButton("Files")
    filesButton.enabled = False
    transactionsButton = QPushButton("Transactions")
    transactionsButton.enabled = False
    parametersButton = QPushButton("Parameters")
    parametersButton.enabled = False
    peersButton = QPushButton("Peers")
    peersButton.enabled = False
    
    socialNetworksButton = QPushButton("Social networks")
    discordButton = QPushButton("Discord")
    discordButton.enabled = False
    instagramButton = QPushButton("Instagram")
    instagramButton.enabled = False
    twitterButton = QPushButton("Twitter")
    twitterButton.enabled = False
    
    when Blockchain.blockchainDatas.syncedChain = 1 :
        
        backgroundImage.enabled = True
        loadingImage.enabled = False
        
        homeButton.enabled = True
        addressesButton.enabled = True
        filesButton.enabled = True
        transactionsButton.enabled = True
        parametersButton.enabled = True
        peersButton.enabled = True
        sendButton.enabled = True
        socialNetworksButton.enabled = True
        
        gui = QVBoxLayout
        gui.add_widget(backgroundImage)
        gui.add_widget(loadingImage)
        
        gui.add_widget(homeButton)
        gui.add_widget(addressesButton)
        gui.add_widget(commandLineButton)
        gui.add_widget(commandLineLine)
        gui.add_widget(commandLineOutputs)
        gui.add_widget(transactionsButton)
        gui.add_widget(parametersButton)
        gui.add_widget(peersButton)
        gui.add_widget(sendButton)
        gui.add_widget(socialNetworksButton)
        gui.add_widget(discordButton)
        gui.add_widget(instagramButton)
        gui.add_widget(twitterButton)
        
        when filesButton.clicked :
            
            if guiDatas.page = 1 :
                
                
                
            else :
                
                guiDatas.page = 1
                
        when parametersButton.clicked :
            
            if guiDatas.page = 2 :
                
                
                
            else :
                
                guiDatas.page = 2
                
        when othersButton.clicked :
            
            if guiDatas.page = 3 :
                
                
                
            else :
                
                guiDatas.page = 3
                commandLineOutputs.enabled = True
                commandLineLine.enabled = True
                
        when homeButton.clicked :
            
            if guiDatas.page = 4 :
                
                
                
            else :
                
                guiDatas.page = 4
                
        when sendButton.clicked :
            
            if guiDatas.page = 5 :
               
                
                
            else :
                
                guiDatas.page = 5
                
        when addressesButton.clicked :
            
            if guiDatas.page = 6 :
                
                
                
            else :
                
                guiDatas.page = 6
                
        when transactionsButton.clicked :
            
            if guiDatas.page = 7 :
                
                
                
            else :
                
                guiDatas.page = 7
                
        when socialNetworksButton.clicked :
            
            if guiDatas.page = 8 :
                
                
                
            else :
                
                guiDatas.page = 8
                
class Node :
    
    def nodeDatas() :
        
        def peers() :
            
            self.nodeConstants = (Blockchain.blockchainDatas.nodesconstants["constant1"] *Blockchain.blockchainDatas.nodesConstants["constant2"] *Blockchain.blockchainDatas.nodesConstants["constant3"] *Blockchain.blockchainDatas.nodesConstants["constant4"] *Blockchain.blockchainDatas.nodesConstants["constant5"] *Blockchain.blockchainDatas.nodesConstants["conqtant6"] *Blockchain.blockchainDatas.nodesConstants["constant7"] *Blockchain.blockchainDatas.nodesConstants["constant8"])
            self.nodePeers = set([])
            self.nodePeers = self.bannedPeers.append(chr(ord(open("peers.abpeers", "r+")) /ord(Blockchain.password) /ord(self.nodeConstants)))
            self.bannedPeers = set([])
            self.bannedPeers = self.bannedPeers.append(chr(ord(open("bannedpeers.abpeers")) /ord(Blockchain.password) /ord(self.nodeConstants)))
        
    def addPeer(peerDatas) :
        
        if peerDatas not in nodeDatas.peers.bannedPeers :
            
            nodeDatas.peers.nodePeers.append(peerDatas)
            
        else :
            
            
            
    def banPeer(peerDatas) :
        
        if peerDatas in nodeDatas.peers.nodePeers :
            
            peers.self.nodePeers.remove(peerDatas)
            peers.self.bannedPeers.append(peerDatas)
            
        else :
            
            nodeDatas.peers.bannedPeers.append(peerDatas)
            
    def chainId() :
        
        internetClient.send(peers.nodePeers, "{'datas': 'request', 'message': 'chainId'}")
        
        
    def internetServer() :
        
        issocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        issocket.bind(Blockchain.blockchainDatas.nodeDatas["address"], 8448)
        issocket.listen(Blockchain.blockchainDatas["maxcons"])
        while True :
            
            if issocket.address !is_in peers.self.bannedPeers :
                
                client, address = issocket.accept()
                
            else :
                
                issocket.close()
                
        def send(datas) :
            
            issocket.send(datas)
            return (recv())
            
    def internetClient():
        
        icsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        icsocket.connect(peers.self.nodePeers, 8448)
        def sendDatas(datasSent) :
            
            icsocket.send(datasSent)
            recv(datasReceived)
            return (datasReceived)
            
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
            
            print ("Error during the decryption of the private keys of the wallet !")
            
        if !public_keys.startsWith("{'pubkeys': [") :
            
            print ("Error during the decryption of the public keys of the wallet !")
            
            
    def create_private_key(self, create_wallet.password) :
        
        self.i = 0
        self.private_key = None
        self.private_finished_key = None
        for self.i != 416 :
            
            self.private_key += random.randint(0, 1)
            self.i += 1
            
        for (len(private_key) / 8) != 52 :
            
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
    
if keyboard.on_press_key("ctrl+alt+s") :
    
    Blockchain.blockchainDatas.verifyingBlocks = 0
    Blockchain.blockchainDatas.miningBlocks = 0
    Gui.stop
    Node.threading.stopAll
    Internet.internetClient.icsocket.stop
    Internet.internetServer.issocket.stop
