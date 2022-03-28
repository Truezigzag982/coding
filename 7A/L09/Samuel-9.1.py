import jieba
import jieba.posseg as pseg

text = u'吃葡萄不吐葡萄皮不吃葡萄倒吐葡萄皮'
seg_list = jieba.cut(text, cut_all=True)
print('full mode: ' + '/'.join(seg_list))

seg_list = jieba.cut(text, cut_all=False)
print('default mode: ' + '/'.join(seg_list))

seg_list = jieba.cut_for_search(text)
print('search engine mode: ' + '/'.join(seg_list))

seg_list = jieba.lcut(text)
print('list: ' + '/'.join(seg_list))
