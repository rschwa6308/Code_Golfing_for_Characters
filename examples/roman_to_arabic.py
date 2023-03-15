# Task: For each numeric argument in Roman numerals, print the same number in Arabic numerals.
# https://code.golf/roman-to-arabic#python


# -------- ORIGINAL (156 chars) --------
import sys
d=dict(zip('IVXLCDM',[1,5,10,50,100,500,1000]))
for a in sys.argv[1:]:print(sum(d[x]*(i<len(a)-1and-(d[x]<d[a[i+1]])or 1)for i,x in enumerate(a))) 
# --------------------------------------


# ------- COMPRESSED (138 chars) -------
exec("".join(chr(ord(x)>>8&255)+chr(ord(x)&255)for x in"業灯牴⁳祳੤㵤楣琨穩瀨❉噘䱃䑍✬嬱ⰵⰱ〬㔰ⰱ〰ⰵ〰ⰱ〰そ⤩੦潲⁡⁩渠獹献慲杶嬱㩝㩰物湴⡳畭⡤學崪⡩㱬敮⡡⤭ㅡ湤⴨摛硝㱤孡孩⬱嵝⥯爠ㄩ景爠椬砠楮⁥湵浥牡瑥⡡⤩⤠"))
# --------------------------------------
