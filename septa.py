#!/usr/bin/python3

import csv

data_dir = './data'

# Days
WD = 1
SUN = 7
SAT = 6

# Options, hardcoded for now:
day = SUN
route = '84'
stop = '1102'

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

print(times)
