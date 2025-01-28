# Base8-to-Base3-Turing
A Python program designed to convert numbers from base 8 (octal) to base 3 (ternary), inspired by the workings of a Turing machine. The program uses custom algorithms to simulate the step-by-step logic of a Turing machine for base conversion.

## How It Works

### - Algorithm
```
Tape: 12
      ^
Tape: 12#0
         ^
Tape: 12#0
       ^
Tape: 11#0
       ^
Tape: 11#0
        ^
Tape: 11#0
         ^
Tape: 11#0
          ^
Tape: 11#0
         ^
Tape: 11#1
        ^
Tape: 11#1
        ^
Tape: 11#1
       ^
Tape: 10#1
       ^
Tape: 10#1
        ^
Tape: 10#1
         ^
Tape: 10#1
          ^
Tape: 10#1
         ^
Tape: 10#2
        ^
Tape: 10#2
        ^
Tape: 10#2
       ^
Tape: 17#2
      ^
Tape: 07#2
      ^
Tape: 07#2
       ^
Tape: 07#2
        ^
Tape: 07#2
         ^
Tape: 07#2
          ^
Tape: 07#2
         ^
Tape: 07#0
        ^
Tape: 07#1
         ^
Tape: 07#1
          ^
Tape: 07#10
         ^
Tape: 07#10
        ^
Tape: 07#10
        ^
Tape: 07#10
       ^
Tape: 06#10
       ^
Tape: 06#10
        ^
Tape: 06#10
         ^
Tape: 06#10
          ^
Tape: 06#10
           ^
Tape: 06#10
          ^
Tape: 06#11
         ^
Tape: 06#11
        ^
Tape: 06#11
        ^
Tape: 06#11
       ^
Tape: 05#11
       ^
Tape: 05#11
        ^
Tape: 05#11
         ^
Tape: 05#11
          ^
Tape: 05#11
           ^
Tape: 05#11
          ^
Tape: 05#12
         ^
Tape: 05#12
        ^
Tape: 05#12
        ^
Tape: 05#12
       ^
Tape: 04#12
       ^
Tape: 04#12
        ^
Tape: 04#12
         ^
Tape: 04#12
          ^
Tape: 04#12
           ^
Tape: 04#12
          ^
Tape: 04#10
         ^
Tape: 04#20
        ^
Tape: 04#20
        ^
Tape: 04#20
       ^
Tape: 03#20
       ^
Tape: 03#20
        ^
Tape: 03#20
         ^
Tape: 03#20
          ^
Tape: 03#20
           ^
Tape: 03#20
          ^
Tape: 03#21
         ^
Tape: 03#21
        ^
Tape: 03#21
        ^
Tape: 03#21
       ^
Tape: 02#21
       ^
Tape: 02#21
        ^
Tape: 02#21
         ^
Tape: 02#21
          ^
Tape: 02#21
           ^
Tape: 02#21
          ^
Tape: 02#22
         ^
Tape: 02#22
        ^
Tape: 02#22
        ^
Tape: 02#22
       ^
Tape: 01#22
       ^
Tape: 01#22
        ^
Tape: 01#22
         ^
Tape: 01#22
          ^
Tape: 01#22
           ^
Tape: 01#22
          ^
Tape: 01#20
         ^
Tape: 01#00
        ^
Tape: 01#10
         ^
Tape: 01#10
          ^
Tape: 01#10
           ^
Tape: 01#100
          ^
Tape: 01#100
         ^
Tape: 01#100
        ^
Tape: 01#100
        ^
Tape: 01#100
       ^
Tape: 00#100
       ^
Tape: 00#100
        ^
Tape: 00#100
         ^
Tape: 00#100
          ^
Tape: 00#100
           ^
Tape: 00#100
            ^
Tape: 00#100
           ^
Tape: 00#101
          ^
Tape: 00#101
         ^
Tape: 00#101
        ^
Tape: 00#101
        ^
Tape: 00#101
       ^
Tape: 07#101
      ^
Tape: 77#101
      ^
Tape: 77#101
       ^
Tape: 07#101
        ^
Tape: 00#101
         ^
Tape: 00#101
         ^
Tape: 00#101
          ^
```
The answer is: 101
### - Description
In this string, there is a separator (#)
which is on the left side of the separator for a number in base 8 and on the right side of the location for a number in base 3.
As you can see in the algorithm, our head first goes to the beginning of the numbers on the left (base 8 numbers) and subtracts one unit.
And after subtracting (if that number is not 0, because if the desired number is 0, when it subtracts it, that number becomes 7.

It continues its movement towards the end of the string (left side) to subtract one unit from a number other than zero) and goes to the string on the right (base 3 number) and adds one unit to it.

In this section, if it encounters the number 2 and adds one unit, that number will become 0 and this movement will continue until it reaches a number other than 2 and adds one unit to it and then reaches the left part (base 8 numbers) again.

