# Task: Write a program that will receive various brainfuck programs as arguments and execute each program in turn.
# https://code.golf/brainfuck#python


# -------- ORIGINAL (205 chars) --------
import sys
for P in sys.argv:
 o="A=[0]*99;p=0";l=0
 for c in P:o+="\n"+" "*l+"p+=1|p-=1|A[p]+=1|A[p]-=1|print(end=chr(A[p]))|while A[p]:|".split("|")["><+-.[]".index(c)];l+=(c in"[]")*(92-ord(c))
 exec(o)
# --------------------------------------


# ------- COMPRESSED (162 chars) -------
exec(''.join(chr(ord(c)>>8&255)+chr(ord(c)&255)for c in"業灯牴⁳祳੦潲⁐⁩渠獹献慲杶㨊⁯㴢䄽嬰崪㤹㭰㴰∻氽《⁦潲⁣⁩渠债漫㴢屮∫∠∪氫≰⬽ㅼ瀭㴱籁孰崫㴱籁孰崭㴱籰物湴⡥湤㵣桲⡁孰崩⥼睨楬攠䅛灝㩼∮獰汩琨≼∩嬢㸼⬭⹛崢⹩湤數⡣⥝㭬⬽⡣⁩渢孝∩⨨㤲ⵯ牤⡣⤩ਠ數散⡯⤠"))
# --------------------------------------
