
k = 0
sensAttribute = 0
qilist = []


class Partition():

    def __init__(self, kn: int, sensitive: int, qil: list):

        self.sensAttribute = sensitive
        self.k = kn
        self.qilist = qil

    def choose_dimension(self):
        dim = int(-1)

        for i in range(0, len(self.qilist)):

            if self.qilist[i] != self.sensAttribute:
                dim = self.qilist[i]
                self.qilist.pop(i)
                break

        return dim

    def frequency_set(self, data: list, dim: int):

        items = []

        if dim != -1:

            for i in data:
                c = False
                for j in items:
                    if j.__contains__(i[dim]):
                        c = True
                if c == False:
                    items.append([i[dim], 0])

                for j, x in enumerate(items):
                    if i[dim] in x:
                        items[j][1] += 1

        return items

    def findMedian(self, fs: list):
        splitValue = 0

        if len(fs) % 2 == 1:
            splitValue = int((len(fs)+1)/2)
        else:
            splitValue = int(len(fs)/2)
        splitValue = fs[splitValue][0]
        return splitValue

    def combine(self, lhs: list, rhs: list):
        combinedList = []

        for i in lhs:
            combinedList.append(i)
        for i in rhs:
            combinedList.append(i)
        return combinedList

    def allowableCut(self, fs: list):

        allow = False
        if fs != []:

            if fs[0][1] >= k:
                allow = True
        return allow

    def findMax(self, datalist: list):
        max = [0]*(len(datalist[0])-1)

        for i in datalist:
            for j in range(0, len(i)-1):

                if int(i[j]) > max[j]:
                    max[j] = int(i[j])
        return max

    def findMin(self, datalist: list):
        min = [10000]*(len(datalist[0])-1)
        for i in datalist:
            for j in range(0, len(i)-1):
                if int(i[j]) < min[j]:
                    min[j] = int(i[j])
        return min

    def generalize(self, datalist: list, max: list, min: list):
        generalized = [""]*len(max)

        for i in range(0, len(max)):
            if i != self.sensAttribute:
                if min[i] != max[i] and (int(max[i])-int(min[i])) > self.k:
                    generalized[i] = "["+str(min[i])+","+str(max[i])+"]"
                else:
                    generalized[i] = str(min[i])

        for i in range(0, len(datalist)):
            for j in range(0, len(generalized)):
                datalist[i][j] = generalized[j]
        return datalist

    def anonymize(self, datalist: list):

        dim = self.choose_dimension()
        datalist = sorted(datalist, key=lambda l: l[dim])

        fs = self.frequency_set(datalist, dim)

        if self.allowableCut(fs) == False:
            max = self.findMax(datalist)
            min = self.findMin(datalist)
            datalist = self.generalize(datalist, max, min)

            return datalist

        anonmizedList = []
        if fs != []:
            splitValue = self.findMedian(fs)

            for i in range(0, len(datalist)):
                if str(splitValue) in datalist[i][dim]:
                    splitValue = i

            lhs = list(self.anonymize(datalist[0:splitValue]))
            rhs = list(self.anonymize(datalist[splitValue:]))
            anonmizedList = self.combine(lhs, rhs)
            return anonmizedList
