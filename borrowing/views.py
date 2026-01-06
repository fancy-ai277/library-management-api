from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Borrow
from books.models import Book

class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        if book.available_copies > 0:
            Borrow.objects.create(user=request.user, book=book)
            book.available_copies -= 1
            book.save()
            return Response({"message": "Book borrowed"})
        return Response({"error": "No copies available"}, status=400)
