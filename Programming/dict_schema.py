class GetDictParam:
    """
    这是一个解析dict 参数的类
    可以用于多参数的指定key 、 指定key集合解析key
    """
    # @classmethod
    def get_value(cls, my_dict, value):
        """ 这是一个递归函数 """
        if isinstance(my_dict, dict):
            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if cls.get_value(my_dict.get(my_dict_key), key) or \
                        cls.get_value(my_dict.get(my_dict_key), key) is False:
                    return cls.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if cls.get_value(my_dict_arr, key) \
                        or cls.get_value(my_dict_arr, key) is False:
                    return cls.get_value(my_dict_arr, key)
    class GetDictParam:
        """
        这是一个解析dict 参数的类
        可以用于多参数的指定key 、 指定key集合解析key
        """
        @classmethod
        def get_value(cls, my_dict, key):
            """ 这是一个递归函数 """
            if isinstance(my_dict, dict):
                if my_dict.get(key):
                    return my_dict.get(key)

                for my_dict_key in my_dict:
                    if cls.get_value(my_dict.get(my_dict_key), key):
                        return cls.get_value(my_dict.get(my_dict_key), key)

            if isinstance(my_dict, list):
                for my_dict_arr in my_dict:
                    if cls.get_value(my_dict_arr, key):
                        return cls.get_value(my_dict_arr, key)
    @classmethod
    def get_value(cls, my_dict, value):
        """ 这是一个递归函数 """
        if isinstance(my_dict, dict):
            if value in my_dict.values():
                return value

            for my_dict_key in my_dict:
                if cls.get_value(my_dict.get(my_dict_key), value):
                    return cls.get_value(my_dict.get(my_dict_key), value)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if cls.get_value(my_dict_arr, value):
                    return cls.get_value(my_dict_arr, value)

    @classmethod
    def list_for_key_to_dict(cls, *args, my_dict):
        """
            接收需要解析的dict和 需要包含需要解析my_dict的keys的list

        :param my_dict: 需要解析的字典
        :param args: 包含需要解析的key的多个字符串
            # list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=dict)
        :return: 一个解析后重新拼装的dict
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: cls.get_value(my_dict, key)})
        return result


def dict_get(self,data, value):
    dict_data = data
    for data_key, data_value in dict_data.items():
        if data_value == value:
            # print(data_key, data_value)
            return data_value
        else:
            if isinstance(data_value, dict):
                ret = dict_get(data_value, value)
                return ret
            elif isinstance(data_value, list):
                for i in data_value:
                    ret = dict_get(i, value)
                    return ret
