# assignment 4 question 2
# create a class book name with title,author and reviews of list  attributes
# add methods add_review,countreview and display all reviews
class book:
    def __init__(self,Title,Author):
        self.Title = Title
        self.Author = Author
        self.reviews_list = []

    def add_review(self,new_review):
        self.reviews_list.append(new_review)

    def count_review(self):
        print(f"count of review is :{len(self.reviews_list)}")

    def dispaly_review(self):
        print(f"all reviews is : {self.reviews_list}") 

book1 = book("python oops","guido van rossum")

book1.add_review("better understanding of oops")
book1.add_review("useer freindly")

book1.count_review()
book1.dispaly_review()