import time
from datetime import datetime

class LogManager:
    def log(self, text):
        print('{} {}'.format(self.get_formatted_timestamp_for_file(), text))
    
    def get_formatted_timestamp_for_file(self):
        return '[{}]'.format(self.get_formatted_timestamp())
        
    def get_formatted_timestamp(self):
        timestamp = time.time()
        date_time = datetime.fromtimestamp(timestamp) # convert to datetime
        str_date_time = date_time.strftime("%Y-%m-%d %H:%M:%S") # convert timestamp to string
        return str_date_time
