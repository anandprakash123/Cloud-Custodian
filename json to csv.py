import json
import csv

with open('/home/anand.prakash@happiestminds.com/Desktop/Cloud Custodian/EBS/output/mark-unattached-ebs-volumes-for-review/resources.json') as json_file:
    data = json.load(json_file)

csv_file = '/home/anand.prakash@happiestminds.com/Desktop/Cloud Custodian/EBS/output/mark-unattached-ebs-volumes-for-review/mark-unattached-ebs-volumes-for-review-report.csv'

if data:
    keys = data[0].keys()
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV report generated: {csv_file}")
else:
    print("No data found in resources.json")

