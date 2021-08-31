#include <iostream>
#include <unordered_map>
#include <vector>

bool CompareSecondElement(const std::pair<int,int>& a, const std::pair<int,int>& b);
bool Loops(int a, int b);
std::vector<std::pair<int, int>> CountOccurences(std::vector<int> ls);
int CountMinimalLoops(std::vector<std::pair<int, int>> counts);

int main()
{
  std::vector<int> input = {};
  return CountMinimalLoops(CountOccurences(input));
}

bool CompareSecondElement(const std::pair<int,int>& a, const std::pair<int,int>& b)
{
  return a.second > b.second;
}

bool Loops(int a, int b)
{
  if (a * b == 0) return false;

  int n = a + b;
  while (n % 2 == 0) 
    n = n / 2;

  return ((a % n) * (b % n) != 0);
}

std::vector<std::pair<int, int>> CountOccurences(std::vector<int> ls)
{
  std::unordered_map<int, int> counts;
  for (int& n : ls) 
    counts[n]++;
    
  std::vector<std::pair<int, int>> v_counts(counts.begin(), counts.end());
  std::sort(v_counts.begin(), v_counts.end(), CompareSecondElement);
  return v_counts;
}

int CountMinimalLoops(std::vector<std::pair<int, int>> counts)
{
  int imposs = 0;
  auto ex_it = counts.begin();
  while (ex_it != counts.end())
  {   
    auto in_it = ex_it;
    while (in_it != counts.end())
    {
    int x = ex_it -> second;
    int y =  in_it -> second;
    if (Loops(ex_it -> first, in_it -> first))
    {
      ex_it -> second = std::max(x-y,0);
      in_it -> second = std::max(y-x,0);
      if (ex_it -> second == 0) break;
    }
    in_it = std::next(in_it, 1);
    }
  imposs += ex_it -> second;
  ex_it = std::next(ex_it, 1);
  }
  return imposs;
}