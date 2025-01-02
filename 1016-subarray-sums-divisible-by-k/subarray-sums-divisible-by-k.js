// I figured it from the math point of view + from the algorithms I considered for the previous daily problem? Subarray sum = difference between two prefix sums, it will be divided by k if prefix sums have the same mod k value. Hence I need to count mod k values and then caclulate the number of pairs for each count (for 0: n * (n + 1) / 2, for the rest: n * ( n - 1) / 2)

// use a hash map to keep track of the remainder of the running sum of the array modulo k. For each index i in the array, we calculate the running sum from index 0 to i, and find its remainder when divided by k. We then check if the remainder already exists in the hash map. If it does, it means that there is a subarray with a sum that is divisible by k, and we increment the count of subarrays. If the remainder doesn't exist in the hash map, we add it to the hash map with a count of 1.

var subarraysDivByK = function(nums, k) {
    let lookup = {0: 1}
    let sum = 0
    let count = 0

    for (let i = 0; i < nums.length; i++) {
        sum += nums[i]
        rem = (sum % k + k) % k
        if (lookup[rem]) count += lookup[rem]
        if (!lookup[rem]) lookup[rem] = 0
        lookup[rem]++
    }
    return count

};