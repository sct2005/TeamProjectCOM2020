from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
import json
import random
from .models import Exhibit, Quiz, Comment, QuizScore, UserProfile, Bookmark
from .forms import UsernameChangeForm, UserRoleForm, ExhibitForm, QuizForm
from .decorators import admin_required, curator_required, can_delete_comment

User = get_user_model()


# Menu page design: map exhibit title -> category, severity, categories (tags)
# Matches "Menu Page for Topics" design. Fallback: domain as category, severity 'medium'
EXHIBIT_MENU_META = {
    "The Outdated Inundation": {"category": "Environmental", "severity": "high", "categories": ["Environmental Management", "Urban Planning", "Risk Assessment"]},
    "The Resolution Mirage": {"category": "Agriculture", "severity": "high", "categories": ["Agricultural Surveillance", "Supply Chain Ethics", "Land-Cover"]},
    "The Overconfident Credit Dashboard": {"category": "Finance", "severity": "high", "categories": ["Fintech", "Lending", "Decision Support"]},
    "The Out-of-Context Arid Agriculture": {"category": "Agriculture", "severity": "high", "categories": ["Irrigation", "Agriculture", "Context Mismatch"]},
    "The Authoritative Air Quality Omission": {"category": "Public Health", "severity": "high", "categories": ["Smart City", "Public Health", "Data Visualization"]},
    "The \"Ghost Lane\" Traffic Optimizer": {"category": "Transport", "severity": "high", "categories": ["Autonomous Transportation", "Computer Vision", "Context Mismatch"]},
    "The Confidence-Blind Wildlife Tracker": {"category": "Conservation", "severity": "critical", "categories": ["Conservation Biology", "Decision Dashboard", "Uncertainty"]},
    "The Resolution-Blurred Property Line": {"category": "Legal Tech", "severity": "high", "categories": ["Real Estate", "Legal Tech", "Resolution Mismatch"]},
    "The Outdated Pandemic Supply Chain": {"category": "Healthcare", "severity": "critical", "categories": ["Logistics", "Healthcare", "Supply Chain"]},
    "The Authoritative Sea-Wall Projection": {"category": "Infrastructure", "severity": "critical", "categories": ["Civil Engineering", "Infrastructure", "Visualization"]},
    "The Subsurface Blind Spot": {"category": "Infrastructure", "severity": "critical", "categories": ["Civil Engineering", "Predictive Maintenance", "Infrastructure"]},
    "The Arctic Drift Bias": {"category": "Maritime", "severity": "high", "categories": ["Maritime Logistics", "Climate Research", "Navigation"]},
    "The High-Altitude Diagnostic": {"category": "Healthcare", "severity": "critical", "categories": ["Healthcare", "Telemedicine", "Context Mismatch"]},
    "The Solar Microgrid Blackout": {"category": "Energy", "severity": "critical", "categories": ["Energy", "Smart Grids", "Uncertainty"]},
    "The Precision-Mismatched Firebreak": {"category": "Emergency Services", "severity": "critical", "categories": ["Disaster Response", "Emergency Services", "Resolution Mismatch"]},
    "The Invisible Urban Heat Island": {"category": "Public Policy", "severity": "high", "categories": ["Social Services", "Public Policy", "Equity"]},
    "The Outdated Bio-Security Filter": {"category": "Agriculture", "severity": "high", "categories": ["Agriculture", "Pest Control", "Outdated Data"]},
    "The Forest Carbon Credit Mirage": {"category": "Finance", "severity": "high", "categories": ["Finance", "Sustainability", "Resolution Mismatch"]},
    "The Arid-Logic Flood Barrier": {"category": "Water Management", "severity": "critical", "categories": ["Water Management", "Climate Shift", "Context Mismatch"]},
    "The Confidence-Blind Dam Sensor": {"category": "Infrastructure", "severity": "critical", "categories": ["Public Infrastructure", "Monitoring", "Uncertainty"]},
}


def home(request):
    """Homepage: Menu Page for Topics design — case study cards with category filter."""
    exhibits = list(Exhibit.objects.all().order_by("title"))
    selected_category = (request.GET.get("category") or "all").strip()
    search_query = (request.GET.get("q") or "").strip()

    # Preload quiz scores for the authenticated user (for badge display)
    user_scores_by_exhibit_id = {}
    bookmarked_exhibit_ids = set()
    if request.user.is_authenticated:
        user_scores = QuizScore.objects.filter(user=request.user)
        user_scores_by_exhibit_id = {qs.exhibit_id: qs for qs in user_scores}
        # User bookmarks
        bookmarked_exhibit_ids = set(
            Bookmark.objects.filter(user=request.user).values_list("exhibit_id", flat=True)
        )

    # Attach menu metadata (category, severity, categories) and user quiz badge to each exhibit
    for ex in exhibits:
        meta = EXHIBIT_MENU_META.get(ex.title)
        if meta:
            ex.menu_category = meta["category"]
            ex.menu_severity = meta["severity"]
            ex.menu_categories = meta["categories"]
        else:
            ex.menu_category = ex.domain or "Other"
            ex.menu_severity = "medium"
            ex.menu_categories = [ex.domain] if ex.domain else []

        # Attach user-specific quiz badge metadata, if a score exists
        quiz_score = user_scores_by_exhibit_id.get(ex.id)
        ex.user_quiz_score = None
        ex.user_quiz_badge = None
        ex.user_quiz_badge_level = None
        ex.user_quiz_dot_level = "none"  # for score dot: none | bronze | silver | gold
        if quiz_score:
            ex.user_quiz_score = quiz_score.score_percentage
            if quiz_score.score_percentage >= 80:
                ex.user_quiz_badge = "Mastered"
                ex.user_quiz_badge_level = "gold"
                ex.user_quiz_dot_level = "gold"
            elif quiz_score.score_percentage >= 50:
                ex.user_quiz_badge = "In Progress"
                ex.user_quiz_badge_level = "silver"
                ex.user_quiz_dot_level = "silver"
            elif quiz_score.score_percentage > 0:
                ex.user_quiz_badge = "Started"
                ex.user_quiz_badge_level = "bronze"
                ex.user_quiz_dot_level = "bronze"

        # Bookmark flag for UI
        ex.is_bookmarked = ex.id in bookmarked_exhibit_ids

    # Unique categories for tabs (from exhibits) plus a Bookmarks tab for logged-in users
    base_categories = sorted({ex.menu_category for ex in exhibits if ex.menu_category}, key=str.lower)
    categories = ["all"]
    if request.user.is_authenticated and bookmarked_exhibit_ids:
        categories.append("bookmarks")
    categories.extend(base_categories)
    total_count = len(exhibits)
    critical_count = sum(1 for ex in exhibits if ex.menu_severity == "critical")
    category_count = len(categories) - 1  # exclude 'all'

    if selected_category == "bookmarks" and request.user.is_authenticated:
        exhibits = [ex for ex in exhibits if ex.id in bookmarked_exhibit_ids]
    elif selected_category != "all":
        exhibits = [ex for ex in exhibits if ex.menu_category == selected_category]

    # Text search by exhibit title (case-insensitive)
    if search_query:
        q_lower = search_query.lower()
        exhibits = [ex for ex in exhibits if q_lower in (ex.title or "").lower()]

    return render(request, "exhibits/home.html", {
        "exhibits": exhibits,
        "categories": categories,
        "selected_category": selected_category,
        "total_count": total_count,
        "critical_count": critical_count,
        "category_count": category_count,
        "search_query": search_query,
    })


def exhibit_list(request):
    exhibits = Exhibit.objects.all()
    return render(request, "exhibits/exhibit_list.html", {
        "exhibits": exhibits
    })

def exhibit_detail(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    comments = (
        Comment.objects.filter(exhibit=exhibit, parent__isnull=True)
        .prefetch_related("replies__replies__replies")
    )
    # Bookmark state for the current user
    is_bookmarked = False
    if request.user.is_authenticated:
        is_bookmarked = Bookmark.objects.filter(user=request.user, exhibit=exhibit).exists()
    # Split timeline into entries for visual timeline (by newlines or by ". " for single paragraph)
    timeline_entries = []
    if exhibit.timeline and exhibit.timeline.strip():
        raw = exhibit.timeline.strip()
        if "\n" in raw:
            timeline_entries = [s.strip() for s in raw.split("\n") if s.strip()]
        else:
            timeline_entries = [s.strip() for s in raw.split(". ") if s.strip()]
    return render(request, "exhibits/exhibit_detail.html", {
        "exhibit": exhibit,
        "comments": comments,
        "timeline_entries": timeline_entries,
        "is_bookmarked": is_bookmarked,
    })

@require_POST
def post_comment(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)

    if not request.user.is_authenticated:
        login_url = reverse("login")
        next_url = reverse("exhibits:detail", args=[exhibit.id]) + "#comments"
        return redirect(f"{login_url}?next={next_url}")

    body = (request.POST.get("body") or "").strip()
    parent_id_raw = (request.POST.get("parent_id") or "").strip()

    if not body:
        return HttpResponseBadRequest("body is required")

    parent = None
    if parent_id_raw:
        try:
            parent_id = int(parent_id_raw)
        except ValueError:
            return HttpResponseBadRequest("parent_id must be an integer")
        parent = get_object_or_404(Comment, pk=parent_id, exhibit=exhibit)

    display_name = (
        request.user.get_full_name()
        or request.user.get_username()
        or "Anonymous"
    )

    Comment.objects.create(
        exhibit=exhibit,
        parent=parent,
        user=request.user,
        author_name=display_name[:80],
        body=body[:2000],
    )

    return redirect(reverse("exhibits:detail", args=[exhibit.id]) + "#comments")


@login_required
@require_POST
def toggle_bookmark(request, pk):
    """Toggle bookmark for an exhibit for the current user."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, exhibit=exhibit)
    if not created:
        bookmark.delete()
        messages.success(request, "Exhibit removed from your bookmarks.")
    else:
        messages.success(request, "Exhibit added to your bookmarks.")

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or reverse("exhibits:detail", args=[exhibit.id])
    return redirect(next_url)


@require_POST
def delete_comment(request, pk, comment_id):
    """Allow a user to delete their own comment, or admins to delete any comment."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id, exhibit=exhibit)

    if not request.user.is_authenticated:
        login_url = reverse("login")
        next_url = reverse("exhibits:detail", args=[exhibit.id]) + "#comments"
        return redirect(f"{login_url}?next={next_url}")

    if not can_delete_comment(request.user, comment):
        return HttpResponseForbidden("You can only delete your own comments.")

    comment.delete()
    return redirect(reverse("exhibits:detail", args=[exhibit.id]) + "#comments")

def quiz_view(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    quizzes = exhibit.quizzes.all()
    
    # Filter out quizzes with no options or empty options
    quizzes = [q for q in quizzes if q.options and len(q.options) > 0]
    
    if not quizzes:
        return render(request, "exhibits/quiz.html", {
            "exhibit": exhibit,
            "quizzes": [],
            "error": "No quiz questions available for this exhibit."
        })
    
    if request.method == "POST":
        # Process quiz submission
        total_questions = len(quizzes)
        correct_answers = 0
        results = []
        
        for quiz in quizzes:
            user_answer = request.POST.get(f"answer_{quiz.id}")
            # Get the shuffled order mapping from hidden field
            order_mapping_json = request.POST.get(f"order_{quiz.id}", "[]")
            try:
                order_mapping = json.loads(order_mapping_json)
            except (json.JSONDecodeError, TypeError):
                order_mapping = list(range(len(quiz.options)))
            
            is_correct = False
            user_answer_index = None
            user_answer_text = "Not answered"
            shuffled_index = None
            
            if user_answer is not None:
                try:
                    shuffled_index = int(user_answer)
                    # Map shuffled index back to original index
                    if 0 <= shuffled_index < len(order_mapping):
                        original_index = order_mapping[shuffled_index]
                        user_answer_index = original_index
                        if 0 <= original_index < len(quiz.options):
                            user_answer_text = quiz.options[original_index]
                            is_correct = original_index == quiz.correct_answer_index
                            if is_correct:
                                correct_answers += 1
                except (ValueError, TypeError):
                    pass
            
            results.append({
                "quiz": quiz,
                "user_answer_index": user_answer_index,
                "user_answer_text": user_answer_text,
                "is_correct": is_correct,
            })
        
        score_percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0

        score_saved = False
        if request.user.is_authenticated and total_questions > 0:
            quiz_score, _created = QuizScore.objects.get_or_create(
                user=request.user,
                exhibit=exhibit,
                defaults={
                    "total_questions": total_questions,
                    "correct_answers": correct_answers,
                    "score_percentage": score_percentage,
                },
            )
            # Always keep the best score
            if correct_answers > quiz_score.correct_answers:
                quiz_score.total_questions = total_questions
                quiz_score.correct_answers = correct_answers
                quiz_score.score_percentage = score_percentage
                quiz_score.save()
            score_saved = True

        return render(request, "exhibits/quiz_results.html", {
            "exhibit": exhibit,
            "results": results,
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "score_percentage": round(score_percentage, 1),
            "score_saved": score_saved,
        })
    
    # GET request - show quiz with randomized options
    quizzes_with_shuffled = []
    for quiz in quizzes:
        # Create a list of indices and shuffle them
        indices = list(range(len(quiz.options)))
        random.shuffle(indices)
        
        # Create shuffled options list
        shuffled_options = [quiz.options[i] for i in indices]
        
        # Create mapping: shuffled_index -> original_index
        # This tells us which original index is at each shuffled position
        order_mapping = indices
        
        quizzes_with_shuffled.append({
            "quiz": quiz,
            "shuffled_options": shuffled_options,
            "order_mapping": json.dumps(order_mapping),  # Serialize as JSON string
        })
    
    return render(request, "exhibits/quiz.html", {
        "exhibit": exhibit,
        "quizzes": quizzes_with_shuffled,
    })

def health(request):
    return JsonResponse({"status": "ok"})


def signup(request):
    """User registration view."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user, defaults={"access_level": "user"})
            login(request, user)
            next_url = request.GET.get("next") or reverse("home")
            return redirect(next_url)
    else:
        form = UserCreationForm()

    return render(request, "exhibits/signup.html", {"form": form})


def login_view(request):
    """User login view."""
    next_url = request.GET.get("next") or reverse("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_to = request.POST.get("next") or next_url
            return redirect(redirect_to)
    else:
        form = AuthenticationForm(request)

    return render(
        request,
        "exhibits/login.html",
        {"form": form, "next": next_url},
    )


def logout_view(request):
    """Log the user out and redirect to home."""
    logout(request)
    return redirect("home")


# ---------------------------------------------------------------------------
# Profile
# ---------------------------------------------------------------------------

@login_required
def profile_view(request):
    """Profile page with tabs: scores, account, permissions (access level)."""
    tab = (request.GET.get("tab") or "scores").strip().lower()
    if tab not in ("scores", "account", "access"):
        tab = "scores"

    # Ensure user has a profile (for access level)
    profile, _ = UserProfile.objects.get_or_create(user=request.user, defaults={"access_level": "user"})

    # Quiz scores for tab 1
    quiz_scores = QuizScore.objects.filter(user=request.user).select_related("exhibit").order_by("exhibit__title")

    # Forms for tab 2
    username_form = UsernameChangeForm(user=request.user)
    password_form = PasswordChangeForm(user=request.user)

    # Admin panel data: all users with profiles (for permissions tab)
    all_users = []
    if profile.is_admin:
        users = User.objects.all().order_by("username")
        for u in users:
            up, _ = UserProfile.objects.get_or_create(user=u, defaults={"access_level": "user"})
            all_users.append({"user": u, "profile": up})

    return render(request, "exhibits/profile.html", {
        "active_tab": tab,
        "quiz_scores": quiz_scores,
        "username_form": username_form,
        "password_form": password_form,
        "user_profile": profile,
        "all_users": all_users,
    })


@login_required
@require_POST
def profile_change_username(request):
    form = UsernameChangeForm(request.POST, user=request.user)
    if form.is_valid():
        request.user.username = form.cleaned_data["new_username"]
        request.user.save()
        messages.success(request, "Your username has been updated.")
    else:
        for _field, errors in form.errors.items():
            for err in errors:
                messages.error(request, err)
    return redirect(reverse("profile") + "?tab=account")


@login_required
@require_POST
def profile_change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        messages.success(request, "Your password has been changed.")
    else:
        for _field, errors in form.errors.items():
            for err in errors:
                messages.error(request, err)
    return redirect(reverse("profile") + "?tab=account")


@login_required
@require_POST
def profile_delete_scores(request):
    QuizScore.objects.filter(user=request.user).delete()
    messages.success(request, "All your quiz scores have been deleted.")
    return redirect(reverse("profile") + "?tab=account")


@login_required
@require_POST
def profile_delete_account(request):
    user = request.user
    logout(request)
    user.delete()
    messages.success(request, "Your account has been deleted.")
    return redirect("home")


# ---------------------------------------------------------------------------
# Admin panel (admin-only)
# ---------------------------------------------------------------------------

@admin_required
@require_POST
def admin_edit_user_role(request, user_id):
    """Admin: change a user's role."""
    target_user = get_object_or_404(User, pk=user_id)
    form = UserRoleForm(request.POST)
    if form.is_valid():
        profile, _ = UserProfile.objects.get_or_create(user=target_user, defaults={"access_level": "user"})
        profile.access_level = form.cleaned_data["access_level"]
        profile.save()
        messages.success(request, f"Role for {target_user.username} updated to {profile.get_access_level_display()}.")
    else:
        messages.error(request, "Invalid role selection.")
    return redirect(reverse("profile") + "?tab=access")


@admin_required
@require_POST
def admin_delete_user(request, user_id):
    """Admin: delete another user's account."""
    target_user = get_object_or_404(User, pk=user_id)
    if target_user.id == request.user.id:
        messages.error(request, "You cannot delete your own account from here.")
        return redirect(reverse("profile") + "?tab=access")
    username = target_user.username
    target_user.delete()
    messages.success(request, f"Account {username} has been deleted.")
    return redirect(reverse("profile") + "?tab=access")


@admin_required
@require_POST
def admin_delete_user_scores(request, user_id):
    """Admin: delete all quiz scores for a user."""
    target_user = get_object_or_404(User, pk=user_id)
    count, _ = QuizScore.objects.filter(user=target_user).delete()
    messages.success(request, f"Deleted {count} quiz score(s) for {target_user.username}.")
    return redirect(reverse("profile") + "?tab=access")


@admin_required
def admin_user_comments(request, user_id):
    """Admin: view all comments by a user with links to exhibits."""
    target_user = get_object_or_404(User, pk=user_id)
    comments = Comment.objects.filter(user=target_user).select_related("exhibit").order_by("-created_at")
    return render(request, "exhibits/admin_user_comments.html", {
        "target_user": target_user,
        "comments": comments,
    })


# ---------------------------------------------------------------------------
# Curator: exhibit CRUD
# ---------------------------------------------------------------------------

@curator_required
def exhibit_create(request):
    """Curator: create a new exhibit."""
    if request.method == "POST":
        form = ExhibitForm(request.POST, request.FILES)
        if form.is_valid():
            exhibit = form.save()
            messages.success(request, f"Exhibit '{exhibit.title}' created.")
            return redirect("exhibits:detail", pk=exhibit.pk)
    else:
        form = ExhibitForm()
    return render(request, "exhibits/exhibit_form.html", {"form": form, "exhibit": None, "is_edit": False})


@curator_required
def exhibit_edit(request, pk):
    """Curator: edit an exhibit."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    if request.method == "POST":
        form = ExhibitForm(request.POST, request.FILES, instance=exhibit)
        if form.is_valid():
            form.save()
            messages.success(request, f"Exhibit '{exhibit.title}' updated.")
            return redirect("exhibits:detail", pk=exhibit.pk)
    else:
        form = ExhibitForm(instance=exhibit)
    return render(request, "exhibits/exhibit_form.html", {"form": form, "exhibit": exhibit, "is_edit": True})


@curator_required
@require_POST
def exhibit_delete(request, pk):
    """Curator: delete an exhibit."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    title = exhibit.title
    exhibit.delete()
    messages.success(request, f"Exhibit '{title}' deleted.")
    return redirect("home")


@curator_required
def quiz_manage(request, pk):
    """Curator: add/edit/delete quiz questions for an exhibit."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    quizzes = exhibit.quizzes.all()
    return render(request, "exhibits/quiz_manage.html", {"exhibit": exhibit, "quizzes": quizzes})


@curator_required
def quiz_add(request, pk):
    """Curator: add a quiz question."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.exhibit = exhibit
            quiz.save()
            messages.success(request, "Quiz question added.")
            return redirect("exhibits:quiz_manage", pk=exhibit.pk)
    else:
        form = QuizForm()
    return render(request, "exhibits/quiz_form.html", {"form": form, "exhibit": exhibit, "quiz": None})


@curator_required
def quiz_edit(request, pk, quiz_id):
    """Curator: edit a quiz question."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    quiz = get_object_or_404(Quiz, pk=quiz_id, exhibit=exhibit)
    if request.method == "POST":
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, "Quiz question updated.")
            return redirect("exhibits:quiz_manage", pk=exhibit.pk)
    else:
        form = QuizForm(instance=quiz)
        form.fields["options_text"].initial = "\n".join(quiz.options) if quiz.options else ""
    return render(request, "exhibits/quiz_form.html", {"form": form, "exhibit": exhibit, "quiz": quiz})


@curator_required
@require_POST
def quiz_delete(request, pk, quiz_id):
    """Curator: delete a quiz question."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    quiz = get_object_or_404(Quiz, pk=quiz_id, exhibit=exhibit)
    quiz.delete()
    messages.success(request, "Quiz question deleted.")
    return redirect("exhibits:quiz_manage", pk=exhibit.pk)
