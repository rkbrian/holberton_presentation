#include <stdio.h>
#include <stdlib.h>

/**
 * pi_calc - function to calculate pi
 */
int pi_calc(int a)
{
	if (n == a)
	{
		pi_calc();
	}
	return (float(pi));
}

/**
 * main - print pi with decimal place of i
 */
int main(int argc, char *argv[])
{
	int i = atoi(argv[1]);
	float pi;

	if (argc != 2)
	{
		printf("Error\n");
		return (1);
	}
	pi = pi_calc(i)
	printf("%d\n", pi);
	return (0);
}
