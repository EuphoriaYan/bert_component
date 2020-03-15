import re
from tqdm import tqdm

def replace_quotes(s):
    s = s.replace('「', '“')
    s = s.replace('」', '”')
    s = s.replace('『', '‘')
    s = s.replace('』', '’')
    return s


def del_bom(s):
    s = s.encode('utf-8')
    s = s.replace(b'\xef\xbb\xbf', b'')
    s = s.decode('utf-8')
    return s


def cut_sent(para):
    para = re.sub('([。！？?])([^）”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^）”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(…{2})([^）”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？?][）”’])([^，。！？?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    sents = para.split("\n")
    sents = [clean_proof(s).strip() for s in sents]
    return sents


def clean_proof(sent):
    sent = re.sub('（(.)）〔(.)〕', r"\1", sent)
    sent = re.sub('〔(.+)〕', r"\1", sent)
    return sent


def clean_core():
    with open('corpus/core.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/core.txt', 'w', encoding='utf-8') as f_tar:
            for line in tqdm(f_ori):
                line = line.strip()
                line = replace_quotes(line)
                sents = cut_sent(line)
                for s in sents:
                    f_tar.write(s + '\n')


def clean_ctext():
    with open('corpus/ctext有标点语料.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/ctext.txt', 'w', encoding='utf-8') as f_tar:
            for line in tqdm(f_ori):
                line = line.strip()
                line = replace_quotes(line)
                lines = re.sub('[0-9]+ ', '\n', line).split('\n')
                for line in lines:
                    sents = cut_sent(line)
                    for s in sents:
                        if s == '【文档间的分割线】':
                            f_tar.write('\n')
                        else:
                            f_tar.write(s + '\n')


def clean_dz():
    with open('corpus/dz.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/dz.txt', 'w', encoding='utf-8') as f_tar:
            target_line = ''
            for line in tqdm(f_ori):
                line = line.strip()
                line = replace_quotes(line)
                if line:
                    target_line += line
                elif target_line:
                    sents = cut_sent(target_line)
                    for s in sents:
                        f_tar.write(s + '\n')
                    target_line = ''
                    f_tar.write('\n')


def clean_dzj():
    with open('corpus/dzj.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/dzj.txt', 'w', encoding='utf-8') as f_tar:
            target_line = ''
            for line in tqdm(f_ori):
                line = line.strip()
                line = del_bom(line)
                if line:
                    line = replace_quotes(line)
                    target_line += line
                elif target_line:
                    sents = cut_sent(target_line)
                    for s in sents:
                        f_tar.write(s + '\n')
                    target_line = ''
                    f_tar.write('\n')


def clean_gujin():
    with open('corpus/gujin.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/gujin.txt', 'w', encoding='utf-8') as f_tar:
            target_line = ''
            flag = True
            for line in tqdm(f_ori):
                if line.startswith('．'):
                    sents = cut_sent(target_line)
                    for s in sents:
                        f_tar.write(s + '\n')
                    target_line = ''
                    f_tar.write('\n')
                    flag = True
                    continue
                elif line.startswith('又'):
                    continue
                line = line.strip()
                line = del_bom(line)
                line = replace_quotes(line)
                if line:
                    target_line += line
                    if flag:
                        target_line += '\n'
                        flag = False


def clean_leishu():
    with open('corpus/leishu.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/leishu.txt', 'w', encoding='utf-8') as f_tar:
            for line in tqdm(f_ori):
                line = line.strip()
                line = replace_quotes(line)
                sents = cut_sent(line)
                for s in sents:
                    f_tar.write(s + '\n')


def clean_yiji():
    with open('corpus/yiji.txt', 'r', encoding='utf-8') as f_ori:
        with open('corpus/cleaned/yiji.txt', 'w', encoding='utf-8') as f_tar:
            target_line = ''
            flag = True
            for line in tqdm(f_ori):
                line = line.strip()
                line = del_bom(line)
                line = replace_quotes(line)
                if line:
                    target_line += line
                    if flag:
                        target_line += '\n'
                        flag = False
                elif target_line:
                    sents = cut_sent(target_line)
                    for s in sents:
                        f_tar.write(s + '\n')
                    target_line = ''
                    flag = True
                    f_tar.write('\n')


if __name__ == '__main__':
    clean_core()
    clean_ctext()
    clean_dz()
    clean_dzj()
    clean_gujin()
    clean_leishu()
    clean_yiji()

