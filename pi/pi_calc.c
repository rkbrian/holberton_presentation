#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int a = atoi(argv[1]);
  float n = 0.0;
  float i;
  float j = -1.0;

  if (argc != 2)
    {
      printf("Error: please provide a valid number\n");
      return (1);
    }
  for (i = 0.0; i < a; i++)
    {
      j = j * (-1);
      n = n + (float)(4 * j / (float)(2 * i + 1));
    }
  printf("My pi approximation after sum of %d fractions is %0.8f\n", a, n);
  printf("Is my result anywhere close to the real pi value of 3.141592653589793... ?\n");
  return (0);
}
