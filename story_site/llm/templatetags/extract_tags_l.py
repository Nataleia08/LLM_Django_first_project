from django import template

register = template.Library()


def tags(llm_tags):
    return ', '.join([str(name) for name in llm_tags.all()])


register.filter('tags', tags)

