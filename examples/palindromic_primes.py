# Task: Print all palindromic primes under 1000.


# -------- ORIGINAL (236 chars) --------
def is_prime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

for n in range(2, 1000):
    if is_prime(n) and is_palindrome(n):
        print(n)
# --------------------------------------


# ------- COMPRESSED (124 chars) -------
exec(''.join(chr(ord(c)>>8&255)+chr(ord(c)&255)for c in"摥映楳彰物浥⡮⤺ਠ†⁦潲⁤⁩渠牡湧攨㈬⁮⤺ਠ†††⁩映渠┠搠㴽‰㨊††††††牥瑵牮⁆慬獥ਠ†⁲整畲渠呲略ਊ摥映楳彰慬楮摲潭攨温㨊††牥瑵牮⁳瑲⡮⤠㴽⁳瑲⡮⥛㨺ⴱ崊੦潲⁮⁩渠牡湧攨㈬‱〰〩㨊††楦⁩獟灲業攨温⁡湤⁩獟灡汩湤牯浥⡮⤺ਠ†††⁰物湴⡮⤠"))
# --------------------------------------
