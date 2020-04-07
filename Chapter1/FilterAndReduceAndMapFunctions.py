class SampleClass:
    def __init__(self,id,y):
        self.id=id;
        self.y=y;
    def __repr__(self):
        return f"{self.id},{self.y}";



if __name__ == '__main__':
    input =list(range(0,10))
    print(input)
    #convert list into multiple by 2
    newList =list(map(lambda x: x*2,input));
    print(newList)
    # Filter only less than 8
    filterList =list(filter(lambda x: x<8,newList))
    print(filterList)

    object_list =[ SampleClass(1,2),SampleClass(1,3),SampleClass(2,4)]
    object_dict = dict((x.id, x) for x in object_list)
    print(object_dict)


    object_list1 =[ SampleClass(1,2),SampleClass(1,3),SampleClass(2,4)]

    object_dict1 = dict(map(lambda x : [x.id,x] ,object_list1))
    print(object_dict1)
    # Below print statement explain about how we can do manipulation of list using generator pattern. we can define the function to process if you want to process list , We can add finter ,map etc to list
    print(([(x.id,x) for x in object_list1]))
