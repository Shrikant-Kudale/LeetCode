class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            # Cannot reach station i + 1 from current start_index
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index