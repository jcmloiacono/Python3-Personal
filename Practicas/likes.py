def likes(names):
    other = len(names)
    if len(names) == 0:
        return "no one likes this"
    
    elif len(names) == 1:
        return ("{} likes this".format(names[0]))
    
    elif len(names) == 2:
        return ("{} and {} like this".format(names[0],names[1]))
    elif len(names) == 3:
        return ("{} {} and {} like this".format(names[0],names[1],names[2]))
    elif len(names) >= 4:
        return ("{}, {} and {} others like this".format(names[0],names[1], other-2))

likes(['Alex', 'Jacob', 'Mark', 'Max'])
likes(['Max', 'John', 'Mark'])
likes(['Jacob', 'Alex'])
likes(['Peter'])
likes([])

# OTRA OPCION

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)