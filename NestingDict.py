travel_log={
	"Jharkhand":{
		"cities_visited":["Godda","Deoghar","Jasidih"],
		"total_visits":12,
	},
	"Bihar":{
		"cities_visited":["Bhagalpur","Patna","Fatuha"],
		"total_explored":5,
	},
}

for x,y in travel_log.items():
	print(y["cities_visited"][0])
