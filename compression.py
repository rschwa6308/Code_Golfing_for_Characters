BUFFER_CHAR = " "

def ascii_to_unicode(s: str) -> str:
    """map each pair of ascii chars to a single unique unicode char by concatenating the hex values of the two chars"""
    if len(s) % 2 == 1: s += BUFFER_CHAR
    o = ""
    for i in range(0, len(s), 2):
        a, b = s[i], s[i+1]
        ordinal = (ord(a) << 8) | ord(b)
        try:
            o += chr(ordinal)
        except:
            print(f"cannot convert ordinal {ordinal} to a char (generated from '{a}' + '{b}')")
    return o


def unicode_to_ascii(s: str) -> str:
    """inverse of `ascii_str_to_unicode_str`"""
    o = ""
    for c in s:
        ordinal = ord(c)
        o += chr(ordinal >> 8) + chr(ordinal & 0x00ff)
    return o




original = r"""import sys
for P in sys.argv:
 o="A=[0]*99;p=0";l=0
 for c in P:o+="\n"+" "*l+"p+=1|p-=1|A[p]+=1|A[p]-=aaaaaaaaaaaaa"""


converted = ascii_to_unicode(original)
print(converted)

back = unicode_to_ascii(converted).strip()
print(back)
