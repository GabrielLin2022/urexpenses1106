from django import forms
from .models import Expense


class ExpenseModelForm(forms.ModelForm):
    #繼承自ModelForm類別，並且在其中設定表單所要綁定的資料模型名稱
    class Meta:
        model = Expense
        fields = '__all__'#要指定在網站上所要顯示的表單欄位，可以透過fields屬性來進行設定
        #如果要顯示資料模型(Model)中的所有欄位，fields屬性的設定可以簡寫為__all__
        #Django ModelForm也提供了widgets屬性，用來客製化表單的顯示外觀，這邊套用Bootstrap的表單CSS類別
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        #由於在資料模型(Model)中，都是定義英文的屬性(Attribute)，所以表單欄位的標題也會顯示英文名稱，如果想要進行修改，
        #可以透過labels屬性來設定
        labels = {
            'name': '花費項目',
            'price': '金額'
        }