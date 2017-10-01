def hexToDec(inNum):
    '''Convert Hex Color To Dec Num'''
    import re
    if not isinstance(inNum, str):
        raise Exception('Unsupported data type')

    if re.match(r'0x', inNum):
        found = re.findall(r'0x([0-9a-eA-E]{6})', inNum)[0]
    else: found = re.findall(r'#([0-9a-eA-E]{6})', inNum)[0]
    #print(found)
    if len(found) != 6: raise Exception('Not A Formal RGB Hex')
    red = int(found[0: 2], 16)
    green = int(found[2: 4], 16)
    blue = int(found[4: 6], 16)
    return [red, green, blue]
