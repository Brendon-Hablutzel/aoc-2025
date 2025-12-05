from dataclasses import dataclass


@dataclass
class Interval:
    low: int
    high: int

    def merge(self, other: "Interval") -> "Interval | None":
        if self.low < other.low:
            lower = self
            higher = other
        else:
            lower = other
            higher = self

        if lower.high < other.low:
            # not overlapping
            return None

        return Interval(lower.low, max(lower.high, higher.high))


@dataclass
class Node:
    interval: Interval
    left: "Node | None"
    right: "Node | None"
    max_end: int


# (not balanced)
class IntervalTree:
    def __init__(self, intervals: list[Interval]):
        self.root: Node | None = None
        for interval in intervals:
            self.root = self.insert(interval, self.root)

    def insert(self, interval: Interval, current_root: Node | None) -> Node:
        if current_root is None:
            return Node(interval, None, None, interval.high)

        current_root.max_end = max(current_root.max_end, interval.high)

        if interval.low < current_root.interval.low:
            # insert into left subtree
            current_root.left = self.insert(interval, current_root.left)
        else:
            # insert into right subtree
            current_root.right = self.insert(interval, current_root.right)

        return current_root

    def _contains_point(self, node: "Node | None", point: int) -> bool:
        if node is None:
            return False

        if node.interval.low <= point <= node.interval.high:
            return True

        if node.left is not None and node.left.max_end >= point:
            if self._contains_point(node.left, point):
                return True

        if node.interval.low <= point:
            return self._contains_point(node.right, point)

        return False

    def contains_point(self, point: int) -> bool:
        return self._contains_point(self.root, point)
