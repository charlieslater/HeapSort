# HeapSort
I am in a very good discrete math class.  While discussing heaps, it was assumed that all heaps were max heaps.  Since the Python heapq module (https://docs.python.org/3.0/library/heapq.html) implements a min heap and an example at GeeksForGeeks (https://www.geeksforgeeks.org/binary-heap/) also uses a min heap, I challenged this assumption.

A max heap implements an in place ascending order sort of an array, I was told.  Well, a min heap implements an in place descending order sort.  And why is there some magic about pushing the top of the heap to the right (highest index) of the array?

Let's just try it.  Here I offer three heap programs:

maxHeapSort.py  This is copied out of Cormen, Lieserson, Rivest and Stein (CLRS) with minimal changes needed to implment it in Python.  The changes are trivial and you may think some of them silly.  For example, a dummy value at index 0 allows counting to start at 1 (as it does in CLRS).

minHeapSortDesc.py Simply reversed the comparisons in maxHeapSort.py, so it implements a min heap.

minHeapSortAsc.py  This puts the top of the heap on the left lowest index.  It does this in a very simple way by exploiting python list support for negative indices.  Any place a list index is used, a minus sign is added.  This results in an in-place sort in ascending order.

These programs illustrate that a max heap is not fundamentally better than a min heap.  Sometimes one is more appropriate than the other.  There is also a trick: use negative numbers (then convert to absolute value).  This converts a min heap into a max heap or vice versa.
