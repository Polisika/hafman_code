import PySimpleGUI as Sg
import functions as f
import input
import logging
import output
from collections import Counter


char_out = '''{0}
Энтропия: {1}
Избыточность: {2}
Средняя длина слова: {3}
Неравенство Крафта: {4}
'''

if __name__ == '__main__':
    outInfo = Sg.Output(size=(88, 6))
    outCodedText = Sg.Output(size=(88, 15))
    outDecodedText = Sg.Output(size=(88, 15))
    layout = [
        [Sg.Text('Probability'), Sg.InputText(), Sg.FileBrowse()],
        [Sg.Text('Text'), Sg.InputText(), Sg.FileBrowse()],
        [Sg.Submit("Code text")],
        [outInfo],
        [outCodedText],
        [Sg.Submit("Decode text")],
        [outDecodedText],
        [Sg.Cancel()]
    ]
    window = Sg.Window('Lab №2, Hafman\'s code', layout)
    dict_coded = {}
    while True:  # The Event Loop
        event, values = window.read()
        try:
            if event in (None, 'Exit', 'Cancel'):
                break
            elif event == "Code text":
                if values[0] and values[1]:
                    p = input.input_probability(values[0])
                    p.sort(reverse=True)
                    c = Counter()
                    text = input.input_text(values[1])
                    c.update(text)
                    a = [num for num, s in c.most_common()]
                    i = 0
                    while len(p) > len(a):
                        a.append('Unused symbol ' + str(i))  # Make len equals for correct work Hafman's algorithm.
                        i += 1
                    dict_coded = f.hafman(p, a)
                    outInfo.update(char_out.format(
                        dict_coded,
                        f.entropy(p),
                        f.redundancy(p),
                        f.average_codeword(dict_coded.values()),
                        f.crafting_inequality(dict_coded.values()),
                    ))
                    text = f.code_text(text, dict_coded)
                    outCodedText.update(text)
                    output.output("ResultCode.txt", text)
            elif event == "Decode text":
                with open("ResultCode.txt", 'r') as result_code:
                    text = result_code.read()
                text = f.decode_text(text, dict_coded)
                outDecodedText.update(text)
                output.output("ResultDecode.txt", text)
            else:
                print("Choose files")
        except BaseException as e:
            logging.error(e)
