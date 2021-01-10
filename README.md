
We pass an array of integers in the function params. We loop throgh the array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.


Input:
The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If we do not find an index that fits these rules, then we will return -1.

Note:
If there are multiple answers within the same array, we return the lowest correct index, 