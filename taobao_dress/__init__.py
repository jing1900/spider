# coding=utf-8
# usr/bin/eny python

#run这个 数据库配置见mysql.txt
__author__ = 'HunterChao'

__all__ = ['Taobao']

from dict import urldict
from multiprocessing import Pool
from api import Taobao

if __name__ == '__main__':
    dics = list(urldict.values())
    pool = Pool(processes=4)
    for dic in dics:
        print(dic)
        tao = Taobao(dic)
        pool.apply_async(tao.run())
    pool.close()
    pool.join()

    print('-----*------ 结束 -----*------')