import hashlib
import keyboard
import PySide6.QtCore
import random
import socket
import threading
import time

class blkChainDatas :
    
    blockchainFile = open("blockchain.abdat", "r+")
    Blockchain.blockchainDatas.chain = chr(ord(blockchainFile) /ord(Algorithms.leya.constantsresult) /ord("ayzelyc blockchain"))
    peersFile = open("peers.abdat", "r+")
    Blockchain.blockchainDatas.peers = chr(ord(peersFile) /ord(Algorithms.leya.constantsresult) /ord("ayzelyc blockchain"))
    walletFile = open("wallet.abdat", "r+")
    Wallet.public_keys = chr(ord(walletFile) /ord(Blockchain.constantsresult))
    
class Algorithms :
    
    class caesar() :
        
        def encrypt(datas, difficulty) :
            
            encrypted_datas = ""
            if len(datas) == 0 :
                
                print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be encrypted !")
                
            else :
                
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
                    
    class leya() :
        
        self.constants = "'constant1': 'leaalgorithm', 'constant2': 'leacoin', 'constant3': 'blockchain', 'constant4': 'crypto', 'constant5': 'algorithm', 'constant6': 'chain', 'constant7': 'hashed', 'constant8': 'wallets'"
        constantsresult = chr(ord(self.constants["constant1"]) *ord(self.constants["constant2"]) *ord(self.constants["constant3"]) *ord(self.constants["constant4"]) *ord(self.constants["constant5"]) *ord(self.constants["constant6"]) *ord(self.constants["constant7"]) *ord(self.constants["constant8"]))
        
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
                
                if difficulty <= 0 :
                    
                    print ("Error during the usage of the leya algorithm, the difficulty can't be smaller than 1 !")
                    
                elif difficulty >= 1 :
                    
                    return (chr(ord(datas) /ord(constantsresult) /difficulty -difficulty))
                    
        def bruteForce(datas) :
            
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
                    
    class leya2() :
        
        def encrypt(datas, difficulty, password) :
            
            return (chr((ord(datas) *ord(password)) +difficulty))
            
        def decrypt(datas, difficulty, password) :
            
            return (chr((ord(datas) -difficulty) /ord(password)))
            
        def bruteForce(datas) :
            
            
            
    def scrypt(datas, password, difficulty, ramdifficulty) :
        
        self.datas = datas
        self.difficulty = difficulty
        self.password = password
        self.ramdifficulty = ramdifficulty
        if len(datas) == 0 :
            
            print ("The bits size of the datas is equal to 0 !")
            
        else :
            
            return (hashlib.scrypt(datas, password, ramdifficulty).hexdigest())
            
    class sha256() :
        
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
                
    class sha512(datas, password, difficulty) :
        
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
        
        blockchainInfos = { "chainid": 0, "blkNumber": 0, "blkReward": 32, "blkTime": 60, "minTxCoins": 0.00000001, "minTxFees": 0.00000001, "halvEach": 2102400, "previousBlockHash": "0000000000000000000000000000000000000000000000000000000000000000", "previousCoinTransactionHash": "0000000000000000000000000000000000000000000000000000000000000000", "previousNfcTransactionHash": "0000000000000000000000000000000000000000000000000000000000000000", "previousTokenTransactionHash": "0000000000000000000000000000000000000000000000000000000000000000" }
        chain = []
        chain0Peers = ["176.136.166.254", "2001:861:4480:6fe0:f83c:e6ea:1b93:588f"]
        constants = {"constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": "proofofwork"}
        mining = 0
        nodeDatas = {"name": "ABlockchain v1.0", "version": 1.0, "address": "127.0.0.1", "port": 8448, "maxcons": 32}
        peers = []
        waitingTransactions = []
    
    def init() :
        
        self.unspendTxs = set({})
        self.blkchain = set({})
        self.chainId = blockchainDatas.blockchainInfos["chainId"]
        self.block = set({})
        self.blksNotValidated = set([])
        self.blksNumber = 0
        
        blockchainDatas.peers = findPeers("1.0.0.0", "254.255.255.255", 8448, "leyaBlockchainChain")
        Internet.internetClient.connect(blockchainDatas.peers[0 : (blockchainDatas.nodeDatas["maxcons"])])
        Internet.internetClient.send("syncChain", blockchainDatas.blockchainInfos["chainId"])
        blocksReceived = Internet.internetClient.receiveDatas()
        
    def create_transaction(transactionType, sender, receiver, coins, fees, message) :
        
        self.transactionType = transactionType
        self.sender = sender
        self.receiver = receiver
        self.coins = coins
        self.fees = fees
        self.transactionMessage = message
        self.datas = ""
        self.hash = 0
        
        if self.transactionType == 1 and len(self.sender) == blockchainDatas.chain["chainPubKeySize"] and len(self.receiver) == blockchainDatas.chain["chainPubKeySize"] and self.coins >= Wallet.public_keys[(self.sender)["coins"]] +blockchainDatas.chain["chainTransactionFees"] and self.fees >= blockchainDatas.chain["chainMinimumTransactionFees"] :
            
            
            
        elif transactionType == 2 and len(self.sender) == blockchainDatas.chain["chainPubKeySize"] and len(self.receiver) == blockchainDatas.chain["chainPubKeySize"] and self.coins >= Wallet.public_keys[(self.sender)["coins"]] +blockchainDatas.chain["chainTransactionFees"] and self.fees >= blockchainDatas.chain["chainMinimumTransactionFees"] :
            
            
            
        elif transactionType == 3 and len(self.sender) == blockchainDatas.chain["chainPubKeySize"] and len(self.receiver) == blockchainDatas.chain["chainPubKeySize"] and self.coins >= Wallet.public_keys[(self.sender)["coins"]] +blockchainDatas.chain["chainTransactionFees"] and self.fees >= blockchainDatas.chain["chainMminimumTransactionFees"] :
            
            
            
        else :
    def create_block(authorAddress, message) :
        
        self.number = (blocks+1)
        self.prevhash = previousBlockHash
        self.txs = blockTransactions
        self.fees = totalFees
        self.message = message
        self.datas = "{'blknumb': " +self.number +", 'prevblkhash': '" +self.prevhash +"', 'blkfees': " +self.fees +"}"
        if Blockchain.blockchainDatas.algo == 1 :
            
            self.hash = Algorithms.caesar.encode(self.datas)
            Algorithms.caesar.bruteForce()
            
        elif Blockchain.blockchainDatas.algo == 2 :
            
            self.hash = Algorithms.leya.encrypt("{'prevblknumb': " +self.number +", 'prevblkhash': '" +self.prevhash +", 'txs': " +self.txs +", 'blkfees': " +self.fees +", 'blkmsg': '" +self.message +"'}", difficulty))
            Algorithms.leya.bruteForce(self.hash)
            
    def create_nfc(authorAddress, fileType, file) :
        
        self.author = authorAddress
        self.fileType = fileType
        self.fileDatas = file
        
    def create_token(authorAddress, tokenDescription, tokenStartingNumber, tokenGlobal, tokenSystem, tokenMaxNumber) :
        
        self.author = authorAddress """ the ayzelyc blockchain address of the token author """
        self.tkDescription = tokenDescription """ the description of the token """
        self.tkStartNumb = tokenStartingNumber """ the number of tokens when he's created """
        self.tkGlob = tokenGlobal """ if the token is gived after each transaction / each block mined ... """
        self.tkSystem = tokenSystem """ if the token is under a POW / POS / other rewarding system """
        self.tkMaxNumb = tokenMaxNumber """ the maximal number of tokens """
        
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
        
        guiButtons = { "buttons": { "home": { "xSize": 100, "ySize": 100, "image": "" }, "addresses": { "xSize": 50, "ySize": 50, "image": "" }, "background": { "xSize": 1920, "ySize": 1080, "image": "" } ,"discord": { "xSize": 50, "ySize": 50, "image": "" }, "instagram": { "xSize": 50, "ySize": 50, "image": "" }, "loading": { "xSize": 1920, "ySize": 1080, "image": "" }, "twitter": { "xSize": 50, "ySize": 50, "image": "" } } }
        guiTexts = { "texts": { "de": { "home": "" }, "en": { "home": "Home" }, "fr": { "home": "Menu" }, "it": { "home": "" }, "sp": { "home": "" } } }
        guiWindow = { "image": "", "title": "AyzeLYC Blockchain Wallet", "xSize": 1920, "ySize": 1080 }
        logs = []
        
    backgroundImage = QImage(guiDatas.guiButtons["background"["image"]], guiDatas.guiButtons["background"["xSize"]], guiDatas.guiButtons["background"["ySize"]] alignment=QtCore.Qt.AlignCenter)
    backgroundImage.enabled = False
    loadingImage = QImage(guiDatas.guiButtons["loading"["image"]], guiDatas.guiButtons["loading"["xSize"]], guiDatas.guiButtons["loading"["ySize"]] ,alignment=QtCore.Qt.AlignCenter)
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
        gui.resize(guiDatas.guiWindow["xSize"], guiDatas.guiWindow["ySize"])
        gui.setWindowIcon(guiDatas.guiWindow["image"])
        gui.setWindowOpacity(1)
        gui.setWindowTitle(guiDatas.guiWindow["title"])
        
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
        
        gui.show()
        
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
        
    def create_private_key(create_wallet.password) :
        
        self.i = 0
        self.private_key = None
        self.private_finished_key = None
        for self.i != 416 :
            
            self.private_key += random.randint(0, 1)
            self.i += 1
            
        for (len(private_key) / 8) != 52 :
            
            self.private_finished_key = chr[(i2 *8) : ((i2 *8) +7)]
            
        self.private_finished_key += yourDate.binaryDate
        return (self.private_finished_key)
        
    def create_public_key(chosensecretkey) :
        
        self.public_key = None
        if chosensecretkey in private_keys :
            
            self.public_key = "AB" + hashlib.sha256(private_keys[(chosensecretkey)]).hexdigest()[0 : 498]
            public_keys.append(self.public_key)
            
        else :
            
            print("Error, the chosen secret key is not in the private keys !")
            
    def lock_wallet(password) :
        
        blkChainDatas.walletFile = Algorithms.caesar.encrypt("{ 'privkeys': [" +chr(ord(self.private_keys) *ord(password) *ord(blockchainConstants)) +"], 'pubkeys': [" +chr(ord() *ord(password) *ord(blockchainConstants) +"] }"), 62)
        
    def unlock_wallet(password) :
        
        private_keys = Algorithms.caesar.decrypt(chr(ord(blkChainDatas.walletFile) /(ord(password) /ord(blockchainConstants)), 62)[privkeys]
        public_keys = Algorithms.caesar.decrypt(chr(ord(blkChainDatas.walletFile) /(ord(password) /ord(blockchainConstants)), 62)[pubkeys]
        if !private_keys.startsWith("{'privkeys': [") :
            
            print ("Error during the decryption of the private keys of the wallet !")
            
        if !public_keys.startsWith("{'pubkeys': [") :
            
            print ("Error during the decryption of the public keys of the wallet !")
            
class yourDate() :
    
    def binaryDate() :
        
        return (time.tm_year +time.tm_month +time.tm_day +time.tm_hour +time.tm_min)
    
if keyboard.on_press_key("ctrl+alt+s") :
    
    Blockchain.blockchainDatas.verifyingBlocks = 0
    Blockchain.blockchainDatas.mining = 0
    Node.threading.stopAll
    Internet.internetClient.icsocket.stop
    Internet.internetServer.issocket.stop
    walletDatas.blockchainFile.write(Blockchain.blockchainDatas.chain[(len(Blockchain.blockchainDatas.chain) -len(walletDatas.blockchainFile)) : len(Blockchain.blockchainDatas.chain)])
