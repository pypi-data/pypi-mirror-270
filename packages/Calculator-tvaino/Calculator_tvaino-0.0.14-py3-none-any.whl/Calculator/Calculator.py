class Calculator:

    def __init__(self):

        '''
        Calculator memory set to zero
        
        '''

        self.mem = 0
      
    def add(self, number:int)->int:

        '''
        Add function adds provided argument value to a memory value
        and stores the result it into the memory.
        
        '''

        if not isinstance(number, (int)):
            raise TypeError('Argument must be type of intiger')
        
        self.mem += number
        
        return self.mem


    def subtract(self, number:int)-> int:

        '''
        Subtract function subtracts provided argument value from a memory value
        and stores the result it into the memory.
        
        '''

        if not isinstance(number, (int)):
            raise TypeError('Argument must be type of intiger')
        
        self.mem -= number
        
        return self.mem

    # @check_type
    def multiply(self, number:int)->int:
        
        '''
        Multiply function multiplies a memory value by the value of the provided argument
        and stores the result it into the memory.
        
        '''

        if not isinstance(number, (int, float)):
            raise TypeError('Argument must be an integer')         
        
        self.mem *= number
        
        return self.mem

    # @check_type
    def divide(self, number:int)->float:

        '''
        Divide function divides a memory value by the value of the provided argument
        and stores it into the memory.

        '''

        if not isinstance(number, (int, float)):
            raise TypeError('Argument must be an integer')
        if number != 0:
            self.mem /= number
            return self.mem
        else:
            raise ValueError('Division by zero is not supported')
        
            
    # @check_type
    def root(self, number:int)->float:

        """
        Root function computes the root of power (provided argument value) of actual memory
        and stores it into the memory.

        """

        if not isinstance(number, (int, float)):
            raise TypeError('Argument must be an integer')
        
        if self.mem <= 0:
            raise ValueError("Calculator does not support roots from negative or zero values")  
        if number == 0:
            raise ValueError('Cannot compute zero root')
        else:
            self.mem = self.mem ** (1 / number)
            
        return self.mem
        

    def reset(self)-> None:

        '''
        Reset function resets memory value to zero.
        
        '''
        
        self.mem = 0
        return self.mem
