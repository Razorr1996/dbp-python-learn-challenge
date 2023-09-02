class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        replace_list = input_list[:]

        if len(replace_list) == 0:
            return replace_list

        max_element = max(replace_list)

        for index, element in enumerate(replace_list):
            if element > 0:
                replace_list[index] = max_element

        return replace_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        _NOT_FOUND = -1
        _ZERO_INDEX = 0

        if len(input_list) == 0:
            return _NOT_FOUND

        if len(input_list) == 1:
            if input_list[_ZERO_INDEX] == query:
                return _ZERO_INDEX
            else:
                return _NOT_FOUND

        assert sorted(input_list) == input_list

        half_length = len(input_list) // 2

        if query < input_list[half_length]:
            additional_index = _ZERO_INDEX
            list_for_search = input_list[:half_length]
        else:
            additional_index = half_length
            list_for_search = input_list[half_length:]

        internal_result = ListExercise.search(list_for_search, query)

        if internal_result == _NOT_FOUND:
            return _NOT_FOUND
        else:
            return internal_result + additional_index
