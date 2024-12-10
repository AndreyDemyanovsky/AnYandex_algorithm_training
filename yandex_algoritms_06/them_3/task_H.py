class StackWithSum:

    def __init__(self):
        self.__data = []
        self.__prefix_sum = [0]

    def __add__(self, other):
        self.__data.append(other)
        self.__prefix_sum.append(self.__prefix_sum[-1] + other)

    def substract(self):
        self.__prefix_sum.pop()
        return self.__data.pop()

    def get_sum_last_k_lements(self, k):
        return self.__prefix_sum[len(self)] - self.__prefix_sum[len(self) - k]
    
    def __len__(self):
        return len(self.__data)


number_operation = int(input())
stack_with_sum = StackWithSum()

for _ in range(number_operation):
    request = input()
    operation, number = request[0], request[1:] 
    match operation: 
        case "+":
            stack_with_sum + int(number)
        case "-":
            print(stack_with_sum.substract())
        case "?":
            print(stack_with_sum.get_sum_last_k_lements(int(number)))
        
        




