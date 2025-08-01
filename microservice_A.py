import json
import os
from datetime import datetime

SESSION_FILE="typingsessionresults.txt"
TOP_SCORE_FILE="UserTopScores.txt"

def parse_sessions_for_user(username):
    top_session=None
    top_score=-1
    if not os.path.exists(SESSION_FILE):
        return None
    with open(SESSION_FILE, "r") as file:
        buffer=""
        for line in file:
            if line.startswith("Record ID:"):
                # New block starting, parse previous block
                if buffer.strip():
                    try:
                        session=json.loads(buffer.strip())
                        if session.get("username") == username:
                            score=session.get("sessionScore",-1)
                            if score>top_score:
                                top_score=score
                                top_session = session
                    except json.JSONDecodeError:
                        pass
                buffer = ""  # Reset for next block
            else:
                buffer += line
        # Handle last block in file
        if buffer.strip():
            try:
                session = json.loads(buffer.strip())
                if session.get("username")==username:
                    score=session.get("sessionScore",-1)
                    if score>top_score:
                        top_score=score
                        top_session=session
            except json.JSONDecodeError:
                pass
    return top_session

def save_top_score(session):
    if session is None:
        return

    # Load existing top scores
    top_scores=[]
    if os.path.exists(TOP_SCORE_FILE):
        with open(TOP_SCORE_FILE, "r") as f:
            try:
                top_scores=json.load(f)
            except json.JSONDecodeError:
                top_scores=[]
    # Replace old top score for user or append new
    updated=False
    for i,s in enumerate(top_scores):
        if s["username"]==session["username"]:
            if s["sessionScore"]<session["sessionScore"]:
                top_scores[i]=session
            updated=True
            break
    if not updated:
        top_scores.append(session)
    # Save back
    with open(TOP_SCORE_FILE, "w") as f:
        json.dump(top_scores, f, indent=2)
def get_saved_top_score(username):
    if not os.path.exists(TOP_SCORE_FILE):
        return None
    with open(TOP_SCORE_FILE, "r") as f:
        try:
            scores=json.load(f)
            for s in scores:
                if s["username"]==username:
                    return s
        except json.JSONDecodeError:
            return None
    return None

# Entry point for main service to call
def update_user_top_score(username):
    top = parse_sessions_for_user(username)
    save_top_score(top)
    return top
