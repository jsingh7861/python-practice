###
# Extracting the title from example.json file
###

import json

def json_title(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        sorted_data = data.get('entities')
        sorted_data1 = sorted_data.get('urls') 
        for i in sorted_data1:
            v = i.get('unwound')
            final_output = v.get('title')
            print(final_output)


                   
if __name__ == "__main__":
    print("Enter the json file name:")
    file_name = 'example.json' 
    json_title(file_name)
