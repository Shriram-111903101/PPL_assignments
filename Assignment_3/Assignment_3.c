// C program to find factorial of given number
#include <stdio.h>

// function to find factorial of given number
unsigned int factorial(unsigned int n)
{
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

int main()
{
    int num = 5;
    printf("Factorial of %d is %d", num, factorial(num));
    return 0;
}

/*
   0x0000000000001178 <+0>:     endbr64
   0x000000000000117c <+4>:     push   %rbp
   0x000000000000117d <+5>:     mov    %rsp,%rbp
   0x0000000000001180 <+8>:     sub    $0x10,%rsp
   0x0000000000001184 <+12>:    movl   $0x5,-0x4(%rbp)
   0x000000000000118b <+19>:    mov    -0x4(%rbp),%eax
   0x000000000000118e <+22>:    mov    %eax,%edi
   0x0000000000001190 <+24>:    callq  0x1149 <factorial>
   0x0000000000001195 <+29>:    mov    %eax,%edx
   0x0000000000001197 <+31>:    mov    -0x4(%rbp),%eax
   0x000000000000119a <+34>:    mov    %eax,%esi
   0x000000000000119c <+36>:    lea    0xe61(%rip),%rdi        # 0x2004
   0x00000000000011a3 <+43>:    mov    $0x0,%eax
   0x00000000000011a8 <+48>:    callq  0x1050 <printf@plt>
   0x00000000000011ad <+53>:    mov    $0x0,%eax
   0x00000000000011b2 <+58>:    leaveq
   0x00000000000011b3 <+59>:    retq

   */
