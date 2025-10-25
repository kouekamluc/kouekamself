from django.shortcuts import render, get_object_or_404
from .models import Project


def portfolio_list(request):
    """List view for portfolio projects."""
    projects = Project.objects.all()
    featured_projects = projects.filter(featured=True)
    
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
    }
    return render(request, 'portfolio/portfolio_list.html', context)


def portfolio_detail(request, slug):
    """Detail view for individual portfolio projects."""
    project = get_object_or_404(Project, slug=slug)
    
    # Get related projects (same technologies)
    related_projects = Project.objects.filter(
        technology_stack__icontains=project.technology_stack.split(',')[0]
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/portfolio_detail.html', context)