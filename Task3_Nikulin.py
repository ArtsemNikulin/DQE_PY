import re

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

# 2 - create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
last_elements = re.findall(r"\w+(?=[.])", text)  # I find last words of each sentence
sentence_to_add = ' '.join(last_elements)  # I join last words in one sentence
text_with_new_sentence = ""

print(f'\nThis sentence need to add: {sentence_to_add}')

list_of_text = re.split('(^|[.]\s|\n\t)', text)  # I create list of text splits

for index, i in enumerate(list_of_text):  # I create a loop that finds a paragraph which needs to add the sentence
    if i == 'also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph':
        list_of_text[index] = i + '. ' + sentence_to_add
        for each_split in list_of_text:  # I create a loop that create new text
            text_with_new_sentence = ''.join(list_of_text)
            text_with_new_sentence = text_with_new_sentence.replace('x“', 'x “')

print(f'\nThis is text with new sentence:\n {text_with_new_sentence}')

# 3 - normalize text

text_with_norm_case = ""

for i in re.split('(^|[.]\s|\n\t)', text_with_new_sentence):  # I use regexp to multiple conditions of split
    text_with_norm_case += i.capitalize()

print(f'\n Text with normal word case is:\n{text_with_norm_case}')

# 4 - It iz misspelling here. Fix“iz” with correct “is”, but only when it iz a mistake.

final_text = text_with_norm_case.replace(' iz ', ' is ')

print(f'\n Final text is: \n {final_text}')