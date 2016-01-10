f = open("crime_rates.csv", "r")
data = f.read()
rows = data.split('\n')
final_data = [row.split(",")
              for row in rows
             if len(row.split(",")) == 2]
#print(final_data)
cities = [city for city, _ in final_data]