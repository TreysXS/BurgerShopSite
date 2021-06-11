def save_user_profile(user_form, profile_form):
    """Save model user and model profile."""
    user_form.save()
    profile_form.save()