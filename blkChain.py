blkChain = []


def get_last_blk_chain_value():
    return blkChain[-1]


def add_value(txn_amt, last_txn_value=[1]):
    """   test comment """
    blkChain.append([last_txn_value, txn_amt])


#   print(blkChain)


def get_transaction_amt():
    return float(input("enter amt: "))


def get_user_choice():
    return input('Choice: ')


def print_blkchain_elements():
    for block in blkChain:
        print(block)


def manipulate():
    blkchain_len = len(blkChain)
    if blkchain_len > 0:
        idx_value = int(input("which idx you want to change ? length of chain is: " + str(blkchain_len) ))
        if idx_value <= blkchain_len:
            blkChain[idx_value - 1] = [float (input("Enter your value: "))]
            print(blkChain)


def verify_chain1():
    if len(blkChain) > 0:
        loop_idx = 0
        for block in blkChain:
            #print("current block  ",block ," idx value ", loop_idx, " current at loop idx ",  block[0] ,  " previous block ", blkChain[loop_idx-1])
                if loop_idx ==0 :
                    loop_idx +=1
                    continue
                elif block[0] != blkChain[loop_idx -1]:
                    print("bad block chain at idx ", block[0] ,  blkChain[loop_idx-1])
                    print("bad block chain at idx ", loop_idx)
                loop_idx += 1
                    #break


def verify_chain():
    if len(blkChain) > 0:
        loop_idx = 0
        for block in blkChain:
            #print("current block  ",block ," idx value ", loop_idx, " current at loop idx ",  block[0] ,  " previous block ", blkChain[loop_idx-1])
            if loop_idx ==0 :
                loop_idx +=1
                continue
            elif block[0] != blkChain[loop_idx -1]:
                return False
            loop_idx += 1
    return True
            #break


while True:

    print('Select 1 2 m v q for add new block: ')

    user_input = get_user_choice()
    if user_input == '1':
        if len(blkChain) >= 1:
            add_value(get_transaction_amt(), get_last_blk_chain_value())
        else:
            add_value(get_transaction_amt())
    elif user_input == '2':
        print_blkchain_elements()
    elif user_input == 'q':
        break
    elif user_input == 'm':
        manipulate()
    elif user_input == 'v':
            print(" Blkcain valid: ",verify_chain() )

    else:
        print('invalid input')
