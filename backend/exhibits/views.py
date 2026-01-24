from django.shortcuts import render, get_object_or_404
import json
import random
from .models import Exhibit, Quiz

def exhibit_list(request):
    exhibits = Exhibit.objects.all()
    return render(request, "exhibits/exhibit_list.html", {
        "exhibits": exhibits
    })

def exhibit_detail(request, pk):
    exhibit = get_object_or_404(Exhibit, pk=pk)
    return render(request, "exhibits/exhibit_detail.html", {
        "exhibit": exhibit,
    })

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
