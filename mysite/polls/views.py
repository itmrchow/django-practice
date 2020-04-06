"""view"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.


# 顯示對象列表
class IndexView(generic.ListView):
    "首頁"
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """返回最近發布的5個問題"""
        return Question.objects.filter(
            pub_date__lte=timezone.now
        ).order_by('-pub_date')[:5]

# 顯示特定類型對象的詳細資訊頁面


class DetailView(generic.DetailView):
    "詳細"
    model = Question

    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    "結果"
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    "投票"
    # 檢查該投票是否存在
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 重新顯示問題投票表
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功處理後始終返回HttpResponseRedirect
        # 包含POST數據。 如果出現以下情況，這可以防止使用者觸發兩次back
        # HttpResponseRedirect：重新導向
        # 反向url
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
