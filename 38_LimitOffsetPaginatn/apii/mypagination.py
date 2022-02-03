from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit =  3 # agr client browser pe 10 bhi likhta h records show krne k liye, still 3 records hi show honge
