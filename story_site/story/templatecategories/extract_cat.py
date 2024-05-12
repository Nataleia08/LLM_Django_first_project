from django import template

register = template.Library()


def categories(story_categories):
    return ', '.join([str(name) for name in story_categories.all()])


register.filter('categories', categories)

