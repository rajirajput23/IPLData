#Importing necessary libraries to Scrpe data

import requests
import pandas as pd
from bs4 import BeautifulSoup


#Providing the url to request access to the website.
url="https://www.iplt20.com/auction/2023#https://bcciplayerimages.s3.ap-south-1.amazonaws.com/ipl/franchises/1671190498_GTroundbig%20%282%29%201.png"
r=requests.get(url)

#print(r)

#Creating a soup objecy to get all the html to parse through. 
soup= BeautifulSoup(r.content, "html.parser")

#Created a table variable to store the table content

table= soup.find("table", class_="ih-td-tab auction-tbl")
#print(table)

#Creating a header variable to store table headings from the table.

header= table.find_all("th")
#print(header)

# Empty titles list
titles=[ ]
# For loop to iterate through the table headers, and append values to the titles list.
for i in header:
    title= i.text
    titles.append(title)

#print(titles)

#Created a dataframe to store the scraped data.
df=pd.DataFrame(columns=titles)
#print(df)

# Now for the data in rows we will create a rows variable that will store the data that is extracted from the tr tag.
rows=table.find_all("tr")
#print(rows)

# Here we will loop through the data and append the data to the location 
for i in rows[1:]:
    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    #print(row)
    l= len(df)
    df.loc[l]=row


# To remove the spaces from data data. 
for col in df:
    df[col]=df[col].str.replace(r'\n', '')

print(df)
#converting the DataFrame into a csv file.
df.to_csv("ipl_stats_data.csv")



