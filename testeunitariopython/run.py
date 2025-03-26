
def meu_log(func):
    def wrapper(*args, **kwargs):
        print("Iniciando " + func.__name__+"...")
        response = func(*args, **kwargs)
        print("Finalizando "+func.__name__+"...")
        return response
    return wrapper

@meu_log
def soma(a, b):
    return a + b


soma(2, 3)
