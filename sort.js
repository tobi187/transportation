arr = [2,1,9,3]

for (var i = 0; i < arr.length-1;i++) {
    for (var j=i+1; j < arr.length; j++) {
        if (arr[i] > arr[j]) {
            var tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        }
    }
}
console.log(arr)
