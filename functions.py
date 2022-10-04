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