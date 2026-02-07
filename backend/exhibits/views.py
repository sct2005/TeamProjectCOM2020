from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
import random
from .models import Exhibit, Quiz, Comment, QuizScore, UserProfile
from .forms import UsernameChangeForm


# Menu page design: map exhibit title -> category, severity, categories (tags)
# Matches "Menu Page for Topics" design. Fallback: domain as category, severity 'medium'
EXHIBIT_MENU_META = {
    "Flood Risk Map Overconfidence": {"category": "Environmental", "severity": "high", "categories": ["Flooding", "Risk Assessment"]},
    "Replit AI Agent Database Wipe": {"category": "Tech", "severity": "critical", "categories": ["Tech", "Data Loss"]},
    "Grok Generating Sexual Images": {"category": "Social Media", "severity": "high", "categories": ["Social Media", "Content Moderation"]},
    "Racial Bias in Healthcare AI Risk Prediction": {"category": "Healthcare", "severity": "critical", "categories": ["Healthcare", "Bias & Ethics"]},
    "DeepSeek Taiwan Censorship Case Study": {"category": "International", "severity": "medium", "categories": ["Tech", "International Relations"]},
    "Parents Sue OpenAI for Role in Teenager Taking His Own Life": {"category": "Social Impact", "severity": "critical", "categories": ["Tech", "Life/Social/Wellbeing"]},
    "Grok AI Makes Antisemitic Comments and Hate Speech Output Failure": {"category": "AI Safety", "severity": "critical", "categories": ["AI Safety", "Hate Speech", "Misinformation"]},
    "Zillow Offers: Algorithmic Home Pricing Collapse": {"category": "Finance", "severity": "high", "categories": ["AI in Finance", "Real Estate", "Predictive Modeling"]},
    "Meta BlenderBot: Misinformation Propagation": {"category": "Social Media", "severity": "high", "categories": ["Conversational AI", "LLM Moderation", "Social Media"]},
    "Amazon Alexa: Gender and Bias Controversies": {"category": "Consumer Tech", "severity": "medium", "categories": ["Voice Assistants", "AI Ethics", "Consumer Devices"]},
    "Air Canada Chatbot: Hallucinated Refund Policy": {"category": "Consumer Tech", "severity": "medium", "categories": ["Consumer AI", "Customer Service"]},
}


def home(request):
    """Homepage: Menu Page for Topics design — case study cards with category filter."""
    exhibits = list(Exhibit.objects.all().order_by("title"))
    selected_category = (request.GET.get("category") or "all").strip()

    # Preload quiz scores for the authenticated user (for badge display)
    user_scores_by_exhibit_id = {}
    if request.user.is_authenticated:
        user_scores = QuizScore.objects.filter(user=request.user)
        user_scores_by_exhibit_id = {qs.exhibit_id: qs for qs in user_scores}

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

    # Unique categories for tabs (from exhibits)
    categories = ["all"] + sorted({ex.menu_category for ex in exhibits if ex.menu_category}, key=str.lower)
    total_count = len(exhibits)
    critical_count = sum(1 for ex in exhibits if ex.menu_severity == "critical")
    category_count = len(categories) - 1  # exclude 'all'

    if selected_category != "all":
        exhibits = [ex for ex in exhibits if ex.menu_category == selected_category]

    return render(request, "exhibits/home.html", {
        "exhibits": exhibits,
        "categories": categories,
        "selected_category": selected_category,
        "total_count": total_count,
        "critical_count": critical_count,
        "category_count": category_count,
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
    return render(request, "exhibits/exhibit_detail.html", {
        "exhibit": exhibit,
        "comments": comments,
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


@require_POST
def delete_comment(request, pk, comment_id):
    """Allow a user to delete their own comment (or replies)."""
    exhibit = get_object_or_404(Exhibit, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id, exhibit=exhibit)

    if not request.user.is_authenticated:
        login_url = reverse("login")
        next_url = reverse("exhibits:detail", args=[exhibit.id]) + "#comments"
        return redirect(f"{login_url}?next={next_url}")

    if comment.user_id != request.user.id:
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
    """Profile page with tabs: scores, account, access level."""
    tab = (request.GET.get("tab") or "scores").strip().lower()
    if tab not in ("scores", "account", "access"):
        tab = "scores"

    # Ensure user has a profile (for access level)
    profile, _ = UserProfile.objects.get_or_create(user=request.user, defaults={"access_level": "viewer"})

    # Quiz scores for tab 1
    quiz_scores = QuizScore.objects.filter(user=request.user).select_related("exhibit").order_by("exhibit__title")

    # Forms for tab 2
    username_form = UsernameChangeForm(user=request.user)
    password_form = PasswordChangeForm(user=request.user)

    return render(request, "exhibits/profile.html", {
        "active_tab": tab,
        "quiz_scores": quiz_scores,
        "username_form": username_form,
        "password_form": password_form,
        "user_profile": profile,
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
