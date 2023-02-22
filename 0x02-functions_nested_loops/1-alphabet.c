#include <stdio.h>
#include "main.h"

/**
 * print_alphabet
 * Description: prints the alphabet, in lowercase, followed by a new line
 * Return: Always (0) Success
*/

void print_alphabet(void)
{
    char letter = 'a';
    while (letter <= 'z') {
        printf("%c", letter);
        letter++;
    }
    printf("\n");
}
