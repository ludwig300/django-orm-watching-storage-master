from datacenter.models import Passcard, Visit
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render, get_list_or_404, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visit = get_list_or_404(Visit, passcard=passcard)
    this_passcard_visits = list()
    for some_visit in visit:
        duration = format_duration(get_duration(some_visit))
        is_strange = is_visit_long(some_visit)
        this_passcard_visits.append(
            {
                'entered_at': some_visit.entered_at,
                'duration': duration,
                'is_strange': is_strange
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
