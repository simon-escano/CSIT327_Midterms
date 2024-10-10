from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='categories')

    def add_post(self, post):
        return self.posts.add(post)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Archive(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()

    def get_posts(self):
        return Post.objects.filter(created_at__year=self.year, created_at__month=self.month)

def get_all_authors():
    return Author.objects.all()

def get_comment_count(post):
    return post.comments.count()

def get_recent_posts(limit=5):
    return Post.objects.order_by('-created_at')[:limit]

def get_posts_by_category(category):
    return Post.objects.filter(categories=category)

def search_posts(query):
    return Post.objects.filter(content__icontains=query)

def get_posts_with_comments():
    return Post.objects.annotate(comment_count=models.Count('comments'))
