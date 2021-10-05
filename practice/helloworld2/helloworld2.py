def greetings(input, print):
    """Функция приветствия"""
    s=input('What is your name?')
    if len(s)>0 and ord('A') <= ord(s[0]) <= ord('Z') and \
        all(map(lambda x: ord('a') <= ord(x) <= ord('z'), s[1:])):
        print (f'Hello, {s}!')
    else:
        print('Hello, World!')