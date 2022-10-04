import urllib
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY') 

class Tutorial:
    def __init__(self, video_url):
        self.__video_url = video_url
        self.__video_id = self.__video_url[self.__video_url.index("=") + 1:]
        self.__duration_string = self.duration_video()
        self.__duration_seconds = self.total_seconds()
        self.__partial_time = 0
        self.__partial_time_string = ''
        self.__status = "In progress"
        self.__title = ''
        
    
    def get_video_url(self):
        return self.__video_url

    def get_title(self):
        seearch_url = f'https://www.googleapis.com/youtube/v3/videos?id={self.__video_id}&key={api_key}&part=snippet'
        req = urllib.request.Request(seearch_url)
        response = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(response)
        all_data = data['items']
        title = all_data[0]['snippet']['title']
        self.__title = title
        return self.__title
    
    def duration_video(self):
        search_url = f'https://www.googleapis.com/youtube/v3/videos?id={self.__video_id}&key={api_key}&part=contentDetails'
        req = urllib.request.Request(search_url)
        response = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(response)
        all_data = data['items']
        duration = all_data[0]['contentDetails']['duration']
        dur = duration[2:-1]
        formatted_time = (dur.replace("H", ":")).replace("M", ":")
        return formatted_time

    def total_seconds(self):
        search_url = f'https://www.googleapis.com/youtube/v3/videos?id={self.__video_id}&key={api_key}&part=contentDetails'
        req = urllib.request.Request(search_url)
        response = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(response)
        all_data = data['items']
        duration = all_data[0]['contentDetails']['duration']
        dur = duration[2:-1]
        formatted_time = (dur.replace("H", ":")).replace("M", ":")
        time_array = formatted_time.split(":")
        hours = 0
        minutes = 0
        seconds = 0

        if len(time_array) == 3:
            hours = int(time_array[0]) * 3600
            minutes = int(time_array[1]) * 60
            seconds = int(time_array[2])
            total_time = hours + minutes + seconds
        elif len(time_array) == 2:
            minutes = int(time_array[0]) * 60
            seconds = int(time_array[1])
            total_time = minutes + seconds
        else:
            total_time = int(time_array[0])
        
        return total_time     
        
    def get_duration_seconds(self):
        return self.__duration_seconds

    def get_duration_string(self):
        return self.__duration_string

    def get_partial_time(self):
        return self.__partial_time

    def get_partial_time_string(self):
        return self.__partial_time_string

    def get_status(self):
        return self.__status

    def set_partial_time(self, time):
        formatted_time = time.split(":")
        if len(formatted_time) == 3:
            self.__partial_time = int(formatted_time[0]) * 3600 + int(formatted_time[1]) * 60 + int(formatted_time[2])
        elif len(formatted_time) == 2:
            self.__partial_time = int(formatted_time[0]) * 60 + int(formatted_time[0])
        elif len(formatted_time) == 1:
            self.__partial_time = int(formatted_time[0])

    def set_partial_time_string(self, time):
        self.__partial_time_string = time

    def set_status(self, string):
        self.__status = string