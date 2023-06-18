if __name__ == '__main__':
    N = int(input())
    ans = []
    for i in range(N):
        command = input().split()
        if command[0] == 'print':
            print(ans)
        elif command[0] == 'sort':
            ans.sort()
        elif command[0] == 'reverse':
            ans.reverse()
        elif command[0] == 'pop':
            if len(ans) > 0:
                ans.pop()
        elif command[0] == 'remove':
            num_to_remove = int(command[1])
            ans.remove(num_to_remove)
        elif command[0] == 'append':
            num_to_append = int(command[1])
            ans.append(num_to_append)
        else:
            num_to_insert = int(command[1])
            pos_to_insert = int(command[2])
            ans.insert(num_to_insert, pos_to_insert)

        
            