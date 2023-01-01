# Create your views here.
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseModelForm

#=================================================新增
def index(request):

    expenses = Expense.objects.all()  # 查詢所有資料

    form = ExpenseModelForm() #建立實體物件

    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/expenses")

    context = {
        'expenses': expenses,
        'form': form
    }

    return render(request, 'expenses/index.html', context)

#=================================================修改
def update(request, pk):

    expense = Expense.objects.get(id=pk)#從資料表取得id, 指給pk, 再傳上去 update(pk)

    form = ExpenseModelForm(instance=expense)##instance 表拿取 expense 內部資料，也就是從資料庫經由objects取得的資料

    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense) #instance 表拿取 expense 內部資料，也就是從資料庫經由objects取得的資料
        if form.is_valid():#Form的對象主要任務是驗證data,使用is_valid()來進行驗證，它會回傳boolean
            form.save()
        return redirect('/expenses')

    context = {
        'form': form
    }

    return render(request, 'expenses/update.html', context)

#=================================================刪除
def delete(request, pk):

    expense = Expense.objects.get(id=pk)

    if request.method == "POST":
        expense.delete()
        return redirect('/expenses')

    context = {
        'expense': expense
    }

    return render(request, 'expenses/delete.html', context)
