class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        curr_gas = 0
        for idx in range(len(gas)):
            curr_gas += gas[idx] - cost[idx]
            if curr_gas < 0:
                curr_gas = 0
                start = idx + 1
        return start

