def exemplo(*args):
    print(args)

exemplo('a', 'b','c')

def dicionario(**kwargs):
    print(kwargs)

dicionario(nome='gabriel', email='gabriel@4llinux.com')

def juntos(*args, **kwargs):
    print(args)
    print(kwargs)

juntos('a', 'b','c')