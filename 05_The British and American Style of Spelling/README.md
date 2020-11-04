American English and British English differ in several aspects which are reflected in their spelling. One difference frequently observed, is that words written in American English, which have a suffix ze often end in se in British English. Given the American-English spelling of a word which ends in ze your task is to find the total count of all its British and American variants in all the given sequences of words. i.e. you need to account for the cases where the word occurs as it is given to you (i.e. the version ending in -ze) and you also need to find the occurances of its British-English counterparts (i.e, the version ending in -se).

<h2>Input Format </h2>

First line contains N, N lines follow each line contains a sequence of words (W) separated by a single space. Next line contains T. T testcases follow in a new line. Each line contains the American English spelling of a word (W')

<h2>Constraints </h2>

1 <= N <= 10 <br>
Each line doesn't contain more than 10 words (W) <br>
Each character of W and W' is a lowercase alphabet. <br>
If C is the count of the number of characters of W or W', then <br>
1 <= C <= 20 <br>
1 <= T <= 10 <br>
W' ends with ze ( US version of the word)

<h2>Output Format </h2>

Output T lines and in each line output the total number of American and British versions of (W') in all of N lines that contains a sequence of words.

<h2>Sample Input </h2>

2 <br>
hackerrank has such a good ui that it takes no time to familiarise its environment <br>
to familiarize oneself with ui of hackerrank is easy <br>
1 <br>
familiarize
<h2>Sample Output </h2>

2
<h2>Explanation </h2>

In the given 2 lines, we find familiarize and familiarise once each. So, the total count is 2.
