#include <cstdio>
#include <stdlib.h>
#include <random>
#include <gem5/m5ops.h>

#define GEM5

int main(int argc, char * argv[])
{
  const int N = atoi(argv[1]);
  int X[N], Y[N], alpha = 2;
  for (int i = 0; i < N; ++i)
  {
    X[i] = rand()%100;
    Y[i] = rand()%100;
  }
  
  // Start of iaxpy loop
  #ifdef GEM5
  m5_dump_reset_stats(0,0);
  for (int i = 0; i < N; ++i)
  {
    Y[i] = alpha * X[i] + Y[i];
  }
  m5_dump_reset_stats(0,0);
  #endif
  // End of iaxpy loop

  int sum = 0;
  for (int i = 0; i < N; ++i)
  {
    sum += Y[i];
  }
  printf("%lf\n", sum);
  return 0;
}
