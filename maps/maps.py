from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        filtered_movies = filter(
            lambda m: MapExercise.get_movie_rating_kinopoisk(m) > 0
            and len(MapExercise.get_movie_countries(m)) >= 2,
            list_of_movies,
        )
        rating_movies = list(map(MapExercise.get_movie_rating_kinopoisk, filtered_movies))
        return sum(rating_movies) / len(rating_movies)

    @staticmethod
    def get_movie_countries(movie: dict) -> list[str]:
        countries_str = movie.get("country", "")

        countries = countries_str.split(",")
        countries = map(str.strip, countries)

        return list(countries)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        filtered_movies = filter(
            lambda m: MapExercise.get_movie_rating_kinopoisk(m) > rating, list_of_movies
        )
        sum_movies = map(lambda m: m["name"].count("и"), filtered_movies)
        return sum(sum_movies)

    @staticmethod
    def get_movie_rating_kinopoisk(movie: dict) -> Union[float, int]:
        rating_str = movie.get("rating_kinopoisk", "")
        if rating_str in ["", "0"]:
            return 0
        return float(rating_str)
