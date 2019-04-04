// Script utilizzato per estrarre le transazioni dalla blockchain di Ethereum
// Deve essere attivo Geth per avviare questo script e prendere i dati 
// Geth deve aver già sincronizzato in locale la blockchain.
// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
i = 0
for (i = 0; i <= 2500000; i++){

    Block = web3.eth.getBlock(i);
    blockNumber = Block.number
    blockTime = Block.timestamp
    transactions = Block.transactions;
    for (j = 0; j < transactions.length; j++) {
        receipt = web3.eth.getTransactionReceipt(transactions[j]);
        trx = web3.eth.getTransaction(transactions[j])

        index = receipt.transactionIndex
        hash = receipt.transactionHash
        nonce = trx.nonce
        value = trx.value;
        gasPrice = trx.gasPrice
        gas = trx.gas
        gasUsed = receipt.gasUsed
        mittente = receipt.from
        destinatario = receipt.to
        contractAddress = receipt.contractAddress
        var status;
        
        if (gas == gasUsed){
            if (trx.input.indexOf(help) == -1){
                if (debug.traceTransaction(transactions[j]).failed == true) {
                    status = "0"
                }
                else {
                    status = "1"
                }
            }
            else{
                status = "1"
            }
        }
        else {
            status = "1"
        }
        
        input = trx.input

        console.log(blockNumber + "," + index + "," + blockTime + "," + hash + "," + nonce + "," + mittente + "," + destinatario + "," + contractAddress + "," + value + "," + gasPrice + "," + gas + "," + gasUsed + "," + status + "," + input)

    }
}

