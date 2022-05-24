#!/usr/bin/env python

import csv
from collections import defaultdict
from datetime import datetime

graph = defaultdict(int)

def write():
    global graph
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"output-{now}.csv"
    print(f"Saving {file_name}")
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        for interaction, strength in graph.items():
            src = interaction[0]
            dst = interaction[1]
            writer.writerow([src, dst, strength])

def should_quit(s):
    return not s or s == "quit" or s == "q"

def main():
    global graph
    src = input("Enter node (or 'quit' to quit): ")
    dst = None

    while not should_quit(src):
        dst = input(f"Who does {src} talk to?: ")
        if should_quit(dst):
            break
        graph[(int(src), int(dst))] += 1
        src = dst

    write()

    return 0

if __name__ == "__main__":
    exit(main())
