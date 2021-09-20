function main() {
    
    function INIT() {
        
        Blockchain.blockchainDatas.chain["blocks"] = null;
        Internet.internetServer.issocket.start("", 8448)
        Internet.internetClient.icsocket.connect(Blockchain.blockchaibDatas.peers, 8448)
        
    };
    void Algorithms() {
        
        
        
    };
    void Blockchain() {
        
        void blockchainDatas = {
            
            var blockchain = {"peers": [], "blocks": [], "blocksnv": []}
            
        };
        function create_block(var blockPrevHash, blockNumber, blockTransactions, blockFees, blockMessage) {
            
            var self = null
            
            self.previousBlockHash = blockPrevHash
            self.number = blockNumber
            self.transactions = blockTransactions
            self.fees = blockFees
            self.message = message
            
            self.datas = "{'prevhash': 'self.previousBlockHash'}"
            self.hash = Algorithms.leya.encrypt(self.datas, blockchainDatas.blockchain["difficulty"])
            self.minedBlock = Algorithms.leya.bruteForce(self.hash)
            Internet.internetServer.send(self.minedBlock)
            
        };
        
    };
    
};

main.INIT();
