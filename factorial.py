def factorial(f):
    memory = {}

    def inner(num):
        if num not in memory:         
            memory[num] = f(num)
        return memory[num]
  
    return inner

@factorial
def facto(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * facto(num-1)