// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
i = 2000000
count = 0
for (i = 2000000; i <= 3000000; i++){
    if (i == 2100000 || i == 2200000 || i == 2300000 || i == 2400000 || i == 2500000 || i == 2600000 || i == 2700000 || i == 2800000 || i == 2900000){
        console.log(i)
        console.log(count)
    }
    sum = web3.eth.getBlock(i).transactions.length
    count = count + sum
}

console.log(count)

