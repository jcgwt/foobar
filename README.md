# foobar
## Solutions to a selection of Google FooBar challenges

### The grandest staircase of them all

For given 2 < N < 200, find the number of ways of stacking N identical blocks to form of a staircase, such that each step is 1 block wide & long. In other words, this problem wants the number of subsets of {1, …, N-1} which sum to N. 

The main idea is to break up partitions according to the height of final steps recursively. In particular we label C[i,j] as the numbers of staircases with (i+1) blocks and final step height ≤ j, computed by summing C[i-k,k-1] over suitable k, where k is the final step height for the (i+1) block staircase. This is done within a matrix C to facilitate the diagonal sums.

###  Knight’s problem

Given an N x N chessboard and two positions, find the fewest number of moves it would require a Knight to get from one point to the other.

We observe that the distances from the Knight can be thought of as ‘octagonal frames’ of width 2 squares. By mirroring so that the Knight is at an origin, with destination in the upper right quadrant, one can easily describe shortest paths between frames till the 3x3 in which the Knight sits (at the bottom left), which can be written explicitly after some algebra.

### Bring a gun to a trainer fight

In a rectangular room of given dimensions (no larger than 1250x1250) and two integer-coordinate positions (a reference and a target, strictly inside the room), find the number of ways a laser beam can travel from the reference point to the target if it is allowed to bounce off walls in the obvious way; in addition, the distance the beam can travel is bounded by some given integer value at most 10,000, and the beam must not hit the reference point before the target.

The room is thought of as mirrored on the integer lattice so that the beam travels in a single straight line. Unit vectors are computed for mirrored reference and target points which allows the conditions (total distance, discarding beam hitting reference first) to be checked easily, and suitable unit vectors are added to the desired set.

### Doomsday Fuel

An exotic chemical can be in some given number N of states with N≤10. In discrete time, the material is able shift state. To each state is associated an array of length N describing the likelihood  of shifting from that state to each of the N others (as a ratio of N integers). For instance if state 2 is associated with [0,1,3,1] then in state 2, we will shift to states 0, 1, 2, 3 with likelihood 1:0:3:1 i.e. 0.2 chance of entering state 0 or 3, 0 chance of entering states 1, and 0.6 chance of remaining in state 2. A state is terminal if it consists of only 0s, and the starting state is state 0.

Given a matrix M whose rows are the arrays associated to each state, find the exact probabilities of ending in each of the final states, expressed as an array of numerators with a common denominator as at the end (e.g. if states 4 and 6 are terminal, the output should look like [a, b, d] where a/d and b/d are the probabilities of ending in state 4 and 6 respectively).

We create a ‘sort-of’ stochastic matrix by correcting empty rows (without normalising; not necessary and likely to induce float errors). For each terminal state, the probability of reaching it from state 0 can then be computed from the inverse of M minus an incomplete identity matrix J (no 1s in terminal rows); in fact it suffices to get the top row of this inverse (or rather the adjugate), at columns whose index matches terminal rows indices. This is straightforward determinant computation, and finally the determinant of the M-J is found, since its the inverse elements are those from the adjugate divided by this determinant. Gcd and moduli then give the required format.

### Distract the trainers

The original problem is worded in terms of bananas and bunnies, but it essentially defines the following operator on pairs of positive integers (a,b) -> (2a,b-a) (WLOG a < b) or halts if a = b. Applied repeatedly this operator either eventually halts or cycles. Then, given a list of integers of length between 1 and 100, with entries between 1 and 20^30-1, the problem asks to return the fewest number of elements such that all others can be paired to cycle indefinitely.

For a pair (a,b) the cycling condition simply translates to neither a nor b being divisible by the odd part of their sum (that is, their sum divided by its largest power of 2). Organise as the list’s elements with their number of occurrences in the list, sort in ascending order, check whether elements fit the looping condition with further elements, removing instances of both when they do, else appending to a list of ‘impossibles’.

### Hey I already did that

Given some number N in base b (as a string) of length k, the following process is done: let x,y be the digits of N in ascending and descending order respectively, compute y - x and correct with 0s to preserve length k if necessary. Repeat with N = y - x. This eventually cycles. Create a function which takes in N and b and returns the length of this cycle (length 1 if the sequence reaches a constant value)

Because most functions in Python return/operate in base-10, it is easiest and without real computational issues to switch between base-10 and base-b at each iteration. The solution is otherwise what one would expect.

### Disorderly escape

Given an MxN board and C colours, call 2 colourings equivalent if it is possible to get from one to the other by swapping rows and columns in some order. Create a function which returns the number of non-equivalent colourings of the board with the given number of colours.

We use Polyá’s counting theorem to produce a comparatively efficient solution. Rows and columns are independent, for each compute partitions of the integer length of each. Each partition is viewed as splitting distinguishable rows (or columns), symmetries are then computed combinatorially.
For each such partition, the corresponding cycle index term is found, and computed for the required number of colours c. This is then summed and divided by the number of row/column-permutations of the broad/matrix, that is M!N! by independence.

To illustrate efficiency, for an 18x18 board with 100,000 colours it takes 0.64628 seconds to output the following number of non-equivalent colourings:

`24395962632753253791129531502508730127518803639073498835204478895373479737453554702189271402974410721793642417841347146743340546665972944007229689855945730008785555783111480715231631414277449021004711070148362101472942395444677339361338053183678215117539163090728025854049372681861509929518532749314842706230542380382848204238989704909721847046131172943580670274752588425568453611331625343144545633212422844750859782489493640890165569525862910843278157310358493737405257296248586151161867571568619986956951699467450712544918252483333324370464878076815008362353737750749639918914362280077623341440121391832920686820805696133292293997171882362176960515802692343722912317123320991230015759301600404772767335418262630012678387790545060100086079122169592143606647638398478298418913113077944753196041158602932308857489528232088946105491748207829171387866560621184038870773716928334859773415693785514529914006789956310873508573279998358458494629312624318804120231400625269124715134511628186459629054690641707843736118385603402026946618385326807685640817578741726629261906166097218901173942126037610181301365649842985553132136267521381781747213309424017602083436634982843148202798782333481529685233232889268976885256993538470300728744250020644149549633292114993010862719474745070651171865738878213711733655127362904868629497077317333687933604745798276384800215184387294388838195468428121294223680231944740789082982454570957452129959852439606177079218310336210627481415926344544843256406107050511770284556334647255314479698498953134941685262646862724084193002296279657609957084304329726646000000000`

