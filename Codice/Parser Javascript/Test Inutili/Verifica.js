// Campi da stampare
// blockNumber, transactionIndex, time, tx hash, nonce, from, 
// to, contractAddress, value, gasPrice, gas, gasUsed, status, input
i = 1000000
count = 0
sum = 0


for (i = 1000000; i <= 2756703; i++){
    if (i == 1500000 || i == 2000000 || i == 2500000){
        console.log(i)
    }
    sum = web3.eth.getBlock(i).transactions.length
    count = count + sum
}

console.log(count)

