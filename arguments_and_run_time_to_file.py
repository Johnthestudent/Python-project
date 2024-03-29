import time

def log(fn):
    """
    Code writes function arguments and run time into a log txt file  
    """

    def log_wrapper(*args, **kwargs):
        # getting arguments
        params = fn.__code__.co_varnames[:fn.__code__.co_argcount]
        params_list = list(params)
        args_list = list(args)
        #   separate keyword arguments
        for key in kwargs.keys():
            if key in params_list:
                params_list.remove(key)
        #   merge positional keys and args
        args_dict = {}
        for key in params_list:
            for arg in args_list:
                args_dict[key] = arg
                args_list.remove(arg)
        print(args_dict)
        print(kwargs)

        # start timer
        st = time.time()

        # Execute function
        result = fn(*args, **kwargs)

        # get execution_time
        run_time = time.time() - st

        # Log function 'fn' name and arguments
        with open("log.txt", "w", encoding="utf-8") as log_file:
            log_file.write(f"{fn.__name__};")
            args_field = ""
            for key, val in args_dict.items():
                args_field += f"{key}={val},"
            args_field = args_field[:-1]
            args_field += ";"
            log_file.write(args_field)
            kwargs_field = ""
            for key, val in kwargs.items():
                kwargs_field += f"{key}={val},"
            kwargs_field = kwargs_field[:-1]
            kwargs_field += ";"
            log_file.write(kwargs_field)
            log_file.write(f"execution time: {run_time} sec.")

    return log_wrapper


@log
def foo(a, b, c):
    return 0


if __name__ == "__main__":
    foo(1, 2, c=3)
