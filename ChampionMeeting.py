class ChampionMeeting:
    def __init__(self, place, ground, distance, distanceType, direction, season, weather, groundCondition):
        self.place = place               
        self.ground = ground              
        self.distance = distance          
        self.distanceType = distanceType  
        self.direction = direction        
        self.season = season              
        self.weather = weather           
        self.groundCondition = groundCondition  

    def display_info(self):
        return (f"สนาม {self.place},ประเภทสนาม{self.ground},ระยะ{self.distance}m,ประเภทระยะทาง{self.distanceType} "
                f",วิ่งทาง {self.direction},ฤดู {self.season},อากาศ {self.weather},สภาพสนาม {self.groundCondition}")