import rank
import csv

class Queue:
    def __init__(self, items: list = None):
        self.items = items or list()

    def enqueue(self, item: int):
        self.items.append(item)

    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return self.items.__str__()


# Returns True if viewer prefers ad i over the one they currently have.
# Returns false otherwise.
def viewer_prefers_i_over_current(viewer_ranking: Queue, i: int):
    found = False
    other_queue = Queue()
    while not viewer_ranking.is_empty():
        item = viewer_ranking.dequeue()
        if item == i:
            found = True
        other_queue.enqueue(item)
    # put all removed items back into queue
    while not other_queue.is_empty():
        viewer_ranking.enqueue(other_queue.dequeue())
    return found


# removes all items in viewer_preferences queue before ad_name (including ad_name)
def viewer_moved_up(viewer_preferences, ad_name):
    item = viewer_preferences.dequeue()
    while item != ad_name:
        item = viewer_preferences.dequeue()


# ads are named 0 to N-1
# viewers are named N to 2N-1
def find_matches(viewer_preferences, ad_preferences):
    N = len(ad_preferences)
    current_matches = [-1] * N  # index is viewer, element is ad
    available_ads = [True] * N
    while any(available_ads):
        print(current_matches)
        ad_index = available_ads.index(True)
        while available_ads[ad_index]:
            viewers_prefered_by_this_ad = ad_preferences[ad_index]
            top_choice_viewer_index = viewers_prefered_by_this_ad.dequeue() - N
            if current_matches[top_choice_viewer_index] == -1:  # viewer is free
                current_matches[top_choice_viewer_index] = ad_index  # match viewer with this ad
                available_ads[ad_index] = False  # this ad is now taken
                viewer_moved_up(viewer_preferences[top_choice_viewer_index], ad_index)
            else:  # viewer is not free
                if viewer_prefers_i_over_current(viewer_preferences[top_choice_viewer_index], ad_index):
                    available_ads[
                        current_matches[top_choice_viewer_index]] = True  # prev ad is now available
                    available_ads[ad_index] = False  # this ad is now taken
                    current_matches[top_choice_viewer_index] = ad_index  # match viewer with this ad
    for ind, elm in enumerate(current_matches):
        print(f"viewer {ind} is matched with ad {elm}")

def dataReader(filename: str):
    file = open(filename, "r")
    reader = csv.reader(file)
    data = list(reader)
    file.close()
    return data

def dataTransfer(data):
    queueList = []
    for line in data:
        queueList.append(reverse(Queue(line)))
    return queueList

def main():
    # read in data
    viewerData = dataReader("viewer_attributes.csv")
    adsData = dataReader("ads_attributes.csv")
    # rank the data
    viewer_preferences = dataTransfer(rank.rankads(viewerData, adsData))
    ad_preferences = dataTransfer(rank.rankViewer(viewerData, adsData))
    # transfer the list within list into queue

    # find matches
    find_matches(viewer_preferences, ad_preferences)

def reverse(q: Queue):
    s = Stack()
    while not q.is_empty():
        s.push(q.dequeue())
    while not s.is_empty():
        q.enqueue(s.pop())
    return q


class Stack:
    def __init__(self, items: list = None):
        self.items = items or list()

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        item = self.items[-1]
        self.items = self.items[:-1]
        return item

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    main()

