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

parser = arg.ArgumentParser(usage='You can choose f and m but its most probably to get a ban account. '
                                  'You can stop process if you want with Ctrl + Shift + C')
parser.add_argument('f', default=0, help='follow mode (1 true/ 0 false)', type=int)
parser.add_argument('m', default=0, help='messages mode (1 true/ 0 false)', type=int)
parser.add_argument('s', default=0, help='scrapping on instagram (1 true/ 0 false)', type=int)
parser.add_argument('t', help='be a stalker on instagram (1 true/ 0 false)', type=int)
parser.add_argument('-n', default=0, help='configure new accounts (upload photo, video, etc)')
parser.add_argument('-to', help='user to follow or send dm to his followers', type=str,
                    default=to_user[random.choice(range(0, 6))])
parser.add_argument('-fo', help='max users to get: )', type=int)
parser.add_argument('-cm', help='custom message', type=str)
parser.add_argument('--media', help='send photo to users as dm (enter filepath)', type=str)
parser.add_argument('--profile', help='send a profile to users as dm')
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
try:
    bot.login(username=user, password=pwd)
except Exception as e:
    print(f'\tCan not login with {user} for cause:\n {e}')

if args.to == 1:
    her_user = args.to
else:
    her_user = random.choice(to_user)


def user_or_error(error):
    if error is True:
        print(e)
    else:
        print(
            '\n\t\t' + Advertisement.warning + Fore.RED + 'Process interrupted by user'
        )


def load_archives(load, pic):
    try:
        load
    except Exception as e:
        if e is True:
            raise e
        else:
            print(f'\tFile does not exist {pic}')


if args.n:
    print("""
    You select the mode -n,
    what do you want to do?:
    ----------------------
    {0} Profile picture
    {1} Upload photo
    {2} Upload video
    {3} Upload story photo
    {4} All
    ----------------------
          """)
    uploader = int(input('\t\t'))
    if uploader == 1:
        pic_upl = input('\tPhoto path: ')
        load_archives(bot.upload_photo(pic_upl), pic_upl)
    elif uploader == 2:
        vid_upl = input('\tVideo path: ')
        load_archives(bot.upload_video(vid_upl), vid_upl)
    elif uploader == 3:
        story_pic = input('\tStory photo path: ')
        load_archives(bot.upload_story_photo(story_pic), story_pic)
    elif uploader == 0:
        prof_pic = input('\tProfile picture path: ')
        load_archives(bot.api.configure_photo(prof_pic), prof_pic)
    elif uploader == 4:
        pic_upl = input('\tPhoto path: ')
        vid_upl = input('\tVideo path: ')
        story_pic = input('\tStory photo path: ')
        prof_pic = input('\tProfile picture path: ')
        load_archives(bot.upload_photo(pic_upl), pic_upl)
        load_archives(bot.upload_video(vid_upl), vid_upl)
        load_archives(bot.upload_story_photo(story_pic), story_pic)
        load_archives(bot.api.configure_photo(prof_pic), prof_pic)
    else:
        pass
else:
    pass

if args.m == 1:
    id_user = bot.get_user_id_from_username(her_user)
    if args.fo:
        followers = bot.get_user_followers(id_user, args.fo)
    else:
        followers = bot.get_user_followers(id_user)
    for each_user in followers:
        try:
            bot.send_messages(user_ids=each_user, text=args.cm)
            if args.media:
                bot.send_photo(her_user, args.media)
            else:
                pass
            if args.profile:
                id_prof = bot.get_user_id_from_username(args.profile)
                bot.send_profile(id_prof, her_user)
            else:
                pass
        except KeyboardInterrupt or Exception as e:
            user_or_error(e)
elif args.cm == args.to:
    id_user = bot.get_user_id_from_username(her_user)
    if args.fo:
        followers = bot.get_user_followers(id_user, args.fo)
    else:
        followers = bot.get_user_followers(id_user)
    try:
        for each_user in followers:
            bot.follow(each_user)
            bot.send_message(args.cm, each_user)
            if args.media:
                bot.send_photo(her_user, args.media)
            else:
                pass
            if args.profile:
                id_prof = bot.get_user_id_from_username(args.profile)
                bot.send_profile(id_prof, her_user)
            else:
                pass
            if args.media:
                bot.send_photo(her_user, args.media)
            else:
                pass
            if args.profile:
                id_prof = bot.get_user_id_from_username(args.profile)
                bot.send_profile(id_prof, her_user)
            else:
                pass
    except KeyboardInterrupt or Exception as e:
        user_or_error(e)
if args.s == 1:
    print(f"""
    [1] Get messages from {user}
    [2] Get followers info from {her_user}
    Coming soon...
    --------------------------------------
    """)
    scraper = int(input('\t\t'))
    if scraper == 1:
        bot.get_messages()
    elif scraper == 2:
        id_user = bot.get_user_followers(her_user)
        if args.fo:
            followers = bot.get_user_followers(id_user, args.fo)
        else:
            followers = bot.get_user_followers(id_user)
        count = 0
        for users_info in followers:
            print(bot.get_user_info(users_info))
            count += 1
            if count == args.fo:
                print('\tUsers information process finished...')
                break
if args.to == 1:
    print(f"""
    [1] Send likes to followers from {her_user}
    Coming soon...
    -------------------------------------------
    """)
    stalker = int(input('\t\t'))
    if stalker == 1:
        if args.to == 1 and args.fo:
            count = 0
            id_user = bot.get_user_id_from_username(her_user)
            followers = bot.get_user_followers(id_user, args.fo)
            for each_user in followers:
                bot.like_user(each_user)
                count += 1
                if count == args.fo:
                    break
bot.logout()


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
