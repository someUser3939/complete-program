
def operation(operation_name, *args, **kwargs):
    def inner_function():
        if operation_name == "add":
            return sum(args)
        elif operation_name == "subtract":
            return args[0] - sum(args[1:])
        elif operation_name == "multiply":
            result = 1
            for num in args:
                result *= num
            return result
        elif operation_name == "divide":
            result = args[0]
            for num in args[1:]:
                result /= num
            return result
        else:
            raise ValueError(f"Unsupported operation: {operation_name}")
    return inner_function
    return operation


    
