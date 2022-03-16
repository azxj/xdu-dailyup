import argparse

from steps import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, required=True, help='学号')
    parser.add_argument('--password', type=str, required=True, help='密码')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    cookies = login(args.username, args.password)
    upload(cookies)


if __name__ == '__main__':
    main()
