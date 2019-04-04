// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
i = 2500000
count = 0
sum = 0
for (i = 2500000; i <= 2756703; i++){
    
    sum = web3.eth.getBlock(i).transactions.length
    count = count + sum
}

console.log(count)

