# inverted index algorithm more here:
from porpositional_logic_eval import *


def find(elem, d_list):
    l_return = []
    i = 0
    for x in d_list:
        if elem in x:
            l_return.append(i)
        i += 1
    return l_return, len(l_return)


def find_key(x, d):
    for y in d.keys():
        if x in y:
            return y
    return "word not in a texts"


d1 = ['i', 'did', 'enact', 'julius', 'caesar', 'i', 'was', 'kill', 'i', 'the', 'capitol', 'brutus', 'me']
d1 = set(d1)
d2 = ['i', 'so', 'let', 'it', 'be', 'with', 'caesar', 'the', 'noble', 'brutus', 'hath', 'told', 'you',
      'caesar', 'was', 'ambitious']
d2 = set(d2)
doc_list = []
doc_list.append(d1)
doc_list.append(d2)

tokens = d1.union(d2)
inv_index = {}
for x in tokens:
    tmp, tmp1 = find(x, doc_list)
    inv_index[(x, tmp1)] = tmp


def NOT(l1):
    indexes = l1
    ret_list = []
    for x in range(len(doc_list)):
        if x not in indexes:
            ret_list.append(x)
    return ret_list


def OR(l1, l2):
    tmp0 = set(l1)
    tmp1 = set(l2)
    indexes = tmp0.union(tmp1)
    ret_list = []
    for x in indexes:
        ret_list.append(x)
    return ret_list


def AND(l1, l2):
    tmp0 = set(l1)
    tmp1 = set(l2)
    indexes = tmp0.intersection(tmp1)
    ret_list = []
    for x in indexes:
        ret_list.append(x)
    return ret_list


def query_tree_evaluate(tree):
    opers = {'||': OR, '&&': AND, '~': NOT}
    leftT = tree.getLeftChild()
    rightT = tree.getRightChild()
    # pdb.set_trace()
    if leftT and not rightT:
        fn = opers[tree.getRootVal()]
        return fn(query_tree_evaluate(leftT))
    elif leftT and rightT:
        fn = opers[tree.getRootVal()]
        return fn(query_tree_evaluate(leftT), query_tree_evaluate(rightT))
    else:
        return tree.getRootVal()


def build_query_parse_tree(exp):
    exp_list = exp.replace('(', ' ( ').replace(')', ' ) ').replace('~', ' ~ ').split()
    e_tree = BinaryTree('')
    current_tree = e_tree
    for token in exp_list:
        if token == '(':
            current_tree.insertLeft('')
            current_tree = current_tree.getLeftChild()
        elif token in ['||', '&&', '->', '==', 'XR']:
            if current_tree.getRootVal() == '~':
                current_tree.getParent().setRootVal(token)
                current_tree.insertRight('')
                current_tree = current_tree.getRightChild()
            else:
                current_tree.setRootVal(token)
                current_tree.insertRight('')
                current_tree = current_tree.getRightChild()
        elif token == '~':
            current_tree.setRootVal('~')
            current_tree.insertLeft('')
            current_tree = current_tree.getLeftChild()
        elif token == ')':
            current_tree = current_tree.getParent()
        elif re.search('[a-zA-z]', token):
            current_tree.setRootVal(inv_index[find_key(token, inv_index)])
            current_tree = current_tree.getParent()
            if current_tree.getRootVal() == '~':
                current_tree = current_tree.getParent()
        else:
            raise ValueError
    return e_tree


if __name__ == "__main__":
    exp = "((i && caesar) && ~julius)"
    tr = build_query_parse_tree(exp)
    inorder_traversal(tr)
    print(query_tree_evaluate(tr))
    '''
    output ->
    [0, 1]
    &&
    [0, 1]
    &&
    [0]
    ~

    [1]
    '''
