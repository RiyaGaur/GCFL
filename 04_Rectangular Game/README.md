You are given an infinite 2-d grid with the bottom left cell referenced as (1,1). All the cells contain a value of zero initially. Let's play a game?

The game consists of N steps wherein each step you are given two integers a and b. The value of each of the cells in the co-ordinate (u, v) satisfying 1 ≤ u ≤ a and 1 ≤ v ≤ b, is increased by 1. After N such steps, if X is the largest number amongst all the cells in the rectangular board, can you print the number of X's in the board?

<h2>Input Format</h2>
The first line of input contains a single integer N. N lines follow. <br>
Each line contains two integers a and b separated by a single space.

<h2>Output Format</h2>
Output a single integer - the number of X's.

<h2>Constraints</h2>
1 ≤ N ≤ 100 <br>
1 ≤ a ≤ 106 <br>
1 ≤ b ≤ 106

<h2>Sample Input</h2>

3 <br>
2 3 <br>
3 7 <br>
4 1
<h2>Sample Output</h2>

2
<h2>Explanation</h2>

Assume that the following board corresponds to cells (i, j) where 1 ≤ i ≤ 4 and 1 ≤ j ≤ 7.

At the beginning board is in the following state:

0 0 0 0 0 0 0 <br>
0 0 0 0 0 0 0 <br>
0 0 0 0 0 0 0 <br>
0 0 0 0 0 0 0 

After the first step we will obtain:

0 0 0 0 0 0 0 <br>
0 0 0 0 0 0 0 <br>
1 1 1 0 0 0 0 <br>
1 1 1 0 0 0 0 

After the second step we will obtain:

0 0 0 0 0 0 0 <br>
1 1 1 1 1 1 1 <br>
2 2 2 1 1 1 1 <br>
2 2 2 1 1 1 1 

Finally, after the last step we will obtain:

1 0 0 0 0 0 0 <br>
2 1 1 1 1 1 1 <br>
3 2 2 1 1 1 1 <br>
3 2 2 1 1 1 1 

So, the maximum number is 3 and there are exactly two cells which correspond to 3. Hence 2.
