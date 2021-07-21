import time
from colored import fg, attr
import os
import threading
# testing the colored lib, first time using it...
# unoptimized code but who cares ¯\_(ツ)_/¯


def clean():
    os.system('cls')




def banner(): # No judgment...
    clean()
    print('\n\t\t\t\t%s  ██▒   █▓▓█████  ███▄    █  ▒█████   ███▄ ▄███▓ %s' % (fg(82), attr("reset")))
    print('\t\t\t\t%s ▓██░   █▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒ %s' % (fg(83), attr("reset")))
    print('\t\t\t\t%s  ▓██  █▒░▒███   ▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░  %s' % (fg(84), attr("reset")))
    print('\t\t\t\t%s   ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒██    ▒██   %s' % (fg(85), attr("reset")))
    print('\t\t\t\t%s    ▒▀█░  ░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒ %s' % (fg(86), attr("reset")))
    print('\t\t\t\t%s   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ %s' % (fg(86), attr("reset")))
    print('\t\t\t\t%s   ░ ░░   ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░ %s' % (fg(86), attr("reset")))
    print('\t\t\t\t%s      ░     ░  ░         ░     ░ ░         ░     %s' % (fg(86), attr("reset")))
    print('\t\t\t\t\t%s  ============================ %s' % (fg(45), attr("reset")))
    print('\t\t\t\t\t%s   The Most Powerful Stresser %s' % (fg(93), attr("reset")))
    print('\t\t\t\t\t%s  ============================ %s' % (fg(45), attr("reset")))
    print('\n\n')

def stresser():
    banner()
    ip = input("[%s+%s] - %sEnter your target's ip :%s " % (fg(93), attr("reset"), fg(93), attr("reset")))
    port = input("[%s+%s] - %sEnter your target's port :%s " % (fg(93), attr("reset"), fg(93), attr("reset")))
    target = f'{ip}:{port}'
    method = input("[%s+%s] - %sEnter your desired method :%s " % (fg(93), attr("reset"), fg(93), attr("reset")))
    duration = int(input("[%s+%s] - %sEnter your desired attack duration (seconds) :%s " % (fg(93), attr("reset"), fg(93), attr("reset"))))
    banner()
    print('[%s~%s] - %sStarting Attack for %s seconds on %s%s%s\n\n' % (fg(93), attr("reset"), fg(93), duration, fg(82), target, attr("reset")))
    time.sleep(1)
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            break
        else:
            print('%s~ %s3GB Sent To %s%s%s' % (fg(82), fg(93), fg(82), target, attr("reset")))
            time.sleep(5)
        
    banner()
    input("[%s~%s] - %sAttack Finished, press ENTER to go back %s" % (fg(93), attr("reset"), fg(93), attr("reset")))
    main()

def methods():
    banner()
    input('''
%s~ %sHTTP
%s~ %sDSTAT
%s~ %sCF-BYPASS\n\nPress ENTER to go back :%s ''' % (fg(82), fg(93), fg(82), fg(93), fg(82), fg(93), attr("reset")))
    main()

def main():
    os.system('title Venom ^| https://github.com/izikut/Venom')
    banner()
    choice = input('''
[%s1%s] - %sAttack%s
[%s2%s] - %sMethods%s

%s>>>%s ''' % (fg(82), attr("reset"), fg(93), attr("reset"), fg(82), attr("reset"), fg(93), attr("reset"), fg(82), attr("reset")))
    if choice == "1":
        stresser()
    if choice == "2":
        methods()
    else:
        main()

main()

