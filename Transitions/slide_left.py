"""
Slide Left Transition Effect
New image slides in from the right while previous image slides out to the left
"""

def generate_slide_left_transition(prev_img_stream, next_img_stream, transition_duration=0.6):
    """
    Generate FFmpeg filter for slide left transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of slide transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for slide left transition
    """
    
    # Create slide left effect - new image slides in from right, old slides out to left
    slide_filter = (
        f"color=black:size=1920:1080:duration={transition_duration}:rate=30[bg_slide];"
        f"[bg_slide]{prev_img_stream}overlay="
        f"x='0-t*1920/{transition_duration}':y=0:enable='lte(t,{transition_duration})'[slide_out];"
        f"[slide_out]{next_img_stream}overlay="
        f"x='1920-t*1920/{transition_duration}':y=0:enable='lte(t,{transition_duration})'[slide_result];"
    )
    
    return slide_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Horizontal slide transition where new image slides in from right while old image slides out to left"

def get_transition_name():
    """Return the name of this transition"""
    return "Slide Left"
