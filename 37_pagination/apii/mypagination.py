from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3  # ek page m kitne record dkhne h
    page_query_param = 'p' # page k jgh p use krenge search krne k lie.
    page_size_query_param = 'records' # by using  page_size_query_param client can  request how many records he want per page.
    max_page_size = 5
    last_page_strings = 'end'
