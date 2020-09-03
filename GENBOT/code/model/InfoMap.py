class InfoMap():

    def __init__(self, filter_field, coorX_field, coorY_field, extra_info_fields):
        self.filter_field = filter_field
        self.coorX_field = coorX_field
        self.coorY_field = coorY_field
        self.extra_info_fields = extra_info_fields

    @property
    def filter_field(self):
        return self.__filter_field

    @property
    def coorX_field(self):
        return self.__coorX_field

    @property
    def coorY_field(self):
        return self.__coorY_field

    @property
    def extra_info_fields(self):
        return self.__extra_info_fields

    @filter_field.setter
    def filter_field(self, filter_field):
        self.__filter_field = filter_field

    @coorX_field.setter
    def coorX_field(self, coorX_field):
        self.__coorX_field = coorX_field

    @coorY_field.setter
    def coorY_field(self, coorY_field):
        self.__coorY_field = coorY_field

    @extra_info_fields.setter
    def extra_info_fields(self, extra_info_fields):
        self.__extra_info_fields = extra_info_fields
