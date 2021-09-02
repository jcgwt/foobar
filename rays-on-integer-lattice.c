#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// input
const int room_width = 30;
const int room_height = 27;
const int ref_x = 15;
const int ref_y = 15;
const int target_x = 18;
const int target_y = 10;
const int laser_power = 500;

typedef struct {
  int x;
  int y;
} pair;

typedef struct {
  int who;
  pair pr;
  double ds;
} triple;

const pair rf = {ref_x, ref_y};
const pair tgt = {target_x, target_y};
const pair rm = {room_width, room_height};

const int Floor(int a, int b);
double EuclDist(pair A, pair B);
int gcd (int a, int b);
int max(int n);

void SwapTuples(triple *a, triple *b);
int Partition(triple *tuples, int i, int j);
void QuickSortTuples(triple *tuples, int i, int j);

void LoadPoints(triple *pts);
pair UnitVector(pair pt, pair fr);
int CheckVector(pair *arr_of_pairs, pair *pr, int k);
int CountValidPoints(triple *pts, int N);

int main()
{
  const int number_of_pts = 2*(Floor(rf.x+laser_power, rm.x) + 1 - Floor(rf.x-laser_power, rm.x))*(Floor(rf.y+laser_power,rm.y) +1 - Floor(rf.y-laser_power,rm.y));
  triple pts[number_of_pts], sorted_pts[number_of_pts];  
  double distances[number_of_pts], aux[number_of_pts];

  LoadPoints(pts);
  QuickSortTuples(pts,0,number_of_pts-1);
  return CountValidPoints(pts, number_of_pts);
}

const int Floor(int a, int b)
{
  double x = a, y = b;
  int div_int = x/y;
  double div_float = x/y;
  if (div_int <= div_float) return div_int;
  else return div_int - 1;
}

double EuclDist(pair A, pair B)
{
  return sqrt(pow(A.x-B.x, 2) + pow(A.y-B.y, 2));
}

int max(int n)
{
  if (n > 1) return n;
  else return 1;
}

int gcd(int x, int y) 
{
  int a = abs(x);
  int b = abs(y);
  if (a*b == 0)
  { 
    if (a != 0) return a;
    else if (b != 0) return b;
    else return 1;
  }
  int r;
  while (b > 0) 
  {
    r = a%b;
    a = b;
    b = r;
  }
  return a;
}

void SwapTuples(triple *a, triple *b) 
{
  triple t = *a;
  *a = *b;
  *b = t;
}

int Partition(triple *tuples, int i, int j) 
{
  double pivot = tuples[j].ds;
  int p = i-1;
  for (int q = i; q < j; q++) 
  {
    if (tuples[q].ds <= pivot) 
    {
      p++;
      SwapTuples(&tuples[p], &tuples[q]);
    }
  }
  SwapTuples(&tuples[p + 1], &tuples[j]);
  return p+1;
}

void QuickSortTuples(triple *tuples, int i, int j) 
{
  if (i < j) 
  {
    int mid = Partition(tuples, i, j);
    QuickSortTuples(tuples, i, mid-1);
    QuickSortTuples(tuples, mid+1, j);
  }
}

pair UnitVector(pair pt, pair rf)
{
  int div = max(abs(gcd((pt.x - rf.x), (pt.y - rf.y))));
  return (pair) {(pt.x - rf.x)/div, (pt.y - rf.y)/div};
}

void LoadPoints(triple *pts)
{
  int t = 0;
  for (int p = Floor(rf.x-laser_power, rm.x); p < Floor(rf.x+laser_power, rm.x)+1; p++)
  {
    for (int q = Floor(rf.y-laser_power, rm.y); q < Floor(rf.y+laser_power, rm.y)+1; q++)
    {
      pair e = {rm.x*(p + abs(p)%2) + pow(-1, p)*tgt.x, rm.y*(q + abs(q)%2) + pow(-1, q)*tgt.y};
      pair m = {rm.x*(p + abs(p)%2) + pow(-1, p)*rf.x, rm.y*(q + abs(q)%2) + pow(-1, q)*rf.y};
      pts[t] = (triple) {1, e, EuclDist(e, rf)};
      pts[t+1] = (triple) {0, m, EuclDist(m, rf)};
      t += 2;
    }
  }
}

int CheckVector(pair *arr_of_pairs, pair *pr, int k)
{
  for (int s = 0; s <= k; s++)
  {
    if (((*pr).x == arr_of_pairs[s].x) && ((*pr).y == arr_of_pairs[s].y)) return 1;
  }
  return 0;
}

int CountValidPoints(triple *pts, int N)
{
  int valid_targets = 0;
  int t = 0;
  int i = 0;
  pair valid_pts[N];
  for (; t < N; t++)
  {
    if (pts[t].ds <= laser_power)
    {
      pair U = UnitVector(pts[t].pr, rf);
      if (CheckVector(valid_pts, &U, t) == 0)
      {
        valid_pts[i] = U;
        i++;
        valid_targets += pts[t].who;
      }
    }
  }
  return valid_targets;
}