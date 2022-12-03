import csv

def printDesc(entry):
    print("")
    for key in entry.keys():
        print(f"{(key).title():18}: \t{entry.get(key).title()}")
    print("")

def printMenu(headers):
    print(f"\nCmd {'':18}Options")
    for header in headers.keys():
        print(f"{header+1:2} {'':20} {headers[header].title()}")
    
file = open(r'.\Characters.csv',encoding="cp1252")
reader = csv.reader(file)
headers = next(reader)
headers=headers[0].lower().replace("\t","").split(';')

options={}

for header in range(0,len(headers)):
    options[header]=headers[header]
    


print(f"{'':50}Welcome To Harry Potter Database")





rows = []

for row in reader:
    rows.append(row)

database=[]
try:
    for row in rows:
        entry={}
        for header in range(0,len(headers)):
            entry[headers[header]]=row[0].split(";")[header].replace("\t","").lower()
        database.append(entry)
except IndexError:
    pass
while True:
    printMenu(options)
    search = int(input("\nEnter the Criteria:"))
    if search>15 or search <1:
        print("Criteria should be in between 1 and 15")
        continue
    search=options.get(search-1)
    value = str(input(f"Enter the Wizard's {search.title()}:")).lower()
    found=False
    for entry in database:
        if(entry.get(search).find(value)>=0):
                printDesc(entry)
                found=True
                
    if not found:
        print("No Wizard in that name")


    
