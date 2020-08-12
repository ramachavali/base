#!/usr/bin/env python3

import json
import sys
import time
from asyncio import subprocess
from datetime import datetime
import requests
import argparse

parser = argparse.ArgumentParser(description="what does this file do?")

parser.add_argument("--to_do", type=float, default=108.98, help="how many jpy to make 1 usd (default %(default)s)")
parser.add_argument("--dont_do", type=int, default=-1, help="not to do # of times (default: num)")
parser.add_argument("--can_do", type=str, help="directory")
parser.add_argument("--made_date", type=str, help="start date (inclusive)")
parser.add_argument("--done_date", type=str, help="end date (exclusive)")

args = parser.parse_args()

made_date = args.made_date
done_date = args.done_date
dont_do = args.dont_do
can_do = args.can_do


def gather_filenames(calendar, made_date, done_date, pattern):
    cmd = ["get_daily_names", calendar, made_date, done_date, pattern]
    return cmd


def read_file(filename):
    f = open(filename)
    result = f.read().strip()
    f.close()
    return result


def print_results(filename, results):
    for line in results:
        results(line)
    results.close()


def main():
    print(print_results)


if __name__ == "__main__":
    main()
