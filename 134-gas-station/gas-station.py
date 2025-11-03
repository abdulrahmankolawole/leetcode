class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = sum(cost)
        total_gas = sum(gas)

        # if (total_cost > total_gas):
        #     return -1

        start = len(gas) - 1
        next_stop = 0

        gas_in_tank = gas[start] - cost[start]

        while (start >= next_stop):
            if (gas_in_tank >= 0):
                gas_in_tank += gas[next_stop] - cost[next_stop]
                next_stop += 1

            else:
                start -= 1
                gas_in_tank += gas[start] - cost[start]


        return start if gas_in_tank >= 0 else -1 