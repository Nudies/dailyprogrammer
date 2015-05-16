#Challenge201_2[practical]
#http://www.reddit.com/r/dailyprogrammer/comments/2vkwgb/20150211_challenge_201_practical_exercise_get/
#A priority queue is a data structure similar to a standard queue, except that entries in the
#queue have a priority associated with them - such that, when removing items from the queue,
#the entry with the highest priority will be removed before ones with lower priority.
#
#Your priority queue must implement at least these methods:
#Enqueue. This method accepts three parameters - a string, priority value A, and priority value B, where the priority
#values are real numbers (see above). The string is inserted into the priority queue with the given priority values A
#and B (how you store the queue in memory is up to you!)
#DequeueA. This method removes and returns the string from the priority queue with the highest priority A value. If two
#entries have the same A priority, return whichever was enqueued first.
#DequeueB. This method removes and returns the string from the priority queue with the highest priority B value. If two
#entries have the same B priority, return whichever was enqueued first.
#Count. This method returns the number of strings in the queue.
#Clear. This removes all entries from the priority queue.
#Additional
#If you can, implement this method, too:
#DequeueFirst. This removes and returns the string from the priority queue that was enqueued first, ignoring priority.
#Depending on how you implemented your priority queue, this may not be feasible, so don't get too hung up on this one.

class DblPriorityQueue:
        '''
        A two-priority priority queue for strings,
        where the priority is represented by a real number.
        '''
        cPickle = __import__('cPickle')

        def __init__(self):
                self.queue = {}
                self.id = 0


        def enqueue(self, addQueue, priorityA, priorityB):
            '''
            Add to self.queue to represent an object in queue with
            two priorities.
            '''
            self.queue[addQueue] = {'A': priorityA, 'B': priorityB, 'ID':
                    self.id}
            self.id += 1
            return

        def dequeueA(self):
            '''
            This method removes and returns the string from the
            priority queue with the highest priority A value. If two
            entries have the same A priority, return whichever was
            enqueued first.
            '''
            highest = 0
            id = None
            item = None
            for k in self.queue.keys():
                if self.queue[k]['A'] > highest:
                    highest = self.queue[k]['A']
                    id = self.queue[k]['ID']
                    item = k
                elif self.queue[k]['A'] == highest:
                    if self.queue[k]['ID'] < id:
                        highest = self.queue[k]['A']
                        id = self.queue[k]['ID']
                        item = k
            self.queue.pop(item)
            return item

        def dequeueB(self):
            '''
            Removes and returns the string from the priority queue
            with the highest priority B value. If two entries have
            the same B priority, return whichever was enqueued first.
            '''
            highest = 0
            id = None
            item = None
            for k in self.queue.keys():
                if self.queue[k]['B'] > highest:
                    highest = self.queue[k]['B']
                    item = k
                elif self.queue[k]['B'] == highest:
                    if self.queue[k]['ID'] < id:
                        highest = self.queue[k]['B']
                        id = self.queue[k]['ID']
                        item = k
            self.queue.pop(item)
            return item


        def dequeueFirst(self):
            '''
            This removes and returns the string from the priority
            queue that was enqueued first, ignoring priority.
            '''
            id = None
            item = None

            for k in self.queue.keys():
                if self.queue[k]['ID'] < id or id == None:
                    id = self.queue[k]['ID']
                    item = k
            self.queue.pop(item)
            return item


        def prettyPrint(self):
            '''
            Print in a nice format.
            '''
            for k, v in self.queue.items():
                print '%s: %s' % (k, v)
            return


        def count(self):
            '''
            Returns the number of strings in the queue.
            '''
            return len(self.queue)


        def clear(self):
            '''
            This removes all entries from the priority queue.
            '''
            self.queue = {}
            return


        def flush(self, file='data.pkl'):
            '''
            Open a file and dump data to it using cPickle.
            '''
            f = open(file, 'wb')
            self.cPickle.dump(self.queue, f)
            f.close()
            print 'Saved as %s' % file
            return


        def load(self, file='data.pkl'):
            '''
            Open a file and load data into queue using cPickle.
            '''
            try:
                f = open(file, 'rb')
                data = self.cPickle.load(f)
                if type(data) != dict:
                    self.queue = {}
                    print 'Incorrect data format, failed to load.'
                else:
                    self.queue = data
                f.close()
            except IOError as e:
                print e
            return
