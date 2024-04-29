# 符文合并  
from web3 import Web3

import math
import json

rpc         = 0
chainId     = 1030
newcfxsContract = '0xd3a4d837e0a7b40de0b4024fa0f93127dd47b8b8'

rpcList = [
    "https://evm.confluxrpc.com",
    'https://conflux-espace-public.unifra.io',
]
rpcUrl = rpcList[rpc]  

myAddr = ''
myKey = ''

# 连接
w3 = Web3(Web3.HTTPProvider(rpcUrl))

# 检查连接
if not w3.is_connected():
    print("connect fail")
    exit(0)

newfile = open('./newcfxs.json')
newabi = json.load(newfile)

newcontract = w3.eth.contract(address= w3.to_checksum_address(newcfxsContract), abi=newabi)
# 读取cfxIds
idfile = open('./id_addr')
idLines = idfile.read().splitlines()

myIds = idLines[0:]

batch = 24 # 一次转移个数 最多24
count = math.ceil(len(myIds)/batch)
x = 0

while x < count:
    print(f'transfer: {x}')
    try:
        nonce    = w3.eth.get_transaction_count(myAddr)
        gasPrice = math.floor(w3.eth.gas_price / 1000000000)
        print(f'gas:{gasPrice}')
        if gasPrice > 100:
            print('skip')
            continue
        
        indexFrom =  x * batch
        indexTo   = indexFrom + batch
        
        sliceList = myIds[indexFrom : indexTo]
        walletList = []
        totalAmount = 0
        for idAmount in sliceList:
            item = idAmount.split(",")
            if int(item[0]) > 0 and len(item) == 2:
                walletList.append(int(item[0]))
                totalAmount += int(item[1])
            if int(item[0]) > 0 and len(item) == 1:
                walletList.append(int(item[0]))
                totalAmount += 1
        if len(walletList) == 0:
            break

        outPut = [
            [
                myAddr,
                totalAmount,
                ""
            ]
        ]
        print(walletList, outPut)
        # 创建交易
        tranDict = {
            'nonce':                nonce,
            'gasPrice':             w3.to_wei(gasPrice * 1.05, 'gwei'),
            'from':                 w3.to_checksum_address(myAddr),
            'value':                0,
            'gas':                  2300000,
            #  'gasPrice': w3.toWei('50', 'gwei'),
            #   'chainId':              chainId
        }
        
        buildParam = newcontract.functions.processTransaction(walletList, outPut).build_transaction(tranDict)
        tx = w3.eth.account.sign_transaction(buildParam, myKey)
    
        txHash = w3.eth.send_raw_transaction(tx.rawTransaction)
        # print('tranfer send success')
        tx_receipt = w3.eth.wait_for_transaction_receipt(txHash, 300, 2)
        print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")
        x += 1
    except Exception as e: 
        print(str(e))
      
   

