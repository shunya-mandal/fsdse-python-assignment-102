
def is_rotation(s1, s2):
    if s1 is None or s2 is None:
        return False

    if len(s1) != len(s2):
        return False

    if len(s1) == len(s2) == 0:
        return True

    for i in range(len(s1)):
        rotated = s2[i+1:] + s2[:i+1]
        if rotated == s1:
            return True
    return False

s1 = 'rotation'
s2 = 'tationro'

print(is_rotation('',''))
