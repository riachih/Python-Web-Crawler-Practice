import pymongo
client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

#left for python and right for the data collection
# path = '/Users/riachih/Desktop/walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             'index': index,
#             'line' : line,
#             'words' : len(line.split())
#         }
#         # filling up the excel sheet
#         sheet_tab.insert_one(data)
#do it one and then the collection would be filled, no need to run it everytime

for item in sheet_tab.find({'words':{'$lt':5}}):
    print(item)