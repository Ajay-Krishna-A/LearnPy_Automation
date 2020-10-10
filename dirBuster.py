# DirBuster

try:
    import sys                  # used to take command line arguments and exit when needed.
    import requests             # used to make HTTP requests


    rHost = sys.argv[1]         # remote host <url>
    wordlist = sys.argv[2]      # wordlist <dictionary>


    print('Checking for valid url...', end=" ")

    try:

        response = requests.get(rHost).status_code

        if response == 200 :

            print (' Done')

        else :

            print ( "404 - Not found.")
            sys.exit(1)

    except : 

        print ( "\nError : Cannot reach the rHost ! " )
        sys.exit(1)

    try :

        print("Parsing the wordlist ... ", end=" ")

        with open(wordlist) as file :

            to_check = file.read().strip().split('\n')

            print ( " Done " )
            print ( "Total Paths to check : ", str(len(to_check)) )


    except IOError :
        
        print('[!] Failed...')
        print('Error : Failed to read Specified file - Wordlist')
        sys.exit(1)

        
    def checkpath(path):
        
        try : 
            
            response = requests.get(rHost + '/' + path ).status_code

            if ( response == 200 ):

                print('[*] Valid path found : ', path)
            

                
        
        except Exception:
            
            print('[!] Failed...')   
            print('Error : An unexpected error occured ...') 
            sys.exit(1)
            
      #  iterating over the list of paths...

    print('\n\n Beginning scan .... ')
    
    for i in range(len(to_check)) :
        checkpath(to_check[i])
        
    print('\n Scan complete ...') 




except KeyboardInterrupt :
    
    print('Error : User interrupted scan ... ')
    sys.exit(1)
