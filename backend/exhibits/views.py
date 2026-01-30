from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
import json
import random
from .models import Exhibit, Quiz, Comment


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

    # Attach menu metadata (category, severity, categories) to each exhibit
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

    author_name = (request.POST.get("author_name") or "").strip()
    body = (request.POST.get("body") or "").strip()
    parent_id_raw = (request.POST.get("parent_id") or "").strip()

    if not author_name or not body:
        return HttpResponseBadRequest("author_name and body are required")

    parent = None
    if parent_id_raw:
        try:
            parent_id = int(parent_id_raw)
        except ValueError:
            return HttpResponseBadRequest("parent_id must be an integer")
        parent = get_object_or_404(Comment, pk=parent_id, exhibit=exhibit)

    Comment.objects.create(
        exhibit=exhibit,
        parent=parent,
        author_name=author_name[:80],
        body=body[:2000],
    )

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
        
        return render(request, "exhibits/quiz_results.html", {
            "exhibit": exhibit,
            "results": results,
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "score_percentage": round(score_percentage, 1),
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
