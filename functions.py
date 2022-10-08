import pickle
from pathlib import Path
from classes import *

def check_file():
    tutorial_list = []
    path = Path("tutorials.data")
    if path.is_file() == 0:
        with open("tutorials.data", "wb") as tut_file:
            pickle.dump(tutorial_list, tut_file)

def load_file():
    with open('tutorials.data', 'rb') as tut_file:
        tutorial_list = pickle.load(tut_file)
    return tutorial_list

def save_file(tutorial_list):
    with open('tutorials.data', 'wb') as tut_file:
        pickle.dump(tutorial_list, tut_file)

def get_bars(part, total):
    progress = (part / total) * 100    
    print("|" + int(progress - 1) * "=" + ">" + (100 - int(progress)) * "-" + "| {}%".format(int(progress)))

def list_tutorials():
    tutorials = load_file()
    for tutorial in tutorials:
        print(tutorial.get_title())
        print("Tutorial status: {}".format(tutorial.get_status()))
        print('Left off at: {}, Total length: {}'.format(tutorial.get_partial_time_string(), tutorial.get_duration_string()))
        get_bars(tutorial.get_partial_time(), tutorial.get_duration_seconds())
        print(tutorial.get_video_url() + "#t={}".format(tutorial.get_partial_time()))
        print("\n")

def add_tutorial(url):
    tutorials = load_file()
    new_tutorial = Tutorial(url)
    tutorials.append(new_tutorial)
    save_file(tutorials)

def update_progress(url, time):
    tutorials = load_file()
    for tutorial in tutorials:
        if tutorial.get_video_url() == url:
            tutorial.set_partial_time(time)
            tutorial.set_partial_time_string(time)
    save_file(tutorials)

def complete_tutorial(url):
    tutorials = load_file()
    for tutorial in tutorials:
        if tutorial.get_video_url() == url:
            tutorial.set_partial_time_string(tutorial.get_duration_string())
            tutorial.set_partial_time(tutorial.get_duration_string())
            tutorial.set_status("Completed")
    save_file(tutorials)

def delete_tutorial(url):
    tutorials = load_file()
    for tutorial in tutorials:
        if tutorial.get_video_url() == url:
            index = tutorials.index(tutorial)
            del tutorials[index]
    save_file(tutorials)

def get_url():
    url = input("Enter full URL of tutorial: ")
    while url[:32] != "https://www.youtube.com/watch?v=":
        url = input("Please enter a valid youtube URL: ")        
    return url

def get_time():
    time = input("Enter time (hh:mm:ss)")
    if len(time) <= 2 and time.isnumeric():
        if int(time) > 0 and int(time) < 60:
            return time
        else:
            print("Invalid time")
    elif len(time) > 2:
        if time.__contains__(":"):
            array = time.split(":")
            if len(array) == 1:
                print("Invalid time")
            elif len(array) == 2:
                if array[0].isnumeric() and int(array[0]) >= 0 and int(array[0]) < 60:
                    if array[1].isnumeric() and int(array[1]) >= 0 and int(array[1]) < 60:
                        return "{}:{}".format(array[0], array[1])
                    else: 
                        print("Invalid time")
                else:
                    print("Invalid time")
            elif len(array) == 3:
                if array[0].isnumeric() and int(array[0]) >= 0 and int(array[0]) < 60:
                    if array[1].isnumeric() and int(array[1]) >= 0 and int(array[1]) < 60:
                        if array[2].isnumeric() and int(array[2]) >= 0 and int(array[2]) < 60:
                            return "{}:{}:{}".format(array[0], array[1], array[2])
                        else:
                            print("Invalid time")
                    else:
                        print("Invalid time")
                else:
                    print("Invalid time")
            else:
                print("Invalid time")
        else:
            print("Invalid time")
    else:
        print("Invalid time")