def code(symbol, move):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if symbol in lowercase:
        index = lowercase.index(symbol) + move
        if index >= 26:
            index -= 26
        return lowercase[index]
    elif symbol in capital:
        index = capital.index(symbol) + move
        if index >= 26:
            index -= 26
        return capital[index]
    else:
        return symbol


def caesar_cipher(text):
    move = -1

    result = [code(text[i], move) for i in range(len(text))]

    moved_string = ''.join(result)
    moved_text = moved_string.split(' ')

    decode(moved_text)


def format_text(text):
    print('Decoded text:')

    for i in range(len(text)):
        for j in range(len(text[i])):
            if '(' in text[i][j]:
                text[i][j] = text[i][j].replace('(', '`')
            elif '+' in text[i][j]:
                text[i][j] = text[i][j].replace('+', '*')
            elif '.' in text[i][j]:
                text[i][j] = text[i][j].replace('.', '-')
        decode_str = ' '.join(text[i])

        print(decode_str)


def decode(moved_text):
    moved_string = []
    new_text = []
    result_word = ''
    result_string = []
    result_text = []

    for i in range(len(moved_text)):
        moved_string.append(moved_text[i])

        if '/' in moved_text[i]:
            new_text.append(moved_string)
            moved_string = []

    for i in range(len(new_text)):
        step = 0
        for j in range(len(new_text[i][0])):
            if new_text[i][0][j].isupper():
                step = len(new_text[i][0]) - j
                break

        new_step = 0
        for j in range(len(new_text[i])):
            if '/' in new_text[i][j]:
                new_text[i][j] = new_text[i][j].replace('/', '')

            if step >= len(new_text[i][j]):
                new_step %= len(new_text[i][j])
            else:
                new_step = step

            for k in range(-new_step, 0):
                result_word += new_text[i][j][k]
            for k in range(-len(new_text[i][j]), -new_step):
                result_word += new_text[i][j][k]

            result_string.append(result_word)
            result_word = ''

        result_text.append(result_string)
        result_string = []

    format_text(result_text)


def the_truth():
    text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf ' \
           'jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp ' \
           'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst ' \
           'tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq ' \
           'up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn ' \
           'puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs ' \
           'boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt ' \
           'fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

    caesar_cipher(text)


the_truth()
