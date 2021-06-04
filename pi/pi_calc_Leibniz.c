#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int a = atoi(argv[1]);
  long double n = 0.0;
  long double i;
  long double j = -1.0;

  if (argc != 2)
    {
      printf("Error: please provide a valid number\n");
      return (1);
    }
  for (i = 0.0; i < a; i++)
    {
      j = j * (-1);
      n = n + (long double)(4 * j / (long double)(2 * i + 1));
    }
  printf("Nilakantha Series: sum of %d fractions\n", a);
  printf("My approximation\n    %0.15Lf\n", n);
  printf("True pi value\n    3.141592653589793....\n");
  return (0);
}
