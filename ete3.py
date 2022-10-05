#! /bin/python

from ete3 import Tree
t = Tree()
t.populate(15) # 随机产生15个枝的树形结构
print (t)

print t.children
print t.get_children()                   # 子节点
print t.up                               # 父节点
print t.name                             # 节点名称
print t.dist                             # 到parent的距离，或分支长度，默认1
print t.is_leaf()                        # 判断是否为leaf
print t.get_tree_root()
print t.children[0].get_tree_root()      # 根节点
print t.children[0].children[0].get_tree_root()   

for leaf in t:                           # 输出leaf节点名字
	print (leaf.name)


### 1. 遍历树 tree traversing：三种遍历方式 postorder, preorder 和 levelorder
t = Tree('((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C);', format=1)


               /-H
           /-D|
          |    \-K
       /-B|
      |   |    /-F
   /-A|    \-G|
  |   |        \-I
  |   |
  |    \-E
--|
  |        /-L
  |    /-J|
  |   |   |    /-N
  |   |    \-O|
   \-C|        \-Q
      |
      |    /-P
       \-M|
           \-S

for node in t.traverse("postorder"): # 从后向前，从上到下
	print (node.name)               
	# HKDFIGBEALNQOJPSMC

for node in t.iter_descendants("postorder"):  # 排除root节点
	print (node.name)


### 2. 搜索满足条件的节点
t = Tree( '((H:1,I:1):0.5, A:1, (B:1,(C:1,D:1):0.5):0.5);' )

D = t.search_nodes(name="D")[0]                    # 按节点名字搜索
D= t&"D"
nodes = t.search_nodes(dist=0.5)                   # 按分支长度搜索
D = t.get_leaves_by_name(name="D")                 # leaf节点名字搜索
def search_by_size(node, size):                    # 按node的子节点数目多少搜索
	"Finds nodes with a given number of leaves"
	matches = []
	for n in node.traverse():
		if len(n) == size:
			matches.append(n)
	return matches

t = Tree()
t.populate(40)
search_by_size(t, size=6)

### 3.最近共同祖先
from ete3 import Tree
t = Tree( "((H:0.3,I:0.1):0.5, A:1, (B:0.4,(C:0.5,(J:1.3, (F:1.2, D:0.1):0.5):0.5):0.5):
ancestor = t.get_common_ancestor("C", "J", "B")  # 某几个节点的最近共同祖先

### 4. 单系群检测
from ete3 import Tree
t = Tree("((((((a, e), i), o),h), u), ((f, g), j));")
print (t)
                  /-a
               /-|
            /-|   \-e
           |  |
         /-|   \-i
        |  |
      /-|   \-o
     |  |
   /-|   \-h
  |  |
  |   \-u
--|
  |      /-f
  |   /-|
   \-|   \-g
     |
      \-j


t.check_monophyly(values=["a", "e", "i", "o", "u"], target_attr="name") #False;不是单系群
t.check_monophyly(values=["a", "e", "i", "o"], target_attr="name") #TRUE，是单系群


##5.节点注释：
(t&"H").add_features(vowel=False, confidence=0.2)

for leaf in t.traverse():
	if leaf.name in "AEIOU":
		leaf.add_features(vowel=True, confidence=random.random())
	else:
		leaf.add_features(vowel=False, confidence=random.random())
print "Which are", [leaf.name for leaf in t.iter_leaves() if leaf.vowel==True]



##6. 树的比较
t1 = Tree('(((a,b),c), ((e, f), g));')
t2 = Tree('(((a,c),b), ((e, f), g));')
rf, max_rf, common_leaves, parts_t1, parts_t2 = t1.robinson_foulds(t2)

### 7. 删除node
J = t.search_nodes(name="J")[0]
removed_node = J.detach()


####8 获得子节点构成的树
t = Tree('((((H,K),(F,I)G),E),((L,(N,Q)O),(P,S)));')
t.prune(["H","F","E","Q", "P"])


### 9 给某个节点增加字节点（树）
t1 = Tree('(A,(B,C));')
t2 = Tree('((D,E), (F,G));')
t3 = Tree('(H, ((I,J), (K,L)));')

A = t1.search_nodes(name='A')[0]
# and adds the two other trees as children.
A.add_child(t2)
A.add_child(t3)

### 10. 多分支变为二分支




