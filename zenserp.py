try:
    import csv

    import requests
    import json

   
except ImportError:
    print("No module found")



# to search
queryy = "Keywords"
with open('keywords.csv', 'w', newline='') as file:
    fieldnames = ['Results']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    with open('o.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                str1 = ''.join(row)
                queryy = str1
                print("TOP Google SEARCH RESULTS For:" + queryy)
                writer.writerow({'Results': "For: " + queryy})
                headers = { 'apikey': 'ebde4fd0-8c9a-11ea-8869-9108d5b495e1.' }

                params = (
                   ("q",queryy),
                   ("device","desktop"),
                   ("location","Manhattan,New York,United States"),
                   ("num","25"),
                );                

                response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);




                j = response.json()
          

              

              


                
                x = j['organic'][16]['title']
                writer.writerow({'Results': x})
                print(x)
                x = j['organic'][17]['title']
                writer.writerow({'Results': x})
                print(x)

                x = j['organic'][18]['title']
                writer.writerow({'Results': x})
                print(x)

                x = j['organic'][19]['title']
                writer.writerow({'Results': x})
                print(x)

                x = j['organic'][20]['title']
                writer.writerow({'Results': x})
                print(x)

                
                

                """
                i = 0
                num = 11
                while i < num:
                    
                    x = j['organic'][i]['title']
               
                    writer.writerow({'Results': x})
                    print(x)
                    i += 1
               
                    
                """
                    
                    

                


               
