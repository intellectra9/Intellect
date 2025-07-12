"""
Push Up Transition Effect
New image pushes up from bottom while previous image moves up
"""

def generate_push_up_transition(prev_img_stream, next_img_stream, transition_duration=0.7):
    """
    Generate FFmpeg filter for push up transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of push transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for push up transition
    """
    
    # Create push up effect - new image pushes up from bottom
    push_filter = (
        f"color=black:size=1920:1080:duration={transition_duration}:rate=30[bg_push];"
        f"[bg_push]{prev_img_stream}overlay="
        f"x=0:y='0-t*1080/{transition_duration}':enable='lte(t,{transition_duration})'[push_out];"
        f"[push_out]{next_img_stream}overlay="
        f"x=0:y='1080-t*1080/{transition_duration}':enable='lte(t,{transition_duration})'[push_result];"
    )
    
    return push_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Vertical push transition where new image pushes up from bottom while old image moves up"

def get_transition_name():
    """Return the name of this transition"""
    return "Push Up"
