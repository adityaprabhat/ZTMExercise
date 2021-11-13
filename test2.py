user1 = {
    'name':'Parker',
    'valid': True
}

user2 = {
    'name':'Tolliver',
    'valid': False
}


def authenticated(func):
    def wrapper(*args,**kwargs):
        if args[0]['valid']:
            return func(*args,**kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print(f'Message has been sent to')

message_friends(user1)