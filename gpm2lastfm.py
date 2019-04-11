import csv
import datetime as dt
import json

def main():
    with open('My Activity.json') as f:
        data = json.load(f)

    with open('gpmscrobbles.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for entry in data:
            if not entry['title'] == 'Used Google Play Music':
                artist = entry['description']
                track = entry['title'].replace('Listened to ', '')
                try:
                    timestamp = dt.datetime.strptime(entry['time'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    timestamp = dt.datetime.strptime(entry['time'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([artist, track, timestamp])


if __name__ == '__main__':
    main()