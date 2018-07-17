class Heap:
   def __init__(self, A, heapSize):
     self.heapSize = heapSize
     self.A = [99999] + A
     self.largest = 1
   def Left(self, i):
     return i-i/2-1
   def Right(self, i):
     return i-i/2
   def exchange(self, i, j):
     tmp = self.A[i]
     self.A[i] = self.A[j]
     self.A[j] = tmp
   def MaxHeapify(self, i):
     l = self.Left(i)
     r = self.Right(i)
     if l <= self.heapSize and self.A[l] > self.A[i]:
       self.largest = l
     else:
       self.largest = i
     if r <= self.heapSize and self.A[r] > self.A[self.largest]:
       self.largest = r
     if self.largest != i:
       self.exchange(i,self.largest)
       self.MaxHeapify(self.largest)
   def BuildMaxHeap(self,A):
     self.A = [99999] + A
     self.heapSize = len(A)
     for i in range(len(self.A)/2,0,-1):
       self.MaxHeapify(i)
   def Heapsort(self,A):
     self.BuildMaxHeap(A)
     print self.A[1:]
     for i in range(len(A),1,-1):
       self.exchange(1,i)
       self.heapSize = self.heapSize - 1
       self.MaxHeapify(1)
       print self.A[1:]
a = [4,1,3,2,16,9,10,14,8,7]
print 'input =',a
h = Heap(a,len(a))
h.Heapsort(a)
print 'result =',h.A[1:]
