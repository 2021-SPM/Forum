from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from notifications.signals import notify

from forum.models import Post
from simpleforum.settings import DEFAULT_FROM_EMAIL
from .forms import CommentForm


# os.environ['DJANGO_SETTINGS_MODULE'] = 'simpleforum/settings.py'


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.commentator = request.user
        comment.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             '评论发表成功！',
                             extra_tags='success')
        if request.user != post.author:
            notify.send(request.user,
                        recipient=post.author,
                        verb='评论了你',
                        target=post)
            if post.emailNotice:
                subject = 'Notifications from the Forum'
                text_content = 'Someone has left a comment under your post, go and check!'
                html_content = '<strong>Someone has left a comment under your post "{}"!</strong><br/>'.format(
                    post.title) + '<a href="http://127.0.0.1:8000/article/{}" >Click the link and check!'.format(post_pk) + '</a>'
                to = post.author.email
                msg = EmailMultiAlternatives(subject, text_content, DEFAULT_FROM_EMAIL, [to])
                msg.attach_alternative(html_content, 'text/html')
                msg.send()
        return redirect(post)
    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request,
                         messages.ERROR,
                         '评论发表失败！请修改表单中的错误后重新提交。',
                         extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)
