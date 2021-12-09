def timer(func):
    """
    函数运行时间计时器
    :param func: function
    :return: as same as function（param）'s return
    """
    from functools import wraps  # 对函数的装饰器

    @wraps(func)  # 使用@wraps时可以保证装饰器修饰的函数的name的值保持不变
    def decorator(*args, **kwargs):
        import time
        print('[{_func_name_}] --> start'.format(_func_name_=func.__name__))
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        interval = end_time - start_time
        if interval >= 1:
            # 耗时大于等于1s时 输出结果以秒为单位
            print('[{_func_name_}] --> {_duration_:.2f}s'
                  .format(_func_name_=func.__name__, _duration_=interval))
        else:
            # 耗时小于1s时 输出结果以毫秒为单位
            print('[{_func_name_}] --> {_duration_:.2f}ms'
                  .format(_func_name_=func.__name__, _duration_=(interval*1000)))
        return ret
    return decorator


if __name__ == '__main__':
    @timer
    def test():
        pass

    test()
