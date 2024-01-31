class PacketCommit:
    def process_list(self, input_list):
        N = len(input_list)
        processed = set()
        output = []
        ptor = -1
        maxVal = 0
        for n in input_list:
            maxVal = max(maxVal, n)
            processed.add(n)
            largest_processed = ptor
            for i in range(ptor + 1, maxVal + 1):
                if i in processed:
                    largest_processed = i
                else:
                    break
            ptor = largest_processed
            output.append(ptor)
        return output

if __name__ == "__main__":
    sol = PacketCommit()

    print("test case 1")
    print(sol.process_list([0, 1, 2, 3]))
    print("test case 2")
    print(sol.process_list([3, 1, 2, 0]))
    print("test case 3")
    print(sol.process_list([2, 0, 1, 3]))
    print("test case 4")