# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    
    choice = input()

    if 'I'in(choice):
        # input from keyboard
        return (input().rstrip(), input().rstrip())
    else:
        with open('tests/06', "r") as fails:
        #     n = int(fails.readline())
        #     data = list(map(int, fails.readline().split()))
            return (fails.readline().rstrip(),fails.readline().rstrip())
            # return (fails.readline(), fails.readline())

    # return (input().rstrip(), input().rstrip())
    # return ("aba", "abacaba")

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    listik = []
    mejik_namber = 7
    mejik_mef = lambda s: sum(ord(c) for c in s)
    
    pattern_hash = mejik_mef(pattern) * mejik_namber
    
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]
        substring_hash = mejik_mef(substring) * mejik_namber
        
        if substring_hash == pattern_hash:
            if substring == pattern:
                listik.append(i)
    
    # and return an iterable variable
    return listik


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
