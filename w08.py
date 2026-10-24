from ChampionMeeting import ChampionMeeting

CM1 = ChampionMeeting(place="Oi",ground="Dirt",distance=2000,distanceType="Medium",direction="Right",season="Fall",weather="Sunny",groundCondition="Good Ground")
CM2 = ChampionMeeting(place="Tokyo",ground="Turf",distance=2400,distanceType="Long",direction="Left",season="Spring",weather="Cloudy",groundCondition="Firm")


print(CM1.display_info())
print(CM2.display_info())