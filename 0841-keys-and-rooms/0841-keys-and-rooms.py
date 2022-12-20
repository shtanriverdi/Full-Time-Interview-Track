class Solution:
    def isPossible(self, cur_room, rooms, seen):
        seen.add( cur_room )
        for next_room in rooms[cur_room]:
            if next_room not in seen:
                self.isPossible(next_room, rooms, seen)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        actual_room_count = len(rooms)
        seen = set()
        self.isPossible(0, rooms, seen)
        processed_room_count = len(seen)
        return actual_room_count == processed_room_count