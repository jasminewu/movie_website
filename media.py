class Movie(object):
    """ this Movie class is created to store movie data,
        input movie_title, poster_image, play_url and
        output a movie instance
    Args:
        param1(str): movie_title,the first param
        param2(str): poster_image,the second param
        param3(str): paly_url,the third param

    """
    def __init__(self, movie_title, poster_image, paly_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = paly_url
