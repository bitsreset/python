
def read_text( prompt ):
    '''
    Displays a prompt and read in a string of text.
    Keyboard interrupts ( Ctrl + C ) are ignored
    returns a string containing the string input by the user. 
    '''
    while True:#repeat forever
        try:
            result = input( prompt ) # read the input
            # if we get here, no exception was raised
            # break out of the loop
            break
        except KeyboardInterrupt:
            # if we get here, the user pressed Ctrl+C
            print('Please enter text')
    #print('result=',result)
    return result

def read_float( prompt ):
    '''
    Displays a prompt and read in a number.
    Keyboard interrupts ( Ctrl + C ) are ignored.
    Invalid numbers are rejected.
    returns a float containing the value input by the user.
    '''
    while True: # repeat forever
        try:
            input_text = read_text( prompt ) # read the input
            type( input_text )
            result = float( input_text )
            # if we get here, no exception was raised
            # break out of the loop
            break
        except ValueError:
            # if we get here, the user entered an invalid number
            print('Please enter a number')
    
    # return the result
    return result
