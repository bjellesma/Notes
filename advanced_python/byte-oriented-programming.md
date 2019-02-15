We use bytes objects to communicate with binary files output for C or other low level software.

## Two's Complement

To represent negative integers in binary, we use an opperation we call **Two's Complement** where we flip all of the bits and add 1.
Mathimatically, this works out because the two's complement will always be outside of the scope of integers.

![Two's Complement Example](https://delightlylinux.files.wordpress.com/2014/10/l12-2.png?w=620&h=504)

This works well for fixed width integers but for variable length integers, we must use sign magnitude which we simply append another bit to the front for positive/negative, 0/1

```py
# The following creates a basic binary object
bin(0b11110000)
```
If you use the bytes object in python, the string must be ASCII

A bytes object is an immutable sequence while a bytesarray object is mutable
