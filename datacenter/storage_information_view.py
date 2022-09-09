from django.utils.timezone import localtime 
from django.shortcuts import render, get_list_or_404
from datacenter.models import Visit, get_duration, format_duration


def storage_information_view(request):
    visit = get_list_or_404(Visit, leaved_at__isnull=True)
    non_closed_visits = list()
    for some_visit in visit:   
        entered_at = localtime(some_visit.entered_at)
        duration = format_duration(get_duration(some_visit))
        who_entered = some_visit.passcard
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)




    