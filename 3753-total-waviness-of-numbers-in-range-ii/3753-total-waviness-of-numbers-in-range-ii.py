class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(limit: int) -> int:
            if limit < 100:
                return 0
            
            s = str(limit)
            n = len(s)
            memo = {}
            
            def dfs(idx: int, prev: int, prev2: int, is_less: bool, is_started: bool) -> tuple:
                if idx == n:
                    return (1 if is_started else 0, 0)
                
                state = (idx, prev, prev2, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit_digit = int(s[idx]) if not is_less else 9
                total_ways = 0
                total_waves = 0
                
                for d in range(limit_digit + 1):
                    next_less = is_less or (d < int(s[idx]))
                    
                    if not is_started:
                        if d == 0:
                            ways, waves = dfs(idx + 1, -1, -1, next_less, False)
                        else:
                            ways, waves = dfs(idx + 1, d, -1, next_less, True)
                    else:
                        wave_increment = 0
                        if prev2 != -1 and prev != -1:
                            if (prev > prev2 and prev > d) or (prev < prev2 and prev < d):
                                wave_increment = 1
                        
                        ways, waves = dfs(idx + 1, d, prev, next_less, True)
                        total_waves += wave_increment * ways
                        
                    total_ways += ways
                    total_waves += waves
                    
                memo[state] = (total_ways, total_waves)
                return memo[state]
            
            return dfs(0, -1, -1, False, False)[1]
        
        return solve(num2) - solve(num1 - 1)
