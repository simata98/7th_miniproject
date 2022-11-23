from django.contrib import admin
from .models import Result, AiModel
from django.shortcuts import render

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
  list_display = ('id', 'answer', 'result', 'pub_date')
  ordering = ("-pub_date",)
  
  def changelist_view(self, request):
    correct_array = [["is_it_correct", "yes"],
                ["correct", 0],
                ["incorrect", 0],]
    for item in Result.objects.all():
        if item.answer == item.result:
            correct_array[1][1] += 1
        else:
            correct_array[2][1] += 1
            
    as_json = json.dumps(correct_array, cls=DjangoJSONEncoder)
    
    return super().changelist_view(request, {"correct_array": as_json})


@admin.register(AiModel)
class AimodelAdmin(admin.ModelAdmin):
  list_display = ("id", "model_name", "uploader", "create_date")
  ordering = ("-create_date",)
  
  def changelist_view(self, request, extra_context=None):
    chart_data = (
      AiModel.objects.annotate(date=TruncDay("create_date"))
      .values("date")
      .annotate(y=Count("id"))
      .order_by("-date")
    )
    
    as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
    extra_context = extra_context or {"chart_data": as_json}
    
    return super().changelist_view(request, extra_context=extra_context)