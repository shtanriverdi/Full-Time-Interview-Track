class Solution:
    def is_ip_valid(self, ip):
        isValid = lambda num: 0 <= num <= 255
        parts = ip.split('.')
        for part in parts:
            part_n = len(part)
            if (part_n > 1 and part[0] == '0') or not isValid(int(part)):
                return False
        return True

    def dot_helper(self, ip, put_dot_index, num_of_dots, answer):
        if num_of_dots == 0:
            str_ip = "".join(ip) 
            if self.is_ip_valid(str_ip):
                answer.append(str_ip)

        for index in range(put_dot_index, min(len(ip), put_dot_index + 3)):
            ip.insert(index, '.')
            self.dot_helper(ip, index + 2, num_of_dots - 1, answer)
            ip.pop(index)

    def solve(self, ip):
        answer = []
        self.dot_helper(list(ip), 1, 3, answer)
        return answer