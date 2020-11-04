We've already seen how UK and US words differ in their spelling. One other difference is how UK has kept the usage of letters our in some of its words and US has done away with the letter u and uses just or. Given the UK format of the word that has our in it, find out the total number of occurrences of both its UK and US variants in a given sequence of words.

<h2> Input Format </h2>

First line contains an integer N. N lines follow, each line contains a sequence of words (W) separated by a single space. <br>
Next lines contains an integer T. T testcases follow in a new line. Each line contains the UK spelling of a word (W')

<h2> Constraints </h2>

1 <= N <= 10 <br>
Each line doesn't contain more than 10 words (W) <br>
Each character of W and W' is a lowercase alphabet. <br>
If C is the count of the number of characters of W or W', then <br>
1 <= C <= 20 <br>
1 <= T <= 10 <br>
W' that has our as a sub-string in it. <br>

<h2> Output Format </h2>

Output T lines and in each line output the number of UK and US version of (W') in all of N lines that contains a sequence of words.

<h2> Sample Input </h2>

2 <br>
the odour coming out of the left over food was intolerable <br>
ammonia has a very pungent odor <br>
1 <br>
odour <br>
<h2> Sample Output </h2>

2
<h2> Explanation </h2>

In the given 2 lines, we find odour and odor once each. So, the total count is 2.
