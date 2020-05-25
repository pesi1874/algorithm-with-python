import random


class MaxHeap:

    def __init__(self):
        self._data = []
        self._count = len(self._data)

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def add(self, item):
        self._data.append(item)
        self._count += 1
        self._shifUp(self._count - 1)

    def pop(self):
        if self._count > 0:
            ret = self._data[0]
            self._data[0] = self._data[self._count - 1]
            self._count -= 1
            self._shifDown(0)
            return ret

    def _shifUp(self, index):
        parent = (index - 1) >> 1
        while index > 0 and self._data[index] < self._data[index]:
            self._data[parent], self._data[index] = self._data[index], self._data[parent]
            index = parent
            parent = (index - 1) >> 1

    def _shifDown(self, index):
        j = (index << 1) + 1
        while j < self._count:
            if j + 1 < self._count and self._data[j+1] > self._data[j]:
                j += 1
            if self._data[index] >= self._data[j]:
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j
            j = (index << 1) + 1

def testIntValue():
    for i in range(10):
        iLen = random.randint(1, 300)
        # allData = random.sample(range(iLen *100), iLen)
        allData = [10, 5, 6, 2, 10, 1, 8]
        print('\nlen = ', iLen)

        oMaxHeap = MaxHeap()
        print('_data:\t', allData)
        arrDataSorted = sorted(allData, reverse=True)
        print('dataSorted:', arrDataSorted)
        for i in allData:
            oMaxHeap.add(i)
        heapData = []
        for i in range(iLen):
            iExpected = arrDataSorted[i]
            iActual = oMaxHeap.pop()
            heapData.append(iActual)
            print('{}, expected:{}, actual:{}'.format(iExpected==iActual, iExpected, iActual))
            assert iExpected == iActual
        print('dataSorted: ', arrDataSorted)
        print('heapData: ', heapData)



if __name__ == '__main__':
    testIntValue()
    # m = MaxHeap()
    # m.add(1)





















