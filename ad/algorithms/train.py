from tgrocery import Grocery
import jieba

def fetch_train_src():
    """
    训练数据格式
    train_src = [('education', 'student just tried  to study British English.'),
                 ('sport', 'Yao Ming attends fame of house and gets suits retired.')]
    return train_src
    """
    f = open('train.txt')
    lines = f.readlines()
    rst = [line.strip('\n') for line in lines]
    return rst


def train_grocery(train_src):
    jieba.set_dictionary("../lib/dict.txt")
    grocery = Grocery('handleHelper')
    grocery.train(train_src)
    grocery.save()


if __name__ =="__main__":
    jieba.set_dictionary('../lib/dict.txt')
    train_grocery('../trainingfolder/train.txt')