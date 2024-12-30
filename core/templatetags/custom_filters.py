# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Return the value for the given key in the dictionary."""
    return dictionary.get(key)
@register.filter
def filter_score(scores, activity):
    for score in scores:
        if score.activity == activity:
            return score
    return None


@register.filter
def get_item(dictionary, key):
    """
    Get an item from a dictionary or return empty list if not found
    Safely handles both dictionary and non-dictionary inputs
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key, [])
    return []

@register.filter
def get_criterion_activities(activities, criterion_type):
    """Get activities for a specific criterion type"""
    try:
        return [a for a in activities if a.subject_criterion.grading_criterion.criteria_type == criterion_type]
    except (AttributeError, TypeError):
        return []
    


@register.filter
def get_dict_value(dictionary, key):
    if dictionary is None:
        return None
    return dictionary.get(str(key))

@register.filter
def filter_by_period(activities, period_id):
    return [activity for activity in activities if activity.grading_period.id == int(period_id)]

@register.filter
def filter_by_period(activities, period_id):
    return [activity for activity in activities if activity.grading_period.id == int(period_id)]