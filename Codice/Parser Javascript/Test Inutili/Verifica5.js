// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
count = 0
for (i = 1410000; i <= 1411000; i++){
    if (i == 1410100 || i == 1410200 || i == 1410300 || i == 1410400 || i == 1410500 || i == 1410600 || i == 1410700 || i == 1410800 || i == 1410900){
        console.log(i)
        console.log(count)
    }
    sum = web3.eth.getBlock(i).transactions.length
    count = count + sum
}

console.log(count)

