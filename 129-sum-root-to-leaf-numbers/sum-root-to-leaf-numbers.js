var sumNumbers = function(root) {
    if (!root) return null
    let array = new Array()
    sum = 0

    function traverse(node, currentPath) {
        if (!node) return ""
        currentPath += node.val
        if (!node.left && !node.right) {
            sum += Number(currentPath)
            return ""
        }
        if (node.left) traverse(node.left, currentPath)
        if (node.right) traverse(node.right, currentPath)

    }   

    traverse(root, "")
    return sum
};