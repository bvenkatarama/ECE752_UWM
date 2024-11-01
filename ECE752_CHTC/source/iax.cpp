#include <cstdio>
#include <stdlib.h>
#include <random>

int main(int argc, char * argv[])
{
  const int N = atoi(argv[1]);
  int X[N], Y[N], alpha = 0.5;
  std::random_device rd; std::mt19937 gen(rd());
  std::uniform_int_distribution<> dis(1,100);
  for (int i = 0; i < N; ++i)
  {
    X[i] = dis(gen);
  }
  
  // Start of iax loop
  #ifdef GEM5
  m5_dump_reset_stats(0,0);
  for (int i = 0; i < N; ++i)
  {
    Y[i] = alpha * X[i];
  }
  m5_dump_reset_stats(0,0);
  #endif
  // End of iax loop

  int sum = 0;
  for (int i = 0; i < N; ++i)
  {
    sum += Y[i];
  }
  printf("%lf\n", sum);
  return 0;
}
