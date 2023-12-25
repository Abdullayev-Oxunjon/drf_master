from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Like, Product


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_product(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)



    if Like.objects.filter(user=user, product=product).exists():
        return Response({'message': 'You have already liked this product'})
    else:
        like = Like.objects.create(user=user, product=product)
        like.save()


        return Response({'message': 'Product liked successfully'})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unlike_product(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)

    like = Like.objects.filter(user=user, product=product).first()
    if not like:
        return Response({'message': 'You have not liked this product'})
    else:
        like.delete()
        return Response({'message': 'Product unliked successfully'})


