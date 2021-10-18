import hashlib
import PySide6.QtCore
import random
import socket
import string
import threading
import time

class main :
    
    logs = []
    
    class algorithms :
        
        class leya :
            
            def encrypt(self, datas) :
                
                self.datas = datas
                self.epassword = blockchain.constantsdigitresult
                
            def brute_force(self, datas) :
                
                
                
        class sha256 :
            
            def hash(datas) :
                
                
                
            def brute_force(hash) :
                
                
                
    class blockchain :
        
        Blockchain = {"chainId": 0, "chainBlks": [], "chainTxs": [], "chainHoldrs": {}, "chainTtalFees": 0}
        constantsdigitresult = string.digits("AyzeLYC") *string.digits("Blockchain") *string.digits("Bitcoin") *string.digits("Litecoin") *string.digits("Marscoin") *string.digits("Mooncoin") *string.digits("Altcoin") *string.digits("Cryptocurrency")
        
        def create_block(self, prevhash, transactions, reward, minerAddress) :
            
            self.phash = prevhash
            self.time = `"year": ${time.tm_year}, "month": ${time.tm_mon}, "day": ${time.tm_mday}, "hour": ${time.tm_hour}, "minute": ${time.tm_min}, "second": ${time.tm_sec}`
            self.txs = transactions
            self.fees = Blockchain["chainTotalFees"]
            self.reward = reward
            self.block = `{"prevhash": "${self.phash}", "time": { ${self.time} }, "txs": ${self.txs}, "fees": ${self.fees}, "reward": ${self.reward}}`
            algorithms.leya.encrypt(self.block, constantsdigitresult)
            
        def create_transaction(self, prevhash, from, to, coins, message, fees) :
            
            self.prvhash = prevhash
            self.from = from
            self.to = to
            self.coins = coins
            self.msg = message
            self.fees = fees
            
            if self.coins < Blockchain["chainHolders"[(self.from)]] :
                
                logs.append("The number of coins you want to send is higher than the number of coins you get !")
                
            else :
                
                if self.coins + self.fees < Blockchain["chainHolders"[(self.from)]] :
                    
                    logs.append("The number of coins you get is smaller than the number of coins you want to send + the mining fees !")
                    
                else :
                    
                    self.tx = '{"prevtxhash": "' +self.prvhash +'", "from": "' +self.from +'", "to": "' +self.to +'", "coins": ' +self.coins +', "msg": "' +self.msg +'", "fees": ' +self.fees +'}'
                    self.etx = string.ascii_letters(string.digits(self.tx) *string.digits(wallet.pubkeys[(self.from)["privkey"]]))
                    Blockchain["chainTxs"].append(self.tx)
                    
    class gui :
        
        
        
