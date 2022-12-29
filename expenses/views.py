# Create your views here.
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseModelForm


def index(request):

    expenses = Expense.objects.all()  # 查詢所有資料

    form = ExpenseModelForm()

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


def update(request, pk):

    expense = Expense.objects.get(id=pk)

    form = ExpenseModelForm(instance=expense)

    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        if form.is_valid():#Form的對象主要任務是驗證data,使用is_valid()來進行驗證，它會回傳boolean
            form.save()
        return redirect('/expenses')

    context = {
        'form': form
    }

    return render(request, 'expenses/update.html', context)


def delete(request, pk):

    expense = Expense.objects.get(id=pk)

    if request.method == "POST":
        expense.delete()
        return redirect('/expenses')

    context = {
        'expense': expense
    }

    return render(request, 'expenses/delete.html', context)
