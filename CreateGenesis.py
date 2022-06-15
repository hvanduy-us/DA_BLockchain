import Client as cl
import Libraries as lib
import Transactions as trans
import Block as block
import BlockChain as blchain


Dinesh = cl.Client()

t0 = trans.Transaction ("Genesis",Dinesh.identity,500.0)

block0 = block.Block()

block0.previous_block_hash = None
block0.Nonce = None

block0.verified_transactions.append(t0)

digest = hash (block0)
last_block_hash = digest



lib.TPCoins.append (block0)
blchain.dump_blockchain(lib.TPCoins)

