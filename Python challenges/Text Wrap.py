import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    output_text = ''
    for line in wrapper.wrap(text=string):
        output_text += line + '\n'
    return output_text

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)