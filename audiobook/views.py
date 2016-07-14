from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import BookForm, ChapterForm, UserForm
from .models import Book, Chapter

TRANSCRIPT_FILE_TYPES = ['vtt']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_book(request):
    if not request.user.is_authenticated():
        return render(request, 'audiobook/login.html')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.book_cover = request.FILES['book_cover']
            file_type = book.book_cover.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'book': book,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'audiobook/create_book.html', context)
            book.save()
            return render(request, 'audiobook/detail.html', {'book': book})
        context = {
            "form": form,
        }
        return render(request, 'audiobook/create_book.html', context)


def create_chapter(request, book_id):
    form = ChapterForm(request.POST or None, request.FILES or None)
    book = get_object_or_404(Book, pk=book_id)
    if form.is_valid():
        books_chapters = book.chapter_set.all()

        for s in books_chapters:
            if s.chapter == form.cleaned_data.get("chapter"):
                context = {
                    'book': book,
                    'form': form,
                    'error_message': 'You already added that chapter',
                }
                return render(request, 'audiobook/create_chapter.html', context)
        chapter = form.save(commit=False)
        chapter.book = book
        chapter.YouTube_key = youtubekey(chapter.YouTube_link)

        chapter.transcriptVTT_file = request.FILES['transcriptVTT_file']
        file_type = chapter.transcriptVTT_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in TRANSCRIPT_FILE_TYPES:
            context = {
                'book': book,
                'form': form,
                'error_message': 'Transcript file must be VTT',
            }
            return render(request, 'audiobook/create_chapter.html', context)

        chapter.save()
        return render(request, 'audiobook/detail.html', {'book': book})
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'audiobook/create_chapter.html', context)


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    books = Book.objects.filter(user=request.user)
    return render(request, 'audiobook/index.html', {'books': books})


def delete_chapter(request, book_id, chapter_id):
    book = get_object_or_404(Book, pk=book_id)
    chapter = Chapter.objects.get(pk=chapter_id)
    chapter.delete()
    return render(request, 'audiobook/detail.html', {'book': book})


def detail(request, book_id):


    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'audiobook/detail.html', {'book': book})








def index(request):
    books = Book.objects.all()
    chapter_results = Chapter.objects.all()
    query = request.GET.get("q")
    if query:
        books = books.filter(
            Q(book_title__icontains=query) |
            Q(writer__icontains=query)
        ).distinct()
        chapter_results = chapter_results.filter(
            Q(chapter__icontains=query)
        ).distinct()
        return render(request, 'audiobook/index.html', {
            'books': books,
            'chapters': chapter_results,
        })
    else:
        return render(request, 'audiobook/index.html', {'books': books})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'audiobook/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.all()
                return render(request, 'audiobook/index.html', {'books': books})
            else:
                return render(request, 'audiobook/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'audiobook/login.html', {'error_message': 'Invalid login'})
    return render(request, 'audiobook/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'audiobook/index.html', {'books': books})
    context = {
        "form": form,
    }
    return render(request, 'audiobook/register.html', context)


def chapters(request):

    try:
        chapter_ids = []
        for book in Book.objects.all():
            for chapter in book.chapter_set.all():
                chapter_ids.append(chapter.pk)
        users_chapters = Chapter.objects.filter(pk__in=chapter_ids)

    except Book.DoesNotExist:
        users_chapters = []
    return render(request, 'audiobook/chapters.html', {
        'chapter_list': users_chapters,

    })


def play(request):

    books = Book.objects.all()
    chapter_results = Chapter.objects.all()
    query = request.GET.get("q")
    if query:
        books = books.filter(
            Q(book_title__icontains=query) |
            Q(writer__icontains=query)
        ).distinct()
        chapter_results = chapter_results.filter(
            Q(chapter__icontains=query)
        ).distinct()
        return render(request, 'audiobook/index.html', {
            'books': books,
            'chapters': chapter_results,
        })
    else:
        return render(request, 'audiobook/audio.html', {'books': books})


def youtubekey(link):
    location = link.find('www.youtube.com/watch?v=')
    if location != -1:
        return link[location+24:location+24+11]

