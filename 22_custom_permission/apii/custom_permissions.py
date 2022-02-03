from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':    # agr request method GET ata hai , us case me user ko allow krenge api access krne k lie.
            return True  # True mean access grant to access the api, jo bhi API is permission class ko use krega.
        return False

    
