def main():
   year_dict = {}
   count_dict = {} 
   BASE_YEAR = 1903;
   file_read = open('WorldSeries.txt', 'r')
   for line in file_read:
       teamName = line.strip()       
       year_dict[BASE_YEAR] = teamName    
       BASE_YEAR += 1;     
       cnt = winners(teamName, count_dict)      
       if cnt==1:
           count_dict[teamName] += 1
       else:
           count_dict[teamName] = 1
   file_read.close()
   showResults(year_dict, count_dict)

def printSorted(count_dict):
   from operator import itemgetter
   for k, v in sorted(count_dict.items(), key=itemgetter(1), reverse=True):
       print(k + " : " + str(v) + " Times")
        
def showResults(year_dict, count_dict):
   year = int(input('Enter a year in the range 1903-2020: '))   
   if year == 1904 or year == 1994:
       print("The world series wasn't played in the year", year)
   elif year < 1903 or year > 2020:
       print('The data for the year', year, 'is not included in our database.')
   else:
       winner = year_dict[year]
       wins = count_dict[winner]
       print('The team that won the world series in ', \
       year, ' is the ', winner, '.', sep='')
       print('They won the world series', wins, 'times.')

def winners(team, count_dict):
   if team in count_dict.keys():
       return 1
   else:
       return 0
      
      
main()
while (True):
    x = input("Do you want to continue, type 'y' for Yes, 'n' for No ")
    if (x == 'y' or x == 'Y'):
        main()
    else:
        break
