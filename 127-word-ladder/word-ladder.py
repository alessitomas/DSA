# beginWord could not be in the wordList


#    | ----------------------------|
# ["hot" <-> "dot" <-> "dog" <-> "lot" <-> "log" <-> "cog"]
#                 | --------------|


# from target node BFS numering the distance and than the 1 dist away with lowest dist

# N length of wordlist
# M length of str
# time O( Nˆ2 * M)  
from collections import defaultdict, deque
class Solution:
    def is_1_dist_away(self, a, b):
        if len(a) != len(b):
            return False
        diffs = 0
        for ai, bi, in zip(a,b):
            if ai != bi:
                diffs += 1
            if diffs > 1:
                return 0
        return diffs == 1


    def bfs(self, cur_index, one_away, graph, index_repre):
        queue = deque()
        queue.append([cur_index, 2])
        visited = set([cur_index])

        while len(queue) > 0:
            cur_index, cur_dist = queue.popleft()
            for repre in index_repre[cur_index]:
                for neigh in graph[repre]:
                    if neigh in visited:
                        continue 
                    
                    if neigh in one_away:
                        return cur_dist + 1
                    
                    queue.append([neigh, cur_dist + 1])
                    visited.add(neigh)

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # adjacency list, using wordlsit indexes
        graph = defaultdict(list)
        index_repre = defaultdict(list)
        begin_len = len(beginWord)
        end_len = len(endWord)
        if begin_len != end_len: return 0

        one_away = set()
        target_index = None
        
        # time O( Nˆ2 * M)  
        # for i in range(len(wordList)):
        #     if wordList[i] == endWord:
        #         target_index = i
        #     if self.is_1_dist_away(beginWord, wordList[i]):
        #         one_away.add(i)
        #     for j in range(i + 1, len(wordList)):
        #         if self.is_1_dist_away(wordList[j], wordList[i]):
        #             graph[i].append(j)
        #             graph[j].append(i)
        
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                target_index = i
            if self.is_1_dist_away(beginWord, wordList[i]):
                one_away.add(i)
            for j in range(len(wordList[i])):
                s_split = list(wordList[i])
                s_split[j] = "*"
                repre = "".join(s_split)
                graph[repre].append(i)
                index_repre[i].append(repre)
                

        if len(one_away) == 0 or target_index is None:
            return 0
        
        if target_index in one_away:
            return 2

        return self.bfs(target_index, one_away, graph, index_repre) 


        


                





        