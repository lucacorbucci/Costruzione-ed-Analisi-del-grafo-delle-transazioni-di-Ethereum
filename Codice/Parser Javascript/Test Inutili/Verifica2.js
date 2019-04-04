// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
i = 1000000
count = 0
for (i = 1000000; i <= 2000000; i++){
    if (i == 1100000 || i == 1200000 || i == 1300000 || i == 1400000 || i == 1500000 || i == 1600000 || i == 1700000 || i == 1800000 || i == 1900000){
        console.log(i)
        console.log(count)
    }
    sum = web3.eth.getBlock(i).transactions.length
    count = count + sum
}

console.log(count)

