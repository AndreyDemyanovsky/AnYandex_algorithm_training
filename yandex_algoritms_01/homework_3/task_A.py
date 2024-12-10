class MySet:
    count_elements = 0

    def __init__(self, sequence=None, size_set=1):
        self.size_set = size_set
        self._set_ = [[] for i in range(size_set)]
        if sequence:
            for i in sequence:
                self.add_new_element_in_set(i)

    def find_element_in_set(self, element, return_index=False):
        xlist = self._set_[element % self.size_set]
        for i, el in enumerate(xlist):
            if el == element:
                return (True, i) if return_index else True
        return (False, None) if return_index else False

    def add_new_element_in_set(self, element):
        if not self.find_element_in_set(element):
            self._set_[element % self.size_set].append(element)
            self.__count_elements__ += 1

        if len(self._set_[element % self.size_set]) > self.size_set:
            self.recreate()

    def del_element_from_set(self, element):
        in_set, element_index = self.find_element_in_set(element, True)
        if in_set:
            xlist = self._set_[element % self.size_set]
            xlist[element_index] = xlist[-1]
            xlist.pop()
            self.__count_elements__ -= 1

    def recreate(self):
        self.size_set *= 2
        new_set = [[] for _ in range(self.size_set)]

        for i_list in self._set_:
            for element in i_list:
                index_list = element % self.size_set
                if element not in new_set[index_list]:
                    new_set[index_list].append(element)

        self._set_ = new_set



set_numbers = MySet(map(int, input().split()))
print(set_numbers.count_elements)
