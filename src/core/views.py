from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count, Sum, Max
from .models import *
# Create your views here.


@login_required
def home(request):
    data_likes=[]
    indiaLikes = India.objects.values('categoryId').annotate(likes1=Max('endLikes'))
    UKlikes = UK.objects.values('categoryId').annotate(likes2=Max('endLikes'))
    USlikes = US.objects.values('categoryId').annotate(likes3=Max('endLikes'))
    for entry in indiaLikes:
        data_likes.append(entry['likes1'])
    for entry in UKlikes:
        data_likes.append(entry['likes2'])
    for entry in USlikes:
        data_likes.append(entry['likes3'])
    maxLike=max(data_likes)

    data_views=[]
    indiaViews = India.objects.values('categoryId').annotate(views1=Max('endViews'))
    UKViews = UK.objects.values('categoryId').annotate(views2=Max('endViews'))
    USViews = US.objects.values('categoryId').annotate(views3=Max('endViews'))
    for entry in indiaViews:
        data_views.append(entry['views1'])
    for entry in UKViews:
        data_views.append(entry['views2'])
    for entry in USViews:
        data_views.append(entry['views3'])
    maxView=max(data_views)

    data_dislikes=[]
    indiaDis = India.objects.values('categoryId').annotate(dl1=Max('endDislikes'))
    UKDis = UK.objects.values('categoryId').annotate(dl2=Max('endDislikes'))
    USdis = US.objects.values('categoryId').annotate(dl3=Max('endDislikes'))
    for entry in indiaDis:
        data_dislikes.append(entry['dl1'])
    for entry in UKDis:
        data_dislikes.append(entry['dl2'])
    for entry in USdis:
        data_dislikes.append(entry['dl3'])
    maxDislike=max(data_dislikes)
    print(maxDislike)

    
    context = {
        'title': 'Home',
        'maxLike':maxLike,
        'maxView':maxView,
        'maxDislike':maxDislike
    }
    return render(request, 'core/home.html', context)

def splash(request):

    context = {
        'title': 'splash',
    }
    return render(request, 'core/splash.html', context)

@login_required
def about(request):

    context = {
        'title': 'About',
    }
    return render(request, 'core/about.html', context)

@login_required
def us(request):

    context = {
        'title': 'US',
    }
    return render(request, 'core/us.html', context)


@login_required
def uk(request):

    context = {
        'title': 'UK',
    }
    return render(request, 'core/uk.html', context)


@login_required
def india(request):

    context = {
        'title': 'India',
    }
    return render(request, 'core/india.html', context)

@login_required
def report(request):

    context = {
        'title': 'Report',
    }
    return render(request, 'core/cap.html', context)

def home_bubble_chart(request):
    uk_likes = []
    uk_views = []
    uk_labels = []
    us_likes = []
    us_views = []
    us_labels = []
    india_likes = []
    india_views = []
    india_labels = []
    uk = UK.objects.values('categoryId').annotate(
        total_likes=Sum('endLikes'), total_views=Sum('endViews'))
    india = India.objects.values('categoryId').annotate(
        total_likes=Sum('endLikes'), total_views=Sum('endViews'))
    us = US.objects.values('categoryId').annotate(
        total_likes=Sum('endLikes'), total_views=Sum('endViews'))
    for entry in uk:
        uk_likes.append(entry['total_likes'])
        uk_views.append(entry['total_views'])
        uk_labels.append(entry['categoryId'])
    for entry in us:
        us_likes.append(entry['total_likes'])
        us_views.append(entry['total_views'])
        us_labels.append(entry['categoryId'])
    for entry in india:
        india_likes.append(entry['total_likes'])
        india_views.append(entry['total_views'])
        india_labels.append(entry['categoryId'])
    return JsonResponse(data={
        'uk_labels': uk_labels,
        'uk_views': uk_views,
        'uk_likes': uk_likes,
        'us_labels': us_labels,
        'us_views': us_views,
        'us_likes': us_likes,
        'india_labels': india_labels,
        'india_views': india_views,
        'india_likes': india_likes,
    })


def britain_most_trending_channel(request):
    labels = []
    data = []
    uk = UK.objects.values('channelTitle').annotate(
        total=Count('id')).order_by('total').reverse()[:10]
    for entry in uk:
        labels.append(entry['channelTitle'])
        data.append(entry['total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def us_most_trending_channel(request):
    labels = []
    data = []
    us = US.objects.values('channelTitle').annotate(
        total=Count('id')).order_by('total').reverse()[:10]
    for entry in us:
        labels.append(entry['channelTitle'])
        data.append(entry['total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def india_most_trending_channel(request):
    labels = []
    data = []
    india = India.objects.values('channelTitle').annotate(
        total=Count('id')).order_by('total').reverse()[:10]
    for entry in india:
        labels.append(entry['channelTitle'])
        data.append(entry['total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def britain_category_count_chart(request):
    ukLabels = uk_labels()
    data = []
    uk = UK.objects.values('categoryId').annotate(total=Count('id'))
    for entry in uk:
        data.append(entry['total'])

    return JsonResponse(data={
        'labels': ukLabels,
        'data': data,
    })


def india_category_count_chart(request):
    indiaLabels = india_labels()
    data = []
    india = India.objects.values('categoryId').annotate(total=Count('id'))
    for entry in india:
        data.append(entry['total'])

    return JsonResponse(data={
        'labels': indiaLabels,
        'data': data,
    })


def us_category_count_chart(request):
    usLabels = us_labels()
    data = []
    us = US.objects.values('categoryId').annotate(total=Count('id'))
    for entry in us:
        data.append(entry['total'])

    return JsonResponse(data={
        'labels': usLabels,
        'data': data,
    })

def britain_category_graph_line(request):
    ukLabels = uk_labels()
    data_likes = []
    data_dislikes = []
    data_comments = []
    uk = UK.objects.values('categoryId').annotate(total_likes=Sum(
        'endLikes'), total_dislikes=Sum('endDislikes'), total_comments=Sum('endCommentCount'))
    for entry in uk:
        data_likes.append(entry['total_likes'])
        data_dislikes.append(entry['total_dislikes'])
        data_comments.append(entry['total_comments'])
    return JsonResponse(data={
        'labels': ukLabels,
        'data_likes': data_likes,
        'data_dislikes': data_dislikes,
        'data_comments': data_comments,
    })


def india_category_graph_line(request):
    indiaLabels = india_labels()
    data_likes = []
    data_dislikes = []
    data_comments = []
    india = India.objects.values('categoryId').annotate(total_likes=Sum(
        'endLikes'), total_dislikes=Sum('endDislikes'), total_comments=Sum('endCommentCount'))
    for entry in india:
        data_likes.append(entry['total_likes'])
        data_dislikes.append(entry['total_dislikes'])
        data_comments.append(entry['total_comments'])

    return JsonResponse(data={
        'labels': indiaLabels,
        'data_likes': data_likes,
        'data_dislikes': data_dislikes,
        'data_comments': data_comments,
    })


def us_category_graph_line(request):
    usLabels = us_labels()
    data_likes = []
    data_dislikes = []
    data_comments = []
    us = US.objects.values('categoryId').annotate(total_likes=Sum(
        'endLikes'), total_dislikes=Sum('endDislikes'), total_comments=Sum('endCommentCount'))
    for entry in us:
        data_likes.append(entry['total_likes'])
        data_dislikes.append(entry['total_dislikes'])
        data_comments.append(entry['total_comments'])

    return JsonResponse(data={
        'labels': usLabels,
        'data_likes': data_likes,
        'data_dislikes': data_dislikes,
        'data_comments': data_comments,
    })


def us_labels():
    labels = ["Film & Animation", "Autos & Vehicles",
              "Music", "Pets & Animals", "Sports", "Travel & Events", "Gaming", "People & Blogs", "Comedy", "Entertainment", "News & Politics", "Howto & Style", "Education", "Science & Technology", "Nonprofits & Activism", "Shows"]

    return labels


def india_labels():
    labels = ["Film & Animation", "Autos & Vehicles",
              "Music", "Pets & Animals", "Sports", "Travel & Events", "Gaming", "People & Blogs", "Comedy", "Entertainment", "News & Politics", "Howto & Style", "Education", "Science & Technology", "Nonprofits & Activism", "Movies", "Shows"]

    return labels


def uk_labels():
    labels = ["Film & Animation", "Autos & Vehicles",
              "Music", "Pets & Animals", "Sports", "Travel & Events", "Gaming", "People & Blogs", "Comedy", "Entertainment", "News & Politics", "Howto & Style", "Education", "Science & Technology", "Nonprofits & Activism"]

    return labels
