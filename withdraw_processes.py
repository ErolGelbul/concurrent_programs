import multiprocessing as mp

def mp_withdraw(amount, balance):
    if (balance.value >= amount):
        print("{} sees balance {}, withdraws {}".format(mp.current_process(),
                                                        balance.value,
                                                        amount))
        balance.value = balance.value - amount 
        return True
    return False

def mp_withdraw_mary(balance):
    amount = balance.value//2
    if (balance.value >= amount):
        print("{} sees balance {}, withdraws {}".format(mp.current_process(),
                                                        balance.value,
                                                        amount))
        balance.value = balance.value - amount 
        return True
    return False

def make_initial_balance():
    balance = mp.Value('i', 100) # 'i' refers to the type, it's an integer
    return balance

def make_processes():
    balance = make_initial_balance()
    transaction_john = mp.Process(target=mp_withdraw, args=(-10, balance), name='John')
    transaction_paul = mp.Process(target=mp_withdraw, args=(20, balance), name='Paul')
    transaction_mary = mp.Process(target=mp_withdraw_mary, args=(balance,), name='Mary')
    return transaction_john, transaction_paul, transaction_mary, balance