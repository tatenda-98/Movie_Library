class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.item = item
        self.previous = prevnode
        self.next = nextnode

class Pyflix:
    # init function to create the doubly linked list,
    # and add the first and last dummy links
    def __init__(self):
        self.first = DLLNode(None, None, None)
        self.last = DLLNode(None, self.first, None)
        self.first.next = self.last
        self.cursor = self.first
        self.size = 0

    def __str__(self):
        # overriding the string function to show what current movie the
        # cursor is pointing to along with the movie title and director
        current = self.first.next
        movies_str = ""
        while current != self.last:
            if current == self.cursor:
                str = "--> %s, %s \n" % (current.item.title, current.item.director)
            else:
                str = "%s, %s \n" % (current.item.title, current.item.director)
            movies_str += str
            current = current.next
        return movies_str

    def add_movie(self, m):
        # function that adds movies to the Doubly linked list
        # create a new item using the DLL class
        new_node = DLLNode(m, self.last.previous, self.last) #added to the end of the list so the end is always going to be the tail node
        new_node.previous.next = new_node # making the new node the next node of the previous node
        self.last.previous = new_node
        self.size += 1 # increasing the list size by 1

    def get_current(self):
        # returns the current item in the list
        return self.cursor.item

    def next_movie(self):
        # moves the cursor to the next item in the list
        if self.cursor.next == self.last and self.size > 0:
            self.cursor = self.first.next
        elif self.size > 0:
            self.cursor = self.cursor.next
        #if  next node is the tail go to the next node
        # if it isnt the tail get the next node

    def prev_movie(self):
        # moves the cursor to the previous item in the list
        if self.cursor == self.first and self.size>0:
            self.cursor = self.last.previous
        elif self.size > 0:
            self.cursor = self.cursor.previous

    def reset(self):
        # resets the cursor to the front of the list
        self.cursor = self.first

    def rate(self):
        # asks the user to input a rating for the current movie in the list
        rating = int(input("Enter your rating here>> "))
        if rating >= 0:
            self.cursor.item.movie_rating = rating
        else:
            return "Invalid input. Please enter a whole number"

    def info(self):
        # calls the get_info() func in the movie class and returns
        # the contents of the output
        return self.cursor.item.get_info()

    def remove_current(self):
        # removes the movie the cursor is currently pointing to
        before = self.cursor.previous
        after = self.cursor.next
        before.next = after
        after.previous = before
        # repoints the nodes on both sides of the deleted node to
        # point at each other
        # decreases the size of the list
        self.size -= 1


    def length(self):
        # returns the size of the list
        return self.size

    def search(self, word):                                                                                 #function to search through the list and return the info of that movie
        current = self.get_current()                                                                        #sets the current position into a variable naemd current
        while self.cursor.next != current:                                                                  #while the next position is not the postion that was started with
            if self.cursor.next == self.last:                                                               #if the next poisiton is not the tail node then reset the cursor in the list to the first item
                self.reset()
                self.next_movie()
            if word in (self.cursor.item.title or self.cursor.item.director or self.cursor.item.cast):      #if the word is the movie/director/cast return the info
                return self.info()
            else:
                self.next_movie()                                                                           #move to the next position in the list
                return "No matching movie."                                                                 #return no matching movie



class Movies:

    def __init__(self, title, director, cast, length, rating= -1):
        self.title = title
        self.director = director
        self.cast = cast
        self.length = length
        self.movie_rating = rating

    def __str__(self):
        return "%s, %s" % (self.title, self.director)

    def get_info(self):
        return "(Title = {}, Director = {}, Cast = {}, Length = {}, Rating = {})"\
            .format(self.title, self.director, self.cast, self.length, self.movie_rating)





m1 = Movies('EL Camino', "Vince Gilligan", "Aaron Paul", 122)
m2 = Movies("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
m3 = Movies("Midsommer", "An Aster", "Florence Pugh", 138)
m4 = Movies("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)

list = Pyflix()

list.add_movie(m1)
list.add_movie(m2)
list.add_movie(m3)

print("v:", list)
list.next_movie()
print()
print("vii:", list.get_current())
list.next_movie()
print()
print("ix:", list.get_current())
list.rate()
list.prev_movie()
#list.remove_current()
print("xiii:\n", list)
print('xiv:', list.get_current())
list.add_movie(m4)
list.next_movie()
list.next_movie()
print("xviii:", list.get_current())
print("xix: \n", list)

print(list.search('Midsommer'))
