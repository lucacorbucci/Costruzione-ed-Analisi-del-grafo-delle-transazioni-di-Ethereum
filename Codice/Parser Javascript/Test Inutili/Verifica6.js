// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
count = 0
for (i = 1400000; i <= 1500000; i++){
    if (i == 1410000 || i == 1420000 || i == 1430000 || i == 1440000 || i == 1450000 || i == 1460000 || i == 1470000 || i == 1480000 || i == 1490000){
        console.log(i)
        console.log(count)
    }
    sum = web3.eth.getBlock(i).transactions.length
    count = count + sum
}

console.log(count)

