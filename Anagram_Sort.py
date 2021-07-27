def anagram(lst):
    ana = []
    tot = []

    dict_sort = {'word':[],'lst_sort':[]}

    for i in lst:
        val = sorted(i)
        val = "".join(val) 
        dict_sort['word'].append(i)
        dict_sort['lst_sort'].append(val)

    words = list(dict_sort.values())[0]
    lst_sorts = list(dict_sort.values())[1]
    set_sorts = list(set(lst_sorts))

    for k in set_sorts:
        ana = []
        for j in range(len(lst_sorts)):
            v1 = lst_sorts[j]
            if v1==k:
                ana.append(words[j])
        tot.append(ana)

    print(tot)
            
if __name__=='__main__':
    lst = ['tea','ate','bat','tab','nab','eat']
    output = [['nab'],['bat','tab'],['tea','eat','ate']] 
    anagram(lst)