from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import redirect

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ['-created_at']

class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"

class PostCreateView(SuccessMessageMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = "blog/post_create.html"
	success_url = reverse_lazy('core:post_list')
	success_message = "Postagem criada com sucesso!"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(SuccessMessageMixin, UpdateView):
	model = Post
	form_class = PostForm
	template_name = "blog/post_create.html"
	success_url = reverse_lazy('core:post_list')
	success_message = "Postagem atualizada com sucesso!"

class PostDeleteView(SuccessMessageMixin, DeleteView):
	model = Post
	template_name = "blog/post_delete_confirmation.html"
	success_url = reverse_lazy('core:post_list')
	success_message = "Postagem deletada com sucesso!"


post_list = PostListView.as_view()
post_detail = PostDetailView.as_view()
post_create = PostCreateView.as_view()
post_update = PostUpdateView.as_view()
post_delete = PostDeleteView.as_view()

# def post_list_dois(request):
#     posts = Post.objects.all() 
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_create(request):
#      if request.method == "POST":
#          form = PostForm(request.POST)
#          if form.is_valid():
#              post = form.save(commit=False)
#              post.author = request.user
#              post.save()
#              return redirect('core:post_list')
#      else:
#          form = PostForm()
#      return render(request, 'blog/post_create.html', {'form': form})
