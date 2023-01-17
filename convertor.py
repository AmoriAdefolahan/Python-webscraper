import csv 
import json 

#Function to convert a csv to JSON 

def make_json(csvFilePath, jsonFilePath):

    #create a root dictionary
    data = {}
    
    with open(csvFilePath, encoding = 'utf-8' ) as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
           car = rows["car"]
           data[car] = rows

    with open(jsonFilePath, 'w', encoding= 'utf-8') as jsonf: 
        jsonf.write(json.dumps(data, indent=4))
#Driver code 
csvFilePath = r'Carreport.csv'
jsonFilePath = r'Carreport.json'


make_json(csvFilePath, jsonFilePath)