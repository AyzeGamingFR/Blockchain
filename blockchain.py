class Blockchain:
  
  def init(self):
    self.actual_transactions = {}
    self.blockchain = {}
    self.blockchainnumber = 0
    self.blocks = 0
    self.nodes = set()
