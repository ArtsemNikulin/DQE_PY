text = """homEwork: 
    tHis iz your homeWork, copy these Text to variable. 
    
    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    
    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
    
    last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# 1 - calculate number of whitespace characters in this text
count = 0

for i in range(len(text)):
    if text[i].isspace():  # I use isspace() method since it return True for all whitespaces
        count += 1
print(f'Total number of whitespaces in the text is: {count}')

# 2 - normalize text

