def countLines(name):
    result = 0
    import os

    if not os.path.exists(name):
        print(name, 'is not found.')
        return None
        
    if not os.path.isfile(name):
        print(name, 'is not a file.')
        return None
        
    with open(name) as f:
        result = len(f.readlines())
    
    return result

def countChars(name):
    result = 0
    import os

    if not os.path.exists(name):
        print(name, 'is not found.')
        return None 
        
    if not os.path.isfile(name):
        print(name, 'is not a file.')
        return None
        
    with open(name) as f:
        result = len(f.read())
    
    return result

def test(name):
    print(countLines(name), 'lines')
    print(countChars(name), 'chars')

if __name__ == '__main__':
    print('My __name__ is "__main__"!')
    
    