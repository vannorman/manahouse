from django.shortcuts import render
def main(request):
    """View function for home page of site."""

    context = {
        'faq' : [
            {
                'q' : 'quesiton1',
                'a' : 'question2',
             },
            {
                'q' : 'quesiton1',
                'a' : 'question2',
             },
        ]
#        'num_books': num_books,
#        'num_instances': num_instances,
#        'num_instances_available': num_instances_available,
#        'num_authors': num_authors,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    

