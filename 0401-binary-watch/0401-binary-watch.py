class Solution:
    def getTimeString(self, selections, selected_indices):
        hours = 0
        minutes = 0
        for selected_index in selected_indices:
            time = selections[selected_index][0]
            kind = selections[selected_index][1]
            if kind == 'M':
                minutes += time
            else:
                hours += time
               
        if hours > 11 or minutes > 59:
            return ""
        
        str_minutes = str(minutes)
        if minutes < 10:
            str_minutes = "0" + str(minutes)
        
        return str(hours) + ":" + str_minutes
    
    def dfs(self, cur_index, selections, selected_indices, t, possible_times):
        selected_indices.append(cur_index)
        t -= 1
        
        if t == 0:
            time = self.getTimeString(selections, selected_indices)
            if time != "":
                possible_times.append(time)
            selected_indices.pop()
            return
        
        for next_index in range(cur_index + 1, 10):
            self.dfs(next_index, selections, selected_indices, t, possible_times)
            
        selected_indices.pop()
            
    def readBinaryWatch(self, t: int) -> List[str]:
        if t == 0:
            return ["0:00"]
        if t > 8:
            return []
        
        selected_indices = []
        selections = [[8, 'H'], [4, 'H'], [2, 'H'], [1, 'H'], [32, 'M'], [16, 'M'], [8, 'M'], [4, 'M'], [2, 'M'], [1, 'M']]
        
        possible_times = []
        for index in range(10):
            self.dfs(index, selections, selected_indices, t, possible_times)
        return possible_times
        