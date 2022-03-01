text = "X-DSPAM-Confidence:    0.8475"
search = text.find('0')
number = (text[search : search + 7])
float(number)
print(number)
