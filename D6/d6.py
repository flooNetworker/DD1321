import datetime
import json
import urllib
import urllib.request
import sys
import re


def parse_url_file(course, start=None, end=None):
    vek = []

    kurs = re.compile("([A-Z]{2})([0-9]{4})")
    datum = re.compile("(20)?[12][0-9](-)?0?(1?[0-9])(-)?0?([123]?[0-9])")

    m = kurs.match(course)
    if m != None:
        vek.append(course)
    else:
        print("Course not accepted")
        sys.exit()

    if start != None:
        m = datum.match(start)
        if m != None:

            if len(start) != 10:
                if len(start) == 8:
                    year = start[0:4]
                    month = start[4:6]
                    day = start[6:8]

                    start = year+"-"+month+"-"+day

                elif len(start) == 6:
                    year = start[0:2]
                    month = start[2:4]
                    day = start[4:6]
                    start = "20"+year+"-"+month+"-"+day

                else:
                    print("Write month and day in format MM-DD")
                    sys.exit()

            vek.append(start)
        else:
            print("Start date not accepted")
            sys.exit()

    if end != None:
        m = datum.match(end)
        if m != None:
            if len(end) != 10:
                if len(end) == 8:
                    year = end[0:4]
                    month = end[4:6]
                    day = end[6:8]

                    end = year+"-"+month+"-"+day

                elif len(end) == 6:
                    year = end[0:2]
                    month = end[2:4]
                    day = end[4:6]
                    end = "20"+year+"-"+month+"-"+day

                else:
                    print("Write month and day in format MM-DD")
                    sys.exit()

            vek.append(end)
        else:
            print("End date not accepted")
            sys.exit()

    return vek


def dates(start, end):
            # date in yyyy/mm/dd format

    s = datetime.datetime.strptime(start, "%Y-%m-%d")
    e = datetime.datetime.strptime(end, "%Y-%m-%d")

    if s > e:
        print("End date before start date")
        sys.exit()

    dates = []

    dates.append(str(s.year)+"-"+str(s.month)+"-"+str(s.day))

    while s <= e:
        d = datetime.timedelta(days=7)
        s = s + d

        year = str(s.year)
        month = str(s.month)
        day = str(s.day)

        if int(month) <= 9:
            month = "0" + month
        if int(day) <= 9:
            day = "0" + day

        dates.append(year+"-"+month+"-"+day)

    return dates


def print_schedule(data):
    for i in range(len(data["entries"])):
        location = []
        for x in data["entries"][i]["locations"]:
            location.append(x["name"])

        print(data["entries"][i]["start"], data["entries"][i]
              ["end"], data["entries"][i]["title"], location)

    # for element in data[0], data[1] and data[2]
    # data[i] is dict with elements start, end, title etc.


def testing():
    if len(sys.argv) < 5:  # check if the length of argument is less than 3
        print(
            "Insert course ID [ccnnnn] and optional start and end time [yyyy-mm-dd]")
        print("Use the program like this:: \n\t python3",
              sys.argv[0], " [course] [start (optional)] [end(optional)]")

        if len(sys.argv) > 1:
            course = sys.argv[1]
            course = parse_url_file(course)[0]
        else:
            sys.exit()

            if len(course) != 6:
                print("Course not accepted, too many characters")
                sys.exit()

        if len(sys.argv) == 3:
            start = parse_url_file(course, sys.argv[2])[1]
            return [course, start, None]

        if len(sys.argv) == 4:
            start = parse_url_file(course, sys.argv[2])[1]
            end = parse_url_file(course, sys.argv[2], sys.argv[3])[2]
            return [course, start, end]

        return [course, None, None]

    elif len(sys.argv) > 4:  # else if the length of argument is more than 3
        print("Too many arguments")
        sys.exit()


#-----------------------#
# MAIN
#-----------------------#

l = testing()

course = l[0]
start = l[1]
end = l[2]


if end != None:
    datum = dates(start, end)

    print("----------- Schedule -------------")
    for day in datum:
        schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
        start = "?startTime="+day
        schemaurl += course + start

        # start = start till end, pluss en vecka hela tiden, skicka in vecka för dag i print

        request_data = urllib.request.urlopen(
            schemaurl).read()  # hämtar data från REST-servern
        # översätter u00f6 -> ö
        utf_data = request_data.decode('utf-8')
        # lägger in i en pythonstruktur

        schedule = json.loads(utf_data)

        print_schedule(schedule)

elif start != None:

    print("----------- Schedule -------------")
    schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
    start = "?startTime="+start
    schemaurl += course + start

    # start = start till end, pluss en vecka hela tiden, skicka in vecka för dag i print

    request_data = urllib.request.urlopen(
        schemaurl).read()  # hämtar data från REST-servern
    # översätter u00f6 -> ö
    utf_data = request_data.decode('utf-8')
    # lägger in i en pythonstruktur

    schedule = json.loads(utf_data)

    print_schedule(schedule)

else:

    print("----------- Schedule -------------")
    print("No entries")

    schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
    schemaurl += course

    # start = start till end, pluss en vecka hela tiden, skicka in vecka för dag i print

    request_data = urllib.request.urlopen(
        schemaurl).read()  # hämtar data från REST-servern
    # översätter u00f6 -> ö
    utf_data = request_data.decode('utf-8')
    # lägger in i en pythonstruktur

    schedule = json.loads(utf_data)

    print_schedule(schedule)
