class Solution:
    def dfs(self, current_node, tree, s, longest_path_len):
        path_lengths = []
        for child in tree[current_node]:
            one_path_len = self.dfs(child, tree, s, longest_path_len)
            if s[current_node] != s[child]:
                path_lengths.append( one_path_len )
        
        max_path_len = 0
        second_max_path_len = 0
        if path_lengths:
            path_lengths.sort(reverse=True)
            max_path_len = path_lengths[0]
            if len(path_lengths) > 1:
                second_max_path_len = path_lengths[1]
        
        current_max_path_len = 1 + max_path_len + second_max_path_len
        longest_path_len[0] = max(longest_path_len[0], current_max_path_len)
        
        # print("current_node:",current_node)
        # print("longest_path_len:",longest_path_len[0])
        # print("return:", 1 + max_path_len, end="\n\n")
        
        return 1 + max_path_len
        
    def longestPath(self, parents: List[int], s: str) -> int:
        # Build the tree
        tree = defaultdict(list)
        for node, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(node)
        
        longest_path_len = [0]
        self.dfs(0, tree, list(s), longest_path_len)
        
        return longest_path_len[0]