a// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
i = 4369748
for (i = 4369748; i <= 4370000; i++){

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

            if (contractAddress != "0x1cc2c9240385446bbdb2df7d5c89647303c073e1" && destinatario != "0x1cc2c9240385446bbdb2df7d5c89647303c073e1" && destinatario != "0x8a187d5285d316bcbc9adafc08b51d70a0d8e000" && destinatario != "0xdf6ef343350780bf8c3410bf062e0c015b1dd671" && destinatario != "0x6090a6e47849629b7245dfa1ca21d94cd15878ef" && destinatario != "0x318f2bee1f51076749d2c9a6f22f306567b60df2" &&  destinatario != "0x8d12a197cb00d4747a1fe03395095ce2a5cc6819" &&  destinatario != "0x8bfe5ebb128ee82f4ba80f56bb32409cc87bc6fb" && destinatario != "0xc22462d4bc50952b061c9e6c585fdd9a04d0d75a" && destinatario != "0x8d12a197cb00d4747a1fe03395095ce2a5cc6819" && destinatario != "0x377dfa7bab23a798ca1fa0923bcd4d4ef2184d85" && destinatario != "0x78d72b75abf4eae76121fdb39fbe5bd5ed39ad3a" && destinatario != "0x2cac6e4b11d6b58f6d3c1c9d5fe8faa89f60e5a2" && destinatario != "0x693b8e1dc2265838da12a7c01f121b5cd0008b6a" && destinatario != "0x2d4c968b6ede2b6706f6d9bec48c2e2e8ad425fb" && destinatario != "0xf45717552f12ef7cb65e95476f217ea008167ae3" && destinatario != "0xe414716f017b5c1457bf98e985bccb135dff81f2" && destinatario != "0x7fd85d1fc04087b3d9d1e610410989191c09b973" && destinatario != "0xb21f8684f23dbb1008508b4de91a0aaedebdb7e4"){
                if (debug.traceTransaction(transactions[j]).failed == true) {
                    status = "0"
                }
                else {
                    status = "1"
                }
            }
            else{
                status = "0"
            }
            
        }
        else {
            status = "1"
        }
        
        input = trx.input

        console.log(blockNumber + "," + index + "," + blockTime + "," + hash + "," + nonce + "," + mittente + "," + destinatario + "," + contractAddress + "," + value + "," + gasPrice + "," + gas + "," + gasUsed + "," + status + "," + input)

    }
}