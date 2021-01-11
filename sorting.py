#This function takes list of tuples and sorts the list in reverse with first element of the first tuple as greatest and second
#elemet of the tuple as least.
def strange(l):
    l.sort(reverse=True, key=lambda x:(x[0],-x[1]))
    return