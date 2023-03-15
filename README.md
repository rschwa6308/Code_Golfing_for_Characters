# Code Golfing for Characters (not Bytes)

Submission for [SIGBOVIK 2023](https://sigbovik.org/)

**Abstract:**
Code golf challenges are usually judged by measuring the length of the source code in bytes. However, certain venues instead count the number of characters. If a variable-length character encoding like UTF-8 is used, and non-ASCII-range characters are allowed, it becomes possible to pack more information into the same number of characters by using high-value code points. We propose a general method for Python code golf that involves compressing source code into a dense string of unicode characters which, when packaged along with a decoder, is (hopefully) shorter than the original.