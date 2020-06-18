# LAB1
############################################################
#
# Labb 1
#

# global variables

import urllib.request
import sys
import getopt
import re
url = "https://cloud.timeedit.net/kth/web/public01/ri16lXQo530Z5lQv57017QW6y5Yp80ZZqY65Y5gQ802917QZ79WQX66wPnabxWju.html"
nyglobal = "DD1321.htm"

############################################################
#
# imports and defs
#


class schedule:
    def __init__(self):  # constructor # self is instance that can acces propeties of class
        self.time = ''  # will be determined later
        self.date = ''  # the date
        self.weekday = ''  # the day of the week
        self.week = ''  # the week number
        self.type = []  # A LIST, datorlabb/övning/julafton etc..

    def __str__(self):  # dunder method , control how object is representet as string
        s = "{ " + self.week + " " + self.weekday + \
            " " + self.date + " " + self.time
        if len(self.type) > 3:
            s += " : " + self.type[0] + " " + self.type[1] + \
                " " + self.type[2] + " " + self.type[3]
        s += " }"
        return s

    # om self innehåller x, returneras sant, går in i alla funktioner och kollar om det finns värden
    def __contains__(self, x):
        if x in self.week:
            return True


###########################################################################
##
# parse_url_file
# tar file:content som IN, detta är en sträng, hämtar schema från nätet, läggs in i en lista lines på olika index,
# IN
# filecontet : en sträng
# OUT
# vek[]: en lista
def parse_url_file(file_content):
    vek = []  # en tom lista

    reg_expr_w = re.compile(
        '.*?td.*?class.*?headline.*?> *([MTOFL][åinorä]) *20[12][0-9]-0?(1?[0-9])-0?([123]?[0-9])<.*weekin.*> *(v.*?)</', re.I)
    reg_expr_d = re.compile(
        '.*?td.*?class.*?headline.*?>([A-Z][a-z]) *20[12][0-9]-0?(1?[0-9])-0?([123]?[0-9])</')
    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)</td')
    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)</td', re.I)

    lines = file_content.split('\n')  # HÄR KRASHAR PROGRAMMET
    qq = schedule()
    for j, line in enumerate(lines):

        m = reg_expr_i.match(line)
        if (m != None):
            qq.type.append(m.group(1))  # lägg till i lines på position 1 ..
            next

        m = reg_expr_w.match(line)
        if (m != None):
            qq.week = m.group(4)
            next

        m = reg_expr_d.match(line)
        if (m != None):
            qq.weekday = m.group(1)
            qq.date = m.group(3) + "/" + m.group(2)
            next

        m = reg_expr_t.match(line)
        if (m != None):
            vek.append(qq)
            qq = schedule()
            qq.time = m.group(1)
            next

    return vek


###########################################################################
##
# get file content
# i get_file_content: OUT är en sträng och i funktionen som kraschade att IN förväntas vara en sträng.

# IN
# file_name : en str
# OUT
# file_content : en str

def get_file_content(file_name):

    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print("No such file", file_name, " please run with --update")
        print("	python", sys.argv[0], "--update")
        sys.exit()

    #file_content = infil.readlines()
    file_content = infil.read()
    return file_content

###########################################################################
##
# usage
# ger felmeddelande om --update etc, allt relaterat till terminal
# IN
# void : inget invärde
# OUT
# void : inget utvärde


def usage():
    print("Usage example:")
    print("python", sys.argv[0],  "--update ")
    print("	updates Time Edit schedule")
    print("python", sys.argv[0],  '--check "v 49"')
    print("	checks schedule for week 49")
    print("python", sys.argv[0])
    print("	prints previously downloaded schedule")

###########################################################################
##
# parse_command_line_args
# ger command av vad som behövs tilläggas
# IN
# inget invärde
# OUT
# returnerar todo : dict


def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", [
                                   "help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"] = value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo

###########################################################################
##
# print_schedule
# printar alla items i listan data (som innehåller alla week, date, times...), item är funktionen schedule först
# IN
# data : en list
# OUT
# void: inget utvärde


def print_schedule(data):
    print("----------- Schedule -------------")
    for item in data:
        print(item)

###########################################################################
##
# search_data
##
# IN
## what, dataset ()
# OUT
# printar ut bara, inget utvärde, inga referens


def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print(item)
    if (found == False):
        print("Nothing happens", what)

###########################################################################
##
# main
# slår upp i todo (ordbok) efter updates in real time, hämtar sckemat genom att ha en str som indata
# IN
##
# OUT
##


def main():

    global url
    global nyglobal

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print("fetching url ...")
        urllib.request.urlretrieve(url, nyglobal)
        print("         done")

    # Get schedule from disc
    filedata = get_file_content(nyglobal)
    sched = parse_url_file(filedata)

    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)


###########################################################################

if __name__ == "__main__":
    main()
