"""
Fade In/Out Transition Effect
Smoothly fades from one image to another
"""

def generate_fade_transition(prev_img_stream, next_img_stream, transition_duration=0.5):
    """
    Generate FFmpeg filter for fade in/out transition
    
    Args:
        prev_img_stream: Previous image stream identifier (e.g., "[img0]")
        next_img_stream: Next image stream identifier (e.g., "[img1]") 
        transition_duration: Duration of fade transition in seconds
    
    Returns:
        String containing FFmpeg filter complex for fade transition
    """
    
    # Create fade out effect on previous image and fade in effect on next image
    fade_filter = (
        f"{prev_img_stream}fade=t=out:st=0:d={transition_duration}:alpha=1[fade_out];"
        f"{next_img_stream}fade=t=in:st=0:d={transition_duration}:alpha=1[fade_in];"
        f"[fade_out][fade_in]overlay=0:0:enable='gte(t,0)'[faded];"
    )
    
    return fade_filter

def get_transition_description():
    """Return description of this transition effect"""
    return "Smooth fade transition that gradually dissolves from one image to another"

def get_transition_name():
    """Return the name of this transition"""
    return "Fade In/Out"
