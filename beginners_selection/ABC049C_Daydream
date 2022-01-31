# -*- coding: utf-8 -*-
s =  input()[::-1]
reverse_words = ["maerd", "remaerd", "esare", "resare"]

# 先頭から1文字ずつ足していき、reverse_wordsとマッチしたらリセット
tmp = ""
for i in range(len(s)):
  tmp += s[i]
  if tmp in reverse_words:
    tmp = ""


if len(tmp) == 0:
  print("YES")
else:
  print("NO")
