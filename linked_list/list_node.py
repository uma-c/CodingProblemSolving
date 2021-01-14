class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def iter(self):
        curr = self
        while curr:
            val = curr.val
            curr = curr.next
            yield val

    def __str__(self):
        vals = []
        for val in self.iter():
            vals.append(str(val))
        return ' -> '.join(vals)