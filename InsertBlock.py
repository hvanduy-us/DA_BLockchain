import Block as block
import Transactions as trans
import CreateGenesis as creaG
import Miner as mine
import Libraries as lib

last_transaction_index = 0
block = block.Block()

for i in range(3):
    temp_transaction = trans.transactions[last_transaction_index]
# validate transaction
    # if valid
    block.verified_transactions.append (temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = creaG.last_block_hash
block.Nonce = mine.mine (block, 2)
digest = hash (block)
lib.TPCoins.append (block)
last_block_hash = digest