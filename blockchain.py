import hashlib
import keyboard
import PySide6.QtCore
import random
import socket
import threading
import time

class Main :

    class blkChainDatas :

        blockchainFile = open("blockchain.abdat", "r+")
        Blockchain.blockchainDatas.chain = chr(ord(blockchainFile) /ord(Algorithms.leya.constantsresult) /ord("ayzelyc blockchain"))
        peersFile = open("peers.abdat", "r+")
        Blockchain.blockchainDatas.peers = chr(ord(peersFile) /ord(Algorithms.leya.constantsresult) /ord("ayzelyc blockchain"))
        walletFile = open("wallet.abdat", "r+")
        Wallet.public_keys = chr(ord(walletFile) /ord(Blockchain.constantsresult))["pubkeys"]
        Wallet.private_keys = chr(ord(walletFile) /ord(Blockchain.constantsresult))["privkeys"]

    class Algorithms :

        class caesar :

            def encrypt(datas, difficulty) :

                self.datas = datas
                self.difficulty = difficulty
                self.encrypted_datas = ""
                if len(self.datas) == 0 :

                    print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be encrypted !")

                else :

                    for char in self.datas :

                        self.encrypted_datas += chr(ord("{ 'datas': '"), ord(char), ord("' }") +self.difficulty)

                    return (self.encrypted_datas)

            def decrypt(datas, difficulty) :

                self.datas = datas
                self.decrypted_datas = ""
                self.difficulty = difficulty
                if len(self.datas) == 0 :

                    print ("The datas who are being encrypted in the caesar algorithm get a size of 0 bits, they can't be decrypted !")

                else :

                    for char in datas :

                        self.decrypted_datas += chr(ord(chr) -self.difficulty)

                    return (self.decrypted_datas)

            def bruteForce(datas) :

                self.datas = datas
                self.decrypted_datas = ""
                self.i = 0
                if len(self.datas) == 0 :



                else :



        class leya :

            self.constants = "'constant1': 'leaalgorithm', 'constant2': 'leacoin', 'constant3': 'blockchain', 'constant4': 'crypto', 'constant5': 'algorithm', 'constant6': 'chain', 'constant7': 'hashed', 'constant8': 'wallets'"
            constantsresult = chr(ord(self.constants["constant1"]) *ord(self.constants["constant2"]) *ord(self.constants["constant3"]) *ord(self.constants["constant4"]) *ord(self.constants["constant5"]) *ord(self.constants["constant6"]) *ord(self.constants["constant7"]) *ord(self.constants["constant8"]))

            def encrypt(datas, difficulty) :

                if len(datas) == 0 :

                    print ("The bit size of the datas inserted is equal to 0 !")

                else :

                    for difficulty <= 0 :

                        return (chr(ord(datas) *ord(constantsresult)))

                    elif difficulty >= 1 :

                        return (chr((ord(datas) +difficulty) *ord(difficulty) *ord(constantsresult)))

            def decrypt(datas, difficulty) :

                if len(datas) == 0 :

                    print("The bit size of the datas inserted is equal to 0 !")

                else :

                    for difficulty <= 0 :

                        print ("Error during the usage of the leya algorithm, the difficulty can't be smaller than 1 !")

                    elif difficulty >= 1 :

                        return (chr(ord(datas) /ord(constantsresult) /ord(difficulty) -difficulty))

            def bruteForce(datas) :

                self.datas = datas
                self.i = 0
                if len(self.datas) == 0 :

                    print("The bit size of the datas inserted is equal to 0 !")

                elif len(self.datas) != 0 datas.startswith("{'datas':") :

                    return (self.datas)

                else :

                    self.datas = chr(ord(self.datas) /ord(constantsresult) /ord(self.i) -self.i)
                    i += 1
                    self.datas = chr((ord(self.datas) +i) *ord(i) *ord(constantsresult))

        class leya2 :

            def encrypt(datas, difficulty, password) :

                return (chr(ord(datas) *ord(password) +difficulty))

            def decrypt(datas, difficulty, password) :

                return (chr(ord(datas) -difficulty) /ord(password)))

        class scrypt :

            def hash(datas, password, difficulty, ramdifficulty) :
            self.datas = datas
            self.difficulty = difficulty
            self.password = password
            self.ramdifficulty = ramdifficulty
            if len(datas) == 0 :

                print ("The bits size of the datas is equal to 0 !")

            else :

                return (hashlib.scrypt(datas, password, ramdifficulty).hexdigest())

        class sha256 :

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

            def hash(datas, password, difficulty) :

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
                self.datas = ""
                self.hashedDatas = ""
                if hashedDatas != self.hash :

                    self.datas = chr(i)
                    self.hashedDatas = hashlib.sha512(self.datas).hexdigest()
                    i += 1

                else :

                    print ("Found the datas after " ,i ," tries !")
                    return (self.datas)

    class Blockchain :

        def blockchainDatas :

            blockchainInfos = { "chainid": 0, "blkNumber": 0, "blkReward": 32, "blkTime": 60, "minTxCoins": 0.00000001, "minTxFees": 0.00000001, "halvEach": 2102400, "previousBlockHash": "0000000000000000000000000000000000000000000000000000000000000000", "previousTransactionHash": "0000000000000000000000000000000000000000000000000000000000000000" }
            chain = { "difficulty": 1, "chainMinimumTransactionFees": 0.00000001, "blocks": [], "transactions": [], "fees": 0 }
            chain0Peers = [ "176.136.166.254", "2001:861:4480:6fe0:f83c:e6ea:1b93:588f" ]
            constants = { "constant1": "blockchain", "constant2": "cryptocurrency", "constant3": "testchain", "constant4": "nfcs", "constant5": "tokens", "constant6": "proofofwork" }
            mining = 0
            nodeDatas = { "name": "ABlockchain v1.0", "version": 1.0, "address": "127.0.0.1", "port": 8448, "maxcons": 32 }
            peers = []

        def INIT() :

            self.unspendTxs = set({})
            self.blkchain = set({})
            self.chainId = blockchainDatas.blockchainInfos["chainId"]
            self.block = set({})
            self.blksNotValidated = set([])
            self.blksNumber = 0
            self.blksReceived = set([])

            if len(blockchainDatas.peers) == 0 :

                blockchainDatas.peers = findPeers("1.0.0.0", "254.255.255.255", 8448, "leyaBlockchainChain")
                if len(blockchainDatas.peers) == 0 :

                    create_transaction("{'sender': 'COINBASE', 'receivers': [ '" +"' ], 'coins': [ '" +blockchainDatas.blockchainInfos["blkReward"] +"' ], 'fees': 0, 'message': 'MINED TRANSACTION'}")
                    create_block()
                    verify_block(blockchainDatas.chain["blocks"[len(blockchainDatas.chain["blocks"]) -1]])

                else :

                    Internet.internetClient.connect(blockchainDatas.peers[0 : (blockchainDatas.nodeDatas["maxcons"])])
                    Internet.internetClient.send("{ 'command': 'syncChain', 'datas': " +blockchainDatas.blockchainInfos["chainId"] +" }")
                    self.blksReceived = Internet.internetClient.icsocket.recv()
                    self.blkchain.insert(len(self.blkchain), verifyChain(self.blksChain))

            else :

                Internet.internetClient.connect(blockchainDatas.peers[0 : (blockchainDatas.nodeDatas["maxcons"])])
                Internet.internetClient.send("{ 'command': 'syncChain', 'datas': " +blockchainDatas.blockchainInfos["chainId"] +" }")
                self.blksReceived = Internet.internetClient.icsocket.recv()
                self.blkchain.insert(len(self.blkchain), verifyChain(self.blksChain))

    def create_transaction(datas) :

            self.prevhash = blockchainDatas.chain["prevtxhash"]
            self.sender = datas["sender"]
            self.receivers = datas["receivers"]
            self.coins = datas["coins"]
            self.fees = datas["fees"]
            self.message = datas["message"]

            self.datas = ""

            if transactionType == 1 :

                for len(self.sender) == blockchainInfos.chain["pubkeysize"] and len(self.receiver) == 
                self.datas = "{ 'prevtxhash': '" +self.prevhash +"', 'txsender': '" +self.sender +"', 'txreceiver': '" +self.receiver +"' +'coins': '" +self.coins +"', 'txfees': " +self.fees +"'message': '" +self.message +"' }"

            elif transactionType == 2 :

                self.datas = "{ 'prevtxhash': '', 'txsender': '" +self.sender +"', 'txreceiver': [" +self.receivers +"], 'coins': [" +self.coins +"], 'txfees': self.fees, 'message': { 'tksender': '" +self.sender +"', 'tkreceiver': [] } }"

            elif transactionType == 3 :

                self.datas = "{ 'prevtxhash': '', 'txsender': '" +self.sender +"', 'txreceiver': [" +self.receivers "], 'coins': [" +self.coins +"], 'txfees': self.fees, 'message': {  } }"

            else :

                print ("Error during the creation of a transaction, the transactionType is not equal to 1, 2 or 3 !")

        def create_block(authorAddress, message) :

            self.difficulty = blockchainDatas.chain["difficulty"] +random.randint(0, 100)

            self.number = len(blockchainDatas.chain["blocks"])
            self.prevhash = previousBlockHash
            self.txs = blockchainDatas.chain["transactions"]
            self.fees = blockchainDatas.chain["fees"]
            self.message = message

            self.datas = "{'prevblknumb': " +self.number +", 'prevblkhash': '" +self.prevhash +", 'txs': " +self.txs +", 'blkfees': " +self.fees +", 'blkmsg': '" +self.message +"'}"
            if blockchainDatas.algo == 1 :

                self.hash = Algorithms.caesar.encrypt(self.datas, self.difficulty)
                Algorithms.caesar.bruteForce()

            elif blockchainDatas.algo == 2 :

                self.hash = Algorithms.leya.encrypt(self.datas, self.difficulty)
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

            binaryDate = time.tm_year +" " +time.tm_month +" " +time.tm_day +" " +time.tm_hour +" " +time.tm_minute
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
            guiTexts = {

                "texts": {

                    "ch": { "home": "", "pubkeys": "", "sns": "", "cons": "", "files": "", "peers": "", "help": "", "params": "" },
                    "de": { "home": "", "pubkeys": "", "sns": "", "cons": "", "files": "", "peers": "", "help": "", "params": "" },
                    "en": { "home": "Home", "pubkeys": "Public Keys", "sns": "Social Networks", "cons": "Console", "files": "Files", "peers": "Peers", "help": "Help Page", "params": "Parameters" },
                    "fr": { "home": "Menu", "pubkeys": "Clés Publiques", "sns": "Réseaux Sociaux", "cons": "Console", "files": "Fichiers", "peers": "Pairs", "help": "Page d'Aide", "params": "Paramètres" },
                    "jp": { "home": "", "pubkeys": "", "sns": "", "cons": "", "files": "", "peers": "", "help": "", "params": "" },
                    "it": { "home": "", "pubkeys": "", "sns": "", "cons": "", "files": "", "peers": "", "help": "", "params": "" },
                    "sp": { "home": "", "pubkeys": "", "sns": "Redes Sociales", "cons": "", "files": "", "peers": "", "help": "", "params": "" }

                }

            }
            guiWindow = {

                "icon": "",
                "title": "AyzeLYC Blockchain Node",
                "xSize": 1920,
                "ySize": 1080

            }
            logs = []

        gui = QVBoxLayout
        gui.resize(guiDatas.guiWindow["xSize"], guiDatas.guiWindow["ySize"])
        gui.setWindowIcon(guiDatas.guiWindow["icon"])
        gui.setWindowOpacity(1)
        gui.setWindowTitle(guiDatas.guiWindow["title"])

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
        socialNetworksButton.enable = False
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
                self.nodePeers = []
                self.nodePeers = chr(ord(open("peers.abpeers", "r+")) /ord(Blockchain.password) /ord(self.nodeConstants))
                self.bannedPeers = []
                self.bannedPeers = chr(ord(open("bannedpeers.abpeers")) /ord(Blockchain.password) /ord(self.nodeConstants))

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

Main.Blockchain.INIT

if keyboard.on_press_key("ctrl+alt+s") :

    Main.Blockchain.blockchainDatas["verifyingBlocks"] = 0
    Main.Blockchain.blockchainDatas["mining"] = 0
    Main.Internet.internetClient.icsocket.stop
    Main.Internet.internetServer.issocket.stop
    Main.Node.threading.stopAll
    Main.walletDatas.blockchainFile.write(Main.Blockchain.blockchainDatas.chain[(len(Main.Blockchain.blockchainDatas.chain)) -len(Main.walletDatas.blockchainFile) : len(Main.Blockchain.blockchainDatas.chain))])

if Main.Gui.stopButton.clicked

    Main.Blockchain.blockchainDatas["verifyingBlock"] = 0
    Main.Blockchain.blockchainDatas["mining"] = 0
    Main.Internet.internetClient.icsocket.close
    Main.Internet.internetServer.issocket.close
    Main.Node.threading.stopAll
    Main.Gui.stopAll
    Main.walletDatas.blockchainFile.write(Main.Blockchain.blockchainDatas.chain[(len(Main.Blockchain.blockchainDatas.chain)) -len(Main.walletDatas.blockchainFile)] : len(Main.Blockchain.blockchainDatas.chain))])
