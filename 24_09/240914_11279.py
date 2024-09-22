import sys
def heap_pop(heap):
    print(heap[1])
    heap[1] = heap[len(heap)-1]
    v = heap.pop()
    l= len(heap)
    i = 1
    while 1:
        left = 2*i
        right = 2*i + 1
        if left > l-1:
            break
        elif left == l-1:
            if heap[left]>heap[i]:
                t = heap[left]
                heap[left] = heap[i]
                heap[i] = t
                i = left
            else:
                break
        else:
            if heap[left] > heap[right]:
                if heap[left]>heap[i]:
                    t = heap[left]
                    heap[left] = heap[i]
                    heap[i] = t
                    i = left
                else:
                    break
            else:
                if heap[right]>heap[i]:
                    t = heap[right]
                    heap[right] = heap[i]
                    heap[i] = t
                    i = right
                else:
                    break
    return

def heap_push(heap, x):
    heap.append(x)
    l = len(heap)
    i = l-1
    while 1:
        if i == 1:
            break
        parent = i//2
        if heap[parent] < heap[i]:
            t = heap[parent]
            heap[parent] = heap[i]
            heap[i] = t
            i = parent
        else:
            break
    return





heap = [0]


N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 1: print("0")
        else: heap_pop(heap)
    else:
        heap_push(heap,x)
