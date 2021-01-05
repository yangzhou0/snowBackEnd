# added some comments
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm
from .models import Comment, Resort
from .serializers import ResortSerializer, CommentSerializer
import json

def all_resorts(request):
    resorts = Resort.objects.all()
    serialized_resorts = ResortSerializer(resorts).all_resorts
    return JsonResponse(data=serialized_resorts, safe=False,status=200)


def resort_detail(request, resort_id):
    resort = Resort.objects.get(id=resort_id)
    serialized_resort = ResortSerializer(resort).resort_detail
    return JsonResponse(data=serialized_resort, status=200)


def resort_comments(request,resort_id):
    resort = Resort.objects.get(id=resort_id)
    serialized_resort = ResortSerializer(resort).resort_detail
    serialized_comments = serialized_resort['comments']
    return JsonResponse(data=serialized_comments, safe=False,status=200)

@csrf_exempt
def like_resort(request,resort_id):
    if request.method == "POST":
        likes = Resort.objects.get(id=resort_id).likes
        Resort.objects.filter(id=resort_id).update(likes = likes + 1) 
        updated_resort = Resort.objects.get(id=resort_id)
        serialized_resort = ResortSerializer(updated_resort).resort_detail
        return JsonResponse(data=serialized_resort, status=200)


def comment_detail(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    serialized_comment = CommentSerializer(comment).comment_detail
    return JsonResponse(data=serialized_comment, status=200)

@csrf_exempt
def new_comment(request):
    if request.method == "POST":
        data = json.load(request)
        form = CommentForm(data)
        if form.is_valid():
            comment = form.save(commit=True)
            serialized_comment = CommentSerializer(comment).comment_detail
            return JsonResponse(data=serialized_comment, status=200)
@csrf_exempt
def like_comment(request,comment_id):
    if request.method == "POST":
        likes = Comment.objects.get(id=comment_id).likes
        Comment.objects.filter(id=comment_id).update(likes = likes + 1) 
        updated_comment = Comment.objects.get(id=comment_id)
        serialized_comment = CommentSerializer(updated_comment).comment_detail
        return JsonResponse(data=serialized_comment, status=200)

@csrf_exempt
def edit_comment(request,comment_id): # this can be used to update comment body or likes
    if request.method == "POST":
        data = json.load(request)
        for k,v in data.items():
            if k == 'body':
                Comment.objects.filter(id=comment_id).update(body=v)
        updated_comment = Comment.objects.get(id=comment_id)
        serialized_comment = CommentSerializer(updated_comment).comment_detail
        return JsonResponse(data=serialized_comment, status=200)

@csrf_exempt
def delete_comment(request,comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return JsonResponse(data={'status':f"successfully deleted {comment.body}"}, status=200)


