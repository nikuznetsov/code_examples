'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

num = 0
dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
        8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16:'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

for i in range(1,1001):
    if len(str(i)) == 1:
        num += len(dict.get(i))
    if len(str(i)) == 2:
        if (9 < i < 20) or (i % 10 == 0):
            num += len(dict.get(i))
        else:
            num += len(dict.get( (i // 10) * 10) ) + len(dict.get(i % 10))
    if len(str(i)) == 3:
        num += len(dict.get(i // 100)) + 7 
        if (str(i)[1] == '1') or ((i % 100) % 10 == 0):
            num += len(dict.get(i % 100))
        else:
            num += len(dict.get( ( (i % 100) // 10) * 10) ) + len(dict.get(i % 10))   
        if (str(i)[1] != '0') or (str(i)[2] != '0'):
            num += 3
    if len(str(i)) == 4:
        num += 11
print(num)
