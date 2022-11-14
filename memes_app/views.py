import os
import random

from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F
from django.conf import settings

from .forms import *
from .models import *

def index(request):
    user = request.user
    return render(request, 'memes_app/index.html', {'user':user})

def meme_page(request):
    # if request.method=="POST":
    # id=request.POST.get('id')
    id = request.user.id

    imagelist=os.listdir(os.path.join(settings.STATIC_DIR, 'images2'))
    print("=======>Image list: ", imagelist)
    all_image=SubmitImage.objects.all()
    print(all_image)
    for instance in all_image:
        image_url=instance.image
        if image_url in imagelist:
            imagelist.remove(image_url)
    imageurl=imagelist[0]
    #user=UserImage.objects.get(userid=id)
    user=UserImage.objects.filter(userid=id)
    if user.exists():
        user=UserImage.objects.get(userid=id)
        number=user.annoted_image
    else:
        number=0
    return render(request,'memes_app/meme_page.html',{'imageurl':imageurl,'image_form':imageform,'id':id,'number':number, 'user':request.user})


def selectiveimage(request):
    imagelist=os.listdir(os.path.join(settings.STATIC_DIR, 'images2'))
    all_image=SubmitImage.objects.all()
    for instance in all_image:
        image_url=instance.image
        if image_url in imagelist:
            imagelist.remove(image_url)
    imageurl=imagelist[0]
    id=request.POST.get('userid')
    user=UserImage.objects.filter(userid=id)
    if user.exists():
        user=UserImage.objects.get(userid=id)
        number=user.annoted_image

    else:
        number=0
    template_name='memes_app/meme_page.html'


    if request.method=="POST":

        image_form=imageform(request.POST)
        #print('form prevalidation')
        if image_form.is_valid():

            #print('form valid')
            pic=request.POST.get('test')
            id=request.user.id
            if id=="None":
                return redirect('index')

            else:
                if pic=="pic1.jpg":
                    pic="very_negative"
                elif pic=="pic2.jpg":
                    pic="negative"
                elif pic=="pic3.jpg":
                    pic="neutral"
                elif pic=="pic4.jpg":
                    pic="positive"
                elif pic=="pic5.jpg":
                    pic="very_positive"
                image_instance = image_form.save(commit=False)
                image_instance.image = imageurl
                image_instance.pic_overall=pic
                image_instance.save()

                user=UserImage.objects.filter(userid=id)
                if user.exists():
                    UserImage.objects.filter(userid=id).update(annoted_image=F("annoted_image") + 1)

                else:
                # Do that...
                    UserImage.objects.create(userid=request.user,annoted_image=1)


                #print(image_instance.pic_humour)
                file=open("data.txt","a")
                file.write(str(imageurl)+","+str(image_instance.pic_humour)+","+str(image_instance.pic_sarcastic)+","+str(image_instance.pic_offensive)+","+str(image_instance.pic_motivational)+","+str(pic))
                file.write("\n")
                file.close()
            
                imagelist=os.listdir(os.path.join(settings.STATIC_DIR, 'images2'))
                all_image=SubmitImage.objects.all()
                for instance in all_image:
                    image_url=instance.image
                    if image_url in imagelist:
                        imagelist.remove(image_url)
                imageurl=imagelist[0]
                user=UserImage.objects.filter(userid=id)
                if user.exists():
                    user=UserImage.objects.get(userid=id)
                    number=user.annoted_image

                else:
                    number=0
                template_name='memes_app/meme_page.html'
                return render(request,template_name,{'imageurl':imageurl,'image_form':imageform,'id':id,'number':number})


        print(image_form.errors)


    return render(request,template_name,{'imageurl':imageurl,'image_form':imageform,'id':id,'number':number})
