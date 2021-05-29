#include <stdio.h>
#include <stdlib.h>

/**
 * pi_calc - function to calculate pi
 */
int pi_calc(int a)
{
  long double n = 0;
  int i, j = -1;

  for (i = 1; i < a; i++)
    {
      j = j * (-1);
      n = n + (long double)(4 * (1 / (2 * i - 1)) * j);
    }
  return (n);
}

/**
 * main - print pi with decimal place of i
 */
int main(int argc, char *argv[])
{
  int i = atoi(argv[1]);
  long double pi;
  
  if (argc != 2)
    {
      printf("Error\n");
      return (1);
    }
  pi = pi_calc(i);
  printf("The first %d digit/digits of pi is %0.10Lf\n", i, pi);
  return (0);
}
