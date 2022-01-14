
from web3 import Web3


url='https://kovan.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
contract_address='0x018Cad184808E41e64CB954742385bf2d006EFEc'
abi="""[
	{
		"inputs": [],
		"name": "retrieve",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "val",
				"type": "string"
			}
		],
		"name": "store",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""
chain_id=42
system_account='0xd675e5EE2eb011738EDDCF931a86beba52A0aB0f'
system_private_key='cb1f3a0cad12678bc14c3ff08c760c804ce558a161cc6d4f590af16da8e27c51'


web3 = Web3(Web3.HTTPProvider(url))
contract_address = web3.toChecksumAddress(contract_address)
contract = web3.eth.contract(address=contract_address, abi=abi)   


#get first data
data = contract.functions.retrieve().call()



#write new data
data ='test new 123345'
gas = contract.functions.store(data).estimateGas()
print('{:.18f}'.format(gas*web3.eth.gasPrice / 10**18))

transaction = contract.functions.store(data).buildTransaction({
    'chainId': chain_id,
    'gasPrice': web3.eth.gasPrice,
    'nonce': web3.eth.getTransactionCount(system_account)
})

signed_txn = web3.eth.account.signTransaction(transaction, system_private_key)
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print('tx_hash', tx_hash)

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print('tx_receipt',tx_receipt )

#get last data
data = contract.functions.retrieve().call()
print(data)
