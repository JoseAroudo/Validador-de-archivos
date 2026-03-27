import re

# Compilar regex una sola vez
Alfanum15 = re.compile(r'^[A-Za-z0-9]{0,15}$')
Alfanum11 = re.compile(r'^[0-9]{0,11}$')
Alfanum12 = re.compile(r'^Frt[A-Za-z0-9]{0,12}$') #, re.IGNORECASE)
num11= re.compile(r'^\d{1,11}$')
num6= re.compile(r'^\d{1,6}$')