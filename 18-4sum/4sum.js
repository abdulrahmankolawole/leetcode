var fourSum = function(nums, target) {
    let lookup = new Set()
    let output = []
    let arr = [...nums].sort((a, b)=> a - b)

    for (let i = 0; i < nums.length - 3; i++) {
        for (let j = i + 1; j < nums.length - 2; j++) {
            first = arr[i]
            second = arr[j]

            a = j + 1
            b = nums.length - 1

            while (a < b) {
                sum = first + second + arr[a] + arr[b]

                if (sum == target) {
                    quadruplets = first + "," + second + "," + arr[a] + "," + arr[b]
                    if (!(lookup.has(quadruplets))) {
                        lookup.add(quadruplets)
                        output.push([first, second, arr[a], arr[b]])
                    }
                    a += 1
                    b -=1
                }
                else if (sum < target) a += 1
                else b -= 1
            }

        }
    }  
    return output
};