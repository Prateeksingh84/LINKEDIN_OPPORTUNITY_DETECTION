# src/qualifier.py

def score_opportunity(post, company_info):
    """
    Scores an opportunity based on post engagement and company information.

    Args:
        post (dict): A dictionary containing post details.
        company_info (dict): A dictionary containing company information.

    Returns:
        dict: A dictionary containing the score and priority of the opportunity.
    """
    engagement_score = post["likes"] * 0.5 + post["comments"] * 0.3 + post["shares"] * 0.2
    company_score = company_info["employee_count"] * 0.4 + company_info["revenue"] * 0.6

    total_score = engagement_score + company_score
    priority = "high" if total_score > 70 else "medium" if total_score > 40 else "low"

    return {"score": total_score, "priority": priority}

def qualify_posts(post):
    """
    Qualifies a post based on its content.

    Args:
        post (dict): A dictionary containing post details.

    Returns:
        dict: A dictionary containing the qualification status of the post.
    """
    return {"content": post["content"], "status": "qualified" if "agency" in post["content"].lower() else "unqualified"}
    
    