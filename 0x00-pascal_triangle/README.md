# Pascal's Triangle
<h2> Pascal formula</h2>
	The formula to fill the number in the nth column and mth row of Pascal's triangle we use the Pascals triangle formula. The formula requires the knowledge of the elements in the (n-1)th row, and (m-1)th and nth columns. The elements of the nth row of Pascal's triangle are given by, nC0, nC1, nC2, ..., nCn. The formula for Pascal's triangle is:

(n)Cm = (n-1)Cm-1 + (n-1)Cm

where

nCm represents the (m+1)th element in the nth row.
n is a non-negative integer, and
0 ≤ m ≤ n.
Let us understand this with an example. If we want to find the 3rd element in the 4th row, this means we want to calculate 4C2. Then according to the formula, we get

4C2 = 4-1C2-1 + 4-1C2

⇒ 4C2 = 3C1 + 3C2

So, this means we need to add the 2nd element in the 3rd row (i.e. 3) with the 3rd element in the 3rd row (i.e. 3.). So our answer will be 4C2 = 3 + 3 = 6

# My attemps:
At first, i added deafult values to all_lis to start with [[1], [1, 1]]
- excluded the specil casses before loops
- tried to loop through every row in the all list ( first loop)
- added [1] as first element and a last element always
- looped in range of (1, row) as row = num of elelemnts added [exclude the both 1](second loop)
- used the pascal formula "" (n)Cm = (n-1)Cm-1 + (n-1)Cm "" , worked coz i have default values
- add row ( lists) to to all_list 
- return it

# problem faced
I took a long time to figure out how i would manage the loops dynmically, and this was hard with the value (1) at start and end, didnt get it at first but finally it's hard coded :)
