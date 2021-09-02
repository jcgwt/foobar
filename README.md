## Solutions to a selection of Google FooBar challenges

Other than the first, these are level 3-5 challenges.

------------------
###  Shortest path on a chessboard

#### Problem
For a rectangular chessboard of given dimensions `[M,N]` and two positions on the board `(x_A,y_A), (x_B,y_B)` write a function `solution([M,N],(x_A,y_A),(x_B,y_B)` which gives the fewest number of moves a Knight would need to get from one point to the other.

<details>
 <summary><b>Solution</b></summary>
 <p></p>
 <b>Outline</b> / <a href="shortest-path-on-chessboard.py">Code</a> / <a href="test_shortest-path-on-chessboard.py">Tests</a>
 <p></p>
 
We observe that the distances from the Knight can be thought of as ‘octagonal frames’ of width 2 squares. By mirroring so that the distination is at an origin, and the Knight in the upper right quadrant, one can easily describe shortest paths between frames till the 3x3 in which the Knight sits (at the bottom left), which can be written explicitly after some algebra (thus achieving constant time).

</details>
 
<details>
 <summary><b>Examples</b></summary>
 <p></p>

`solution([10000,4000],(3927,31),(477,1022)) = 1725` (0.0000152 sec)

`solution([64,64],(0,0),(1,1)) = 4` (0.0000201 sec)
 
 </details>

------------------
### Partitions of N with distinct terms

#### Problem
Create a function `solution(N)` for `2 < N < 200` which outputs the number of ways of stacking `N` identical blocks to form of a staircase, such that each step is 1 block wide & long, and there are at least 2 steps.

<details>
 <summary><b>Solution</b></summary>
 <p></p>
 <b>Outline</b> / <a href="partitions-with-distinct-terms.py">Code</a> / <a href="test_partitions-with-distinct-terms.py">Tests</a>
 <p></p>
 
This asks for the number of subsets of {1 ... N-1} which sum to N. The idea is to categorise partitions of integers by conditioning on the largest integer in each partition (for instance, partitions of 11 can be categorised as having largest digit 10 (just {10,1}), or 9 (just {9,2}), or 8 ({8,3} and {8,2,1}) and so on). In particular we label <code>C[i,j]</code> as the numbers of staircases with (i + 1) blocks and final step height ≤ j, computed by summing `C[i-k,k-1]` over suitable k, where k is the final step height for the (i + 1) block staircase. This is done within a matrix `C` to facilitate the diagonal sums and filling sections of rows which do not require compution. This could most likely be improved upon though by not storing as much information.
 
</details>

<details>
 <summary><b>Examples</b></summary>
 <p></p>

`solution(50) = 3657` (0.005642 sec)

`solution(200) = 487067745` (0.362902 sec)
 
 </details>

------------------
### Rays on the 2-dimensional integer lattice

#### Problem
In a rectangular room of given dimensions (no larger than `1500 x 1500`) and two integer-coordinate positions (a reference and a target, strictly inside the room), create a function `solution(room_dim,ref_pos,tgt_pos,max_distance)` which returns the number of ways a laser beam can travel from the reference point to the target if it is allowed to bounce off walls in the obvious way; the laser can be pointed in any direction. In addition, the distance the beam can travel is bounded by some given integer value at most `10,000`, and the beam must not hit the reference point before the target.

<details>
 <summary><b>Solution</b></summary>
 <p></p>
 <b>Outline</b> / <a href="rays-on-integer-lattice.py">Code (Python)</a> / <a href="rays-on-integer-lattice.c">Code (C)</a> / <a href="test_rays-on-integer-lattice.py">Tests</a>
 <p></p>
 
The room is thought of as mirrored on the integer lattice so that the beam travels in a single straight line. Unit vectors are computed for mirrored reference and target points which allows the conditions (total distance, discarding beam hitting reference first) to be checked easily, and suitable unit vectors are added to the desired set. This is at its most demanding when the ratio of the maximal beam distance to room size is large.
</details>
<details>
 <summary><b>Examples</b></summary>
 <p></p>

`solution([6,7],[2,3],[3,5],1000) = 73070` (0.84456 sec)

`solution([623,197],[2,3],[38,502],5200) = 690` (0.01556 sec)

 </details>
 
------------------
### Absorption probabilities 

#### Problem
An exotic chemical can be in some given number `N` of states with `N ≤ 10`. In discrete time, the material is able shift state. To each state is associated an array of length `N` describing the likelihood  of shifting from that state to each of the `N` others (as a ratio of `N` integers). For instance if state 2 is given the array `[0, 1, 3, 1]`, then in state 2, we would shift to states 0, 1, 2, 3 with likelihood 1 : 0 : 3 : 1. In other words a `1/5` chance of entering state 0 or 3, a `0` chance of entering states 1, and a `3/5` chance of remaining in state 2. A state is terminal if it consists of only 0s, and the starting state is state 0.

Create a function `solution(M)` which, given an list of arrays `M`, where each array is associated to each state, returns the exact probabilities of ending in each of the terminal states, expressed as an list of numerators with a common denominator at the end (e.g. if states 4 and 6 are terminal, the output should look like `[a, b, d]` where `a/d` and `b/d` are the probabilities of ending in state 4 and 6 respectively). In any state, it is guaranteed that there is a path towards a terminal state (in other words,`M` will always be such that there is a positive probability of ending in a terminal state).

<details>
 <summary><b>Solution</b></summary>
 <p></p>
 <b>Outline</b> / <a href="absorption-probabilities.py">Code</a> / <a href="test_absorption-probabilities.py">Tests</a>
 <p></p>
 
We create a ‘non-normalised’ stochastic matrix `Q` by correcting empty rows of `M` with a 1 on the diagonal entry (normalising other rows to make the matrix classically stochastic is not necessary and likely to induce float errors). For each terminal state, the probability of reaching it from state 0 can then be computed from the inverse of `Q` minus an incomplete identity matrix `J` (no 1s in terminal rows); in fact it suffices to get the top row of the adjugate, for columns whose index matches terminal rows indices. This is straightforward determinant computation, and finally the determinant of the `Q-J` is found, since its the inverse elements are those from the adjugate divided by this determinant. Gcd and moduli then give the required format.

</details>
<details>
 <summary><b>Examples</b></summary>
 <p></p>

`solution([[1,0,4,5,0,0,3],
           [3,0,2,0,1,1,7],
           [0,0,0,0,0,0,0],
           [9,0,8,0,0,0,1],
           [0,0,3,5,0,2,8],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]) = [112, 0, 59, 171]` (0.000288 sec)
 
 </details>

------------------
### Maximal pairing of integers

#### Problem
The following operator is defined on pairs of positive integers: `(a,b)` leads to `(2a,b - a)` if `a < b` (WLOG) and halts if `a = b`. Applied repeatedly this operator either eventually halts or cycles. Then, given a list of integers of length between `1` and `100`, with entries between `1` and `20^30 - 1`, the problem asks for `solution(list_ints)` to return the minimal size of a sublist with the property that all integers not in it can be paired to cycle indefinitely.

<details>
 <summary><b>Solution</b></summary>
 <p></p>
 <b>Outline</b> / <a href="maximal-pairing-of-integers.py">Code (Python)</a> / <a href="maximal-pairing-of-integers.cpp">Code (C++)</a> / <a href="test_maximal-pairing-of-integers.py">Tests</a>
 <p></p>
 
For a pair `(a,b)` the cycling condition simply translates to neither `a` nor `b` being divisible by the odd part of their sum (that is, `a + b` divided by the largest power of 2 which divides `a + b`). Set up a list of pairs where each pair gives the distinct elements from the original list coupled with their number of occurrences. Sort in ascending order on the first entry, check whether elements fit the looping condition with further elements, removing instances of both when they do: for instance if there are 17 x 1s, 13 x 2s, 9 x 3s, 6 x 5s, then the list of pairs begins `[(1,17), (2,13), (3,9)  ...]`. `(1,2)` loop, so removing will update the list of pairs to `[(1,4), (3,9), (5,6) ...]`. `(1,3)` do not loop, `(1,5)` do, update to `[(3,9), (5,2) ...]` etc. If a pair cannot be looped with any further elements, record the second entry of this pair and discard.

 </details>
 <details>
 <summary><b>Examples</b></summary>
 <p></p>
 
`solution([1,1,1,2,5,3,1,1,1,9,15,3,4,3,3,10,4,5,4,3]) = 4` (0.000068 sec)

`solution([k for k in range(1,1000)]) = 1` (0.036142 sec)
 </details>

------------------
### Non-equivalent colourings of a rectangular board

#### Problem
Given a rectangular board and `c` colours, call 2 colourings equivalent if it is possible to get from one to the other by swapping rows and columns in some order. Create a function `solution(dim_x,dim_y,colours)` which returns the number of non-equivalent colourings of a board with given dimensions & number of colours.

<details>
 <summary><b>Solution</b></summary>
 <p></p>
 <b>Outline</b> / <a href="non-equivalent-colourings.py">Code</a> / <a href="test_non-equivalent-colourings.py">Tests</a>
 <p></p>
 
We use Polyá’s enumeration theorem to produce a comparatively efficient solution. Rows and columns are independent, for each compute partitions of the integer length of each. Each partition is viewed as splitting distinguishable rows (or columns), symmetries are then computed combinatorially.
For each such partition, the corresponding cycle index term is found, and computed for the required number of colours `c`. This is then summed and divided by the number of row/column-permutations of the broad/matrix, that is `dim_x!dim_y!` by independence.

 </details>
 <details>
 <summary><b>Examples</b></summary>
 <p></p>

`solution(10,5,1000) = 2296443268665594227660199884442974721785919717032266018985550162929588679709764322189156301210227255204184301166149921785333257938229173812500` (0.0019321 sec)

`solution(18,18,100000) = 24395962632753253791129531502508730127518803639073498835204478895373479737453554702189271402974410721793642417841347146743340546665972944007229689855945730008785555783111480715231631414277449021004711070148362101472942395444677339361338053183678215117539163090728025854049372681861509929518532749314842706230542380382848204238989704909721847046131172943580670274752588425568453611331625343144545633212422844750859782489493640890165569525862910843278157310358493737405257296248586151161867571568619986956951699467450712544918252483333324370464878076815008362353737750749639918914362280077623341440121391832920686820805696133292293997171882362176960515802692343722912317123320991230015759301600404772767335418262630012678387790545060100086079122169592143606647638398478298418913113077944753196041158602932308857489528232088946105491748207829171387866560621184038870773716928334859773415693785514529914006789956310873508573279998358458494629312624318804120231400625269124715134511628186459629054690641707843736118385603402026946618385326807685640817578741726629261906166097218901173942126037610181301365649842985553132136267521381781747213309424017602083436634982843148202798782333481529685233232889268976885256993538470300728744250020644149549633292114993010862719474745070651171865738878213711733655127362904868629497077317333687933604745798276384800215184387294388838195468428121294223680231944740789082982454570957452129959852439606177079218310336210627481415926344544843256406107050511770284556334647255314479698498953134941685262646862724084193002296279657609957084304329726646000000000` (0.627063 sec)
 
 </details>
