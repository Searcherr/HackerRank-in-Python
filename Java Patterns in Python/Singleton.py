class Singleton_class:
    __instance = None
    
    def __new__(cls, inputString,*args, **kwargs):
        cls.inputString = inputString
        if cls.__instance is None:
            cls.__instance = super(Singleton_class, cls).__new__(cls)
        return cls.__instance

if __name__ == "__main__":

    #Testing
    #userInputString = str(input('Enter the string: '))
    firstObjectPointer = Singleton_class('Velue_1')
    secondObjectPointer = Singleton_class('Value_2')
    thirdObjectPointer = Singleton_class('Velue_3')

    print(f' ID of the 1st object pointer: {firstObjectPointer}', '\n',
          f'ID of the 2nd object pointer: {firstObjectPointer}', '\n',
          f'ID of the 3rd object pointer: {firstObjectPointer}', '\n')

    variablesPointToTheSameObject = str(firstObjectPointer == secondObjectPointer == thirdObjectPointer)
    print('Statement that variables point to the same object is ' +
          '\x1B[4m' + variablesPointToTheSameObject + '\x1B[0m')

    if id(firstObjectPointer) == id(secondObjectPointer) == id(thirdObjectPointer):
        print("We have the same object, so Singleton works")
    else:
        print("Unfortunately there were created different objects, so Singleton doesn't work")
    
    
    print('Result: ' + firstObjectPointer.inputString)
    print('Result: ' + secondObjectPointer.inputString)
    print('Result: ' + thirdObjectPointer.inputString)