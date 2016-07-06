from blog_posts.models import Subject

def subjects_generator(request):
    return {'subjects_list':Subject.objects.all()}