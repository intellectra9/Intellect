"""
Slide Right Transition Effect
New image slides in from the left while previous image slides out to the right
"""

def generate_slide_right_transition(prev_img_stream, next_img_stream, transition_duration=0.6):
    """
    Generate FFmpeg filter for slide right transition
    
    Args:
        prev_img_stream: Previous image stream identifier
        next_img_stream: Next image stream identifier
        transition_duration: Duration of slide transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for slide right transition
    """
    
    # Create slide right effect - new image slides in from left, old slides out to right
    slide_filter = (
        f"color=black:size=1920:1080:duration={transition_duration}:rate=30[bg_slide];"
        f"[bg_slide]{prev_img_stream}overlay="
        f"x='t*1920/{transition_duration}':y=0:enable='lte(t,{transition_duration})'[slide_out];"
        f"[slide_out]{next_img_stream}overlay="
        f"x='-1920+t*1920/{transition_duration}':y=0:enable='lte(t,{transition_duration})'[slide_result];"
    )
    
    return slide_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Horizontal slide transition where new image slides in from left while old image slides out to right"

def get_transition_name():
    """Return the name of this transition"""
    return "Slide Right"
