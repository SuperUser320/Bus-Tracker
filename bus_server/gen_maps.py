#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import csv, time, threading

routes = []

PORT_NUMBER = 8080

def gen_maps():
    routes = []

    from subprocess import call
    call(["sh", "get_db.sh"])

    with open('db.csv', 'rb') as csvfile:
        dbreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in dbreader:
            if not (row[0] in routes) and not (row[0] == "route"):
                from subprocess import call
                call(["sh", "get_map.sh", row[0], row[1], row[2], "320", "200"])
                routes.append(row[0]);

    threading.Timer(5, gen_maps).start()

#Start generating maps
gen_maps()
