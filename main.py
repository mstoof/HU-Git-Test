import json

def read_json():
    with open('steam.json') as file:
        lines = json.load(file)
        for index, line in enumerate(lines):
            app_id = line.get('appid')
            app_name = line['name']
            release_date = line['release_date']
            developer = line['developer']
            categories = line['categories']

            print(f"App ID: {app_id} \n"
                  f"App Name: {app_name} \n"
                  f"Release Date: {release_date} \n"
                  f"Developer: {developer} \n"
                  f"Categories: {categories} \n")



if __name__ == '__main__':
    read_json()