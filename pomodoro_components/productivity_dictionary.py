
import pickle

PRODUCTIVITY_DIC = "productivity-dic"
# d = { "abc" : [1, 2, 3], "qwerty" : [4,5,6] }
# afile = open(r'productivity_dic', 'wb')
# pickle.dump(d, afile)
# afile.close()

# #reload object from file
# file2 = open(r'C:\d.pkl', 'rb')
# new_d = pickle.load(file2)
# file2.close()

# print(new_d)

class ProductivityDictionary:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d = set({}) 
        try: 
            fp = open(PRODUCTIVITY_DIC)
        except IOError:
            fp = open(PRODUCTIVITY_DIC,'w+')

            self.saveDictionary({"all-time": set({}) })


    def grabDictionary(self):
        file2 = open(r''+PRODUCTIVITY_DIC, 'rb')
        dic = pickle.load(file2)
        file2.close()
        return {} if dic is  None else dic

    def saveDictionary(self, dic):
        afile = open(r''+PRODUCTIVITY_DIC, 'wb')
        pickle.dump(dic, afile)
        afile.close()

    def addDate(self, date):
        dic = self.grabDictionary()
        dic[date] = set({}) 
        self.saveDictionary(dic)

    def addTask(self, date, task):
        dic = self.grabDictionary()

        if date not in dic:
            dic[date] = set({})
            
        dic[date].add(task)
        self.saveDictionary(dic)

 
if __name__ == "__main__":
    A = ProductivityDictionary()

    A.addDate("all-time")

    print(A.grabDictionary())

    A.addTask("all-time", "love")

    print(A.grabDictionary())

    # goal: Determine if addTask should initialize a new
    A.addDate('09/11/2019')
    print(A.grabDictionary())
