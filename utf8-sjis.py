import codecs

def convert_encoding(input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_sjis.' + input_file.rsplit('.', 1)[1]
    with codecs.open(input_file, 'r', 'utf-8') as f_in:
        with codecs.open(output_file, 'w', 'shift_jis') as f_out:
            for line in f_in:
                f_out.write(line)

# 使用例
input_file = input("変換したいファイルのパスを入力してください: ")

convert_encoding(input_file)
