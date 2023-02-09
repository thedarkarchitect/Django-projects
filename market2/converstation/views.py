from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from items.models import Item
from .models import *

from .forms import *
# Create your views here.

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:#if you are the owener you should not be able to visit this page
        return redirect('dashboard:index')

    conversation = Conversation.objects.filter(item=item).filter(member__in=[request.user.id]) #this shows existing conversation

    if conversation:
        # pass #redirect to conversation
        return redirect('converstation:detail', pk=conversation.first().id)

    if request.method == 'POST':
        form = ConversationMessage(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    
    context = {
        'form':form,
    }
    
    return render(request, 'coversation/new.html', context)

@login_required
def inbox(request):
    conversation = Conversation.objects.filter(member__in=[request.user.id])

    context  = {
        'conversation':conversation
    }

    return render(request, 'converstation/inbox.html', context)

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(member__in=[request.user.id]).get(pk=pk)
    form = ConversationMessaageForm()

    if request.method == 'POST':
        form = ConversationMessaageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('converstation:detail', pk=pk)

    context={
        'conversation':conversation,
        'form':form
    }
    return render(request, 'converstation/detail.html', conversation)
