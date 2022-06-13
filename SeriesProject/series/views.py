from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Series, Review, Suggestions
from .serializers import SeriesSerializer, ReviewSerializer, SuggestionsSerializer


# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_series(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_series = SeriesSerializer(data=request.data)
    if new_series.is_valid():
        new_series.save()
        data = {
            "msg": "Added Successfully",
            "series": new_series.data
        }
        return Response(data)
    else:
        print(new_series.errors)
        data = {"msg": "couldn't Add a series"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_review(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_review = ReviewSerializer(data=request.data)
    if new_review.is_valid():
        new_review.save()
        data = {
            "msg": "Added Successfully",
            "review": new_review.data
        }
        return Response(data)
    else:
        print(new_review.errors)
        data = {"msg": "couldn't Add a review"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_suggestions(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_suggestions = SuggestionsSerializer(data=request.data)
    if new_suggestions.is_valid():
        new_suggestions.save()
        data = {
            "msg": "Added Successfully",
            "suggestions": new_suggestions.data
        }
        return Response(data)
    else:
        print(new_suggestions.errors)
        data = {"msg": "couldn't Add a suggestions"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_series(request: Request):
    series = Series.objects.all()

    data = {
        "msg": "List of All Series",
        "Series": SeriesSerializer(instance=series, many=True).data
    }

    return Response(data)


@api_view(['GET'])
def list_review(request: Request):
    review = Review.objects.all()

    data = {
        "msg": "List of All Reviews",
        "Review": ReviewSerializer(instance=review, many=True).data
    }

    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_suggestions(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    suggestions = Suggestions.objects.all()

    data = {
        "msg": "List of All Suggestions",
        "Suggestions": SuggestionsSerializer(instance=suggestions, many=True).data
    }

    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_series(request: Request, series_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    series = Series.objects.get(id=series_id)

    updated_series = SeriesSerializer(instance=series, data=request.data)
    if updated_series.is_valid():
        updated_series.save()
        data = {
            "msg": "updated successfully"
        }

        return Response(data)
    else:
        print(updated_series.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_review(request: Request, review_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    review = Review.objects.get(id=review_id)

    updated_review = ReviewSerializer(instance=review, data=request.data)
    if updated_review.is_valid():
        updated_review.save()
        data = {
            "msg": "updated successfully"
        }

        return Response(data)
    else:
        print(updated_review.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_suggestions(request: Request, suggestions_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    suggestions = Suggestions.objects.get(id=suggestions_id)

    updated_suggestions = SuggestionsSerializer(instance=suggestions, data=request.data)
    if updated_suggestions.is_valid():
        updated_suggestions.save()
        data = {
            "msg": "updated successfully"
        }

        return Response(data)
    else:
        print(updated_suggestions.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_series(request: Request, series_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    series = Series.objects.get(id=series_id)
    series.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_review(request: Request, review_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    review = Review.objects.get(id=review_id)
    review.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_suggestions(request: Request, suggestions_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    suggestions = Suggestions.objects.get(id=suggestions_id)
    suggestions.delete()
    return Response({"msg": "Deleted Successfully"})
