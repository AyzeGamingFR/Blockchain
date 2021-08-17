import json

class Blockchain:
  
  def init(self):
    self.actual_transactions = {}
    self.blockchain = {}
    self.blockchainnumber = 0
    self.blocks = 0
    self.nodes = set()
    
  def create_transaction(self, sender, receiver, coins, message):
    self.previoushash = self.previoushash
    self.coins = coins
    self.message = message
