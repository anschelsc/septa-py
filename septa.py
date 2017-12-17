#!/usr/bin/python3

import csv
from sys import argv, exit

data_dir = './data'

# Days
days = {'wd': 1, 'sun': 7, 'sat': 6}

# Get options from the command line
if len(argv) != 4:
    print('USAGE: ' + argv[0] + ' day route stop_id\nSee README')
    exit(1)
route = argv[2]
stop = argv[3]
if argv[1].lower() not in days:
    print('day must be WD, SAT, or SUN (case insensitive)')
    exit(1)
day = days[argv[1].lower()]

# Get a set of services for this day
services = set()
with open(data_dir + '/calendar.txt', newline='') as cal_file:
    cal = csv.reader(cal_file)
    for line in cal:
        if line[day] == '1':
            services.add(line[0])

# Get a set of trips for this route on this day
trips = set()
with open(data_dir + '/trips.txt', newline='') as trips_file:
    trips_lines = csv.reader(trips_file)
    for line in trips_lines:
        if line[0] == route and line[1] in services:
            trips.add(line[2])

# Get a list of times for this stop on this route on this day
times = []
with open(data_dir + '/stop_times.txt', newline='') as st_file:
    st = csv.reader(st_file)
    for line in st:
        if line[3] == stop and line[0] in trips:
            times.append(line[2])
times.sort()

print('\n'.join(times))
