import os
import sys
import random
import argparse as arg
import pyautogui as auto
from time import sleep
from instabot import Bot
from colorama import init, Fore

init(autoreset=True)


class Advertisement:
    warning = Fore.LIGHTYELLOW_EX + '<' + Fore.LIGHTBLACK_EX + '!' + Fore.LIGHTYELLOW_EX + '> '
    message = Fore.LIGHTBLACK_EX + '+' + Fore.LIGHTYELLOW_EX + '> '
    information = Fore.LIGHTYELLOW_EX + '<' + Fore.LIGHTBLACK_EX + 'data' + Fore.LIGHTYELLOW_EX + '> '
    end = Fore.LIGHTYELLOW_EX + '/' + Fore.LIGHTBLACK_EX + '>' + '/ '
    suggest = Fore.BLUE + '*' + Fore.LIGHTBLUE_EX + '> '
    step = Fore.LIGHTBLUE_EX + '<' + Fore.LIGHTBLACK_EX + '!' + Fore.LIGHTBLUE_EX + '> '


to_user = 'vanessa.rhd', 'lanarohades', 'ladies', 'katekirienko', \
       'xlightmoon.x', 'arigameplays', 'natalie.tananska'
random_msg = 'Helloooo', 'follow me honey',\
             'so cute', 'i love you', 'send me your best >;)'

parser = arg.ArgumentParser(usage='You can choose f and m but its most probably to get a ban account. '
                                  'You can stop process if you want with Ctrl + Shift + C')
parser.add_argument('f', default=0, help='follow mode (1 true/ 0 false)', type=int)
parser.add_argument('m', default=0, help='messages mode (1 true/ 0 false', type=int)
parser.add_argument('-to', help='user to follow or send dm to his followers', type=str,
                    default=to_user[random.choice(range(0, 6))])
parser.add_argument('-cm', help='custom message', type=str)
parser.add_argument('-os', default=0, help="""operative system:
                                    [1] windows
                                    [2] macos
                                    [3] linux""", type=int)
args = parser.parse_args()

if args.os == 1:
    os.system('cls')
elif args.os == 2 or args.os == 3:
    os.system('clear')
else:
    pass

banner1 = """
 ██▓  ▄████       ██▓    ▄▄▄       ███▄    █  ▄▄▄▄    ▒█████  ▄▄▄█████▓     def see_mysocial(social, my_name):
▓██▒ ██▒ ▀█▒     ▓██▒   ▒████▄     ██ ▀█   █ ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒           my_name = Mynor Estrada
▒██▒▒██░▄▄▄░     ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░           social = {
░██░░▓█  ██▓     ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██░█▀  ▒██   ██░░ ▓██▓ ░                      'yt':'GlandesMates',
░██░░▒▓███▀▒ ██▓ ░██████▒▓█   ▓██▒▒██░   ▓██░░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░                      'github:'GlandesMates'
░▓   ░▒   ▒  ▒▓▒ ░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░              {
 ▒ ░  ░   ░  ░▒  ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░▒░▒   ░   ░ ▒ ▒░     ░               print(my_name)
 ▒ ░░ ░   ░  ░     ░ ░    ░   ▒      ░   ░ ░  ░    ░ ░ ░ ░ ▒    ░                       for i in social:
 ░        ░   ░      ░  ░     ░  ░         ░  ░          ░ ░                                print(i + ': ', social[i])
              ░                                    ░                        see_mysocial()
                #Use -h command to see all options
"""
print('\n\n')
colors = Fore.LIGHTBLUE_EX, Fore.BLUE, Fore.CYAN, Fore.LIGHTMAGENTA_EX
for banner in banner1:
    print(random.choice(colors) + banner, end='')
    sys.stdout.flush()
    sleep(0)
bot = Bot(
    unfollow_delay=1, follow_delay=1, filter_private_users=True,
    filter_users_without_profile_photo=True, filter_verified_accounts=True, message_delay=1
)
print('\n' + Advertisement.warning + Fore.CYAN +
      ' After this, you need to delete the session and cookies archives, and you can change the users list''\n''\n')

user = input(Advertisement.step + Fore.WHITE + '\tUsername: ')
pwd = input(Advertisement.step + Fore.WHITE + '\tPassword: ')
print('\n')
bot.login(username=user, password=pwd)

if args.f == 1 and args.m == 0:
    id_victim = bot.get_user_id_from_username(args.to)
    if args.to:
        print('\n')
        try:
            bot.follow_followers(
                id_victim, nfollows=int(input(
                    '\tMax follows: '
                ))
            )
        except KeyboardInterrupt or Exception as e:
            if e is True:
                print(f'Error: {e}')
            else:
                print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')
    else:
        print('\n')
        id_victim = bot.get_user_id_from_username(
            random.choice(to_user)
        )
        print(
              '\n' + Advertisement.message +
              Fore.LIGHTGREEN_EX + 'Followers from user: ' +
              str(
                bot.get_username_from_user_id(
                    id_victim
                )
              )
        )
        print('\n')
        try:
            bot.follow_followers(
                id_victim, nfollows=int(input(
                    '\tMax follows: '
                ))
            )
        except KeyboardInterrupt or Exception as e:
            if e is True:
                print(f'Error: {e}')
            else:
                print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')
    bot.unfollow_non_followers()

elif args.m == 1 and args.f == 0:
    if args.to:
        id_victim = bot.get_user_id_from_username(args.to)
        followers = bot.get_user_followers(id_victim, nfollows=int(input(f'\tGet custom users list from {args.to}: ')))
        if args.cm:
            try:
                bot.send_messages(followers, args.cm)
            except KeyboardInterrupt or Exception as e:
                if e is True:
                    print(f'Error: {e}')
                else:
                    print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')
        else:
            try:
                bot.send_messages(followers, random.choice(random_msg))
            except KeyboardInterrupt or Exception as e:
                if e is True:
                    print(f'Error: {e}')
                else:
                    print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')
    else:
        id_victim = bot.get_user_id_from_username(
            random.choice(to_user)
        )
        print(
            '\n' + Advertisement.message +
            Fore.LIGHTGREEN_EX + 'Followers from user: ' +
            str(
                bot.get_username_from_user_id(
                    id_victim
                )
            )
        )
        followers = bot.get_user_followers(id_victim, nfollows=int(input(f'\tGet custom users list from {args.to}: ')))
        if args.cm:
            try:
                bot.send_messages(
                    followers,
                    args.cm
                )
            except KeyboardInterrupt or Exception as e:
                if e is True:
                    print(f'Error: {e}')
                else:
                    print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')
        else:
            try:
                bot.send_messages(followers, random.choice(random_msg))
            except KeyboardInterrupt or Exception as e:
                if e is True:
                    print(f'Error: {e}')
                else:
                    print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')

elif args.f == args.m:
    if args.to and not args.cm:
        MaxUsersFromVictim = int(input(f'\tGet followers from {args.to}: '))
        id_victim = bot.get_user_id_from_username(args.to)
        followers = list(bot.get_user_followers(id_victim, nfollows=MaxUsersFromVictim))
        for each_follower in followers:
            try:
                bot.follow(each_follower)
                bot.send_message(random.choice(random_msg), each_follower)
            except KeyboardInterrupt or Exception as e:
                if e is True:
                    print(f'Error: {e}')
                else:
                    print('\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user')


def writer(text, time):
    auto.typewrite(text)
    auto.press('enter')
    sleep(time)


if args.os == 1:
    writer('start', 2)
    writer('cd config', 3)
    writer('DEL ' + user + '_uuid_and_cookie.json', 0)
    writer('DEL ' + user + '.checkpoint', 0)
elif args.os == 2 or args.os == 3:
    auto.hotkey('ctrl', 'shift', 'n')
    sleep(2)
    writer('cd config', 0)
    writer('rm' + user + '_uuid_and_cookie.json', 0)
    writer('rm' + user + '.checkpoint', 0)
else:
    print(
        Advertisement.warning +
        Fore.RED +
        '\n\tYou dont specify an OS so...'
        '\n\tyou had to delete by yourself the archives in config file'
    )
print(
    Advertisement.message +
    Fore.CYAN +
    '\n\t\t\t\tSee you later influencer ;)\n'
)
