# * - coding=utf-8 - * #

if __name__ == '__main__':
    documents = []
    documents.append([])
    with open('corpus/cleaned/shibu.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '':
                documents.append([])
            else:
                documents[-1].append(line)
    # remove empty lists
    documents = list(filter(None, documents))
    f1 = open('corpus/cleaned/shibu1.txt', 'w', encoding='utf-8')
    f2 = open('corpus/cleaned/shibu2.txt', 'w', encoding='utf-8')
    for i in range((len(documents)+1)//2):
        for line in documents[i]:
            f1.write(line)
        f1.write('\n')
    for i in range((len(documents)+1)//2, len(documents)):
        for line in documents[i]:
            f2.write(line)
        f2.write('\n')
    f1.close()
    f2.close()
