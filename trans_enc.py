import codecs
import pathlib
import re

def convert_encoding(input_file, output_file_endwith='_sjis', in_encoding='utf-8', out_encoding='CP932'):
    input_file_path = pathlib.Path(re.sub(r'\\ ', ' ', str(input_file)))
    output_file = input_file.rsplit('.', 1)[0] + output_file_endwith + '.' + input_file.rsplit('.', 1)[1]
    with codecs.open(input_file_path, 'r', in_encoding) as f_in:
        with codecs.open(output_file, 'w', out_encoding) as f_out:
            for line in f_in:
                f_out.write(line)

if __name__ == '__main__':
    # 使用例
    input_file = input("変換したいファイルのパスを入力してください: ")

    convert_encoding(input_file)
