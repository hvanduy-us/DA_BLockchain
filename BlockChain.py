import Libraries as lib
import Transactions as trans
import Block as block



def dump_blockchain (self):
    print ("Number of blocks in the chain: " + str(len (self)))
    for x in range (len(lib.TPCoins)):
        block_temp = lib.TPCoins[x]
        print ("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            trans.display_transaction(transaction)
        print ('--------------')
        print ('=====================================')