#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a = 300;
  float n = 0.0;
  float i;
  float j = -1.0;

  for (i = 0.0; i < a; i++)
    {
      j = j * (-1);
      n = n + (float)(4 * j / (float)(2 * i + 1));
    }
  printf("The pi approximation after sum of %d fractions is %0.8f\n", a, n);
  return (0);
}
