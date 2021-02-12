#include "palindrome.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function that checks whether or not a
 * given unsigned integer is a palindrome.
 * @n: unsigned integer
 *
 * Return: 1 if n is a palindrome, and 0 otherwise
 */

int is_palindrome(unsigned long n)
{
	int remainder, num, rev = 0;

	num = n;

	while (n != 0)
	{
		remainder = n % 10;
		rev = rev * 10 + remainder;
		n = n / 10;
	}
	if (num == rev)
		return (1);
	else
		return (0);
}
