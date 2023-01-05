class Solution:
    def getMinutes(self, hours, minutes):
        first_digit = hours[0]
        second_digit = hours[1]
        total_minutes = 0
        
        if first_digit != "0":
            total_minutes += (int(first_digit) * 10) * 60
        if second_digit != "0":
            total_minutes += int(second_digit) * 60
            
        if minutes[0] != "0":
            total_minutes += int(minutes[0]) * 10
        if minutes[1] != "0":
            total_minutes += int(minutes[1])
            
        return total_minutes
    
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_start = self.getMinutes(event1[0][0:2], event1[0][3:])
        event1_end = self.getMinutes(event1[1][0:2], event1[1][3:])
        
        event2_start = self.getMinutes(event2[0][0:2], event2[0][3:])
        event2_end = self.getMinutes(event2[1][0:2], event2[1][3:])
        
        event_1 = [event1_start, event1_end]
        event_2 = [event2_start, event2_end]
        
        events = [event_1, event_2]
        events.sort(key = lambda event: event[1])
        
        return events[1][0] <= events[0][1]
